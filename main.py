import pydicom
import sys
import datetime
import os
import numpy as np
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QFileDialog
import matplotlib.pyplot as plt
from viewer import Ui_MainView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class DcmViewer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainView()
        self.ui.setupUi(self)

        self.file_load_flag = False

        self.file_path = None
        self.file_name = None
        self.dataset = None
        self.clip_data = None
        self.canvas = None
        self.reslope = None
        self.reinter = None
        self.hu_data = None
        self.ww = 0
        self.wc = 0

        self.ui.val_ww.setPlainText("0")
        self.ui.val_wc.setPlainText("0")

        os.makedirs("results", exist_ok=True)

    def log(self, txt):
        self.ui.txt_log.appendPlainText(txt)

    def clip(self, hu):
        self.wc = int(self.ui.val_wc.toPlainText())
        self.ww = int(self.ui.val_ww.toPlainText())

        return np.clip(hu, self.wc - (self.ww / 2), self.wc + (self.ww / 2))

    def wc_slide(self):
        try:
            self.wc = int(self.ui.val_wc.toPlainText())
        except ValueError:
            return None

        self.ui.slider_wc.setValue(self.wc)

        if self.ww is not None:
            self.view()

    def ww_slide(self):
        try:
            self.ww = int(self.ui.val_ww.toPlainText())
        except ValueError:
            return None

        self.ui.slider_ww.setValue(self.ww)

        if self.wc is not None:
            self.view()

    def wc_text(self, val):
        self.wc = val
        self.ui.val_wc.setPlainText(str(val))

        if self.ww is not None:
            self.view()

    def ww_text(self, val):
        self.ww = val
        self.ui.val_ww.setPlainText(str(val))

        if self.wc is not None:
            self.view()

    def loadfile(self):
        f_dialog = QFileDialog(self)
        f_dialog.setFileMode(QFileDialog.ExistingFile)
        f_dialog.setNameFilter(self.tr("Dicom File (*.dcm)"))
        f_dialog.setViewMode(QFileDialog.Detail)

        if f_dialog.exec_():
            self.file_path = f_dialog.selectedFiles()[0]
            self.ui.val_file_path.setPlainText(str(self.file_path))
            self.file_name = os.path.basename(self.file_path)

        if self.file_path is None:
            self.log("[LOAD::FAIL]")
            return None

        self.dataset = pydicom.dcmread(self.file_path)

        self.reslope = int(self.dataset.RescaleSlope)
        self.reinter = int(self.dataset.RescaleIntercept)

        self.hu_data = self.reslope * self.dataset.pixel_array + self.reinter

        self.log("[LOAD::PASS]  " + self.file_name)
        self.file_load_flag = True

        self.view()

    def view(self):
        if self.file_load_flag is False:
            return None

        if self.canvas is not None:
            self.ui.layout.removeWidget(self.canvas)

        self.clip_data = self.clip(self.hu_data)

        fig = plt.Figure()
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
        self.canvas = FigureCanvasQTAgg(fig)

        self.canvas.resize(self.clip_data.shape[0]*1.2, self.clip_data.shape[1]*1.2)

        self.ui.layout.addWidget(self.canvas)

        fig.clear()

        ax = fig.add_subplot(111)
        ax.imshow(self.clip_data, cmap='gray')
        ax.axis("off")

        self.canvas.draw()

    def save(self):
        if self.file_load_flag is False:
            return None

        self.clip_data = self.clip(self.hu_data)

        now = datetime.datetime.now()

        output = "results//" + now.strftime("%m-%d_%H%M_") + str(self.wc) + "_" + str(self.ww) + "_" \
                    + self.file_name + "_result.png"

        plt.imsave(output, self.clip_data, cmap='gray')

        self.log("[SAVE::PASS]  " + output)


app = QApplication([])
app.setStyle('Fusion')

window = DcmViewer()
window.show()

sys.exit(app.exec_())
