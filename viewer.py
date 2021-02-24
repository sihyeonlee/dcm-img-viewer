# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainView(object):
    def setupUi(self, MainView):
        if not MainView.objectName():
            MainView.setObjectName(u"MainView")
        MainView.resize(1300, 600)
        self.centralwidget = QWidget(MainView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.val_ww = QPlainTextEdit(self.centralwidget)
        self.val_ww.setObjectName(u"val_ww")
        self.val_ww.setGeometry(QRect(380, 180, 81, 21))
        self.val_ww.setFocusPolicy(Qt.StrongFocus)
        self.val_ww.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.val_ww.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.val_ww.setTabChangesFocus(True)
        self.val_ww.setUndoRedoEnabled(False)
        self.val_ww.setOverwriteMode(True)
        self.txt_WW = QPlainTextEdit(self.centralwidget)
        self.txt_WW.setObjectName(u"txt_WW")
        self.txt_WW.setGeometry(QRect(17, 160, 31, 21))
        self.txt_WW.setFocusPolicy(Qt.NoFocus)
        self.txt_WW.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.txt_WW.setFrameShape(QFrame.NoFrame)
        self.txt_WW.setFrameShadow(QFrame.Plain)
        self.txt_WW.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_WW.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_WW.setTextInteractionFlags(Qt.NoTextInteraction)
        self.txt_WC = QPlainTextEdit(self.centralwidget)
        self.txt_WC.setObjectName(u"txt_WC")
        self.txt_WC.setGeometry(QRect(16, 100, 31, 21))
        self.txt_WC.setFocusPolicy(Qt.NoFocus)
        self.txt_WC.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.txt_WC.setFrameShape(QFrame.NoFrame)
        self.txt_WC.setFrameShadow(QFrame.Plain)
        self.txt_WC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_WC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_WC.setTextInteractionFlags(Qt.NoTextInteraction)
        self.val_wc = QPlainTextEdit(self.centralwidget)
        self.val_wc.setObjectName(u"val_wc")
        self.val_wc.setGeometry(QRect(380, 120, 81, 21))
        self.val_wc.setFocusPolicy(Qt.StrongFocus)
        self.val_wc.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.val_wc.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.val_wc.setTabChangesFocus(True)
        self.val_wc.setUndoRedoEnabled(False)
        self.val_wc.setOverwriteMode(True)
        self.val_file_path = QPlainTextEdit(self.centralwidget)
        self.val_file_path.setObjectName(u"val_file_path")
        self.val_file_path.setGeometry(QRect(20, 40, 441, 51))
        self.val_file_path.setFocusPolicy(Qt.NoFocus)
        self.val_file_path.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.val_file_path.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.val_file_path.setReadOnly(True)
        self.txt_Path = QPlainTextEdit(self.centralwidget)
        self.txt_Path.setObjectName(u"txt_Path")
        self.txt_Path.setGeometry(QRect(16, 20, 41, 21))
        self.txt_Path.setFocusPolicy(Qt.NoFocus)
        self.txt_Path.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.txt_Path.setFrameShape(QFrame.NoFrame)
        self.txt_Path.setFrameShadow(QFrame.Plain)
        self.txt_Path.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_Path.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_Path.setTextInteractionFlags(Qt.NoTextInteraction)
        self.txt_log = QPlainTextEdit(self.centralwidget)
        self.txt_log.setObjectName(u"txt_log")
        self.txt_log.setGeometry(QRect(10, 260, 451, 331))
        self.txt_log.setFocusPolicy(Qt.NoFocus)
        self.txt_log.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_log.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_log.setUndoRedoEnabled(False)
        self.txt_log.setReadOnly(True)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(461, -30, 20, 641))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.slider_wc = QSlider(self.centralwidget)
        self.slider_wc.setObjectName(u"slider_wc")
        self.slider_wc.setGeometry(QRect(20, 120, 351, 22))
        self.slider_wc.setMinimum(-1000)
        self.slider_wc.setMaximum(1000)
        self.slider_wc.setOrientation(Qt.Horizontal)
        self.slider_ww = QSlider(self.centralwidget)
        self.slider_ww.setObjectName(u"slider_ww")
        self.slider_ww.setGeometry(QRect(20, 180, 351, 22))
        self.slider_ww.setMaximum(1000)
        self.slider_ww.setOrientation(Qt.Horizontal)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(480, 6, 813, 588))
        self.layout = QGridLayout(self.gridLayoutWidget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 230, 451, 25))
        self.layout1 = QGridLayout(self.widget)
        self.layout1.setObjectName(u"layout1")
        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setFocusPolicy(Qt.NoFocus)

        self.layout1.addWidget(self.btn_save, 0, 2, 1, 1)

        self.btn_load = QPushButton(self.widget)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setFocusPolicy(Qt.NoFocus)

        self.layout1.addWidget(self.btn_load, 0, 0, 1, 1)

        self.btn_view = QPushButton(self.widget)
        self.btn_view.setObjectName(u"btn_view")
        self.btn_view.setFocusPolicy(Qt.NoFocus)

        self.layout1.addWidget(self.btn_view, 0, 1, 1, 1)

        MainView.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainView)
        self.btn_load.clicked.connect(MainView.loadfile)
        self.btn_view.clicked.connect(MainView.view)
        self.btn_save.clicked.connect(MainView.save)
        self.val_wc.textChanged.connect(MainView.wc_slide)
        self.val_ww.textChanged.connect(MainView.ww_slide)
        self.slider_wc.sliderMoved.connect(MainView.wc_text)
        self.slider_ww.sliderMoved.connect(MainView.ww_text)

        QMetaObject.connectSlotsByName(MainView)
    # setupUi

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(QCoreApplication.translate("MainView", u"MainWindow", None))
        self.txt_WW.setPlainText(QCoreApplication.translate("MainView", u"WW", None))
        self.txt_WC.setPlainText(QCoreApplication.translate("MainView", u"WC", None))
        self.txt_Path.setPlainText(QCoreApplication.translate("MainView", u"Path", None))
        self.btn_save.setText(QCoreApplication.translate("MainView", u"Save", None))
        self.btn_load.setText(QCoreApplication.translate("MainView", u"Load", None))
        self.btn_view.setText(QCoreApplication.translate("MainView", u"View", None))
    # retranslateUi

