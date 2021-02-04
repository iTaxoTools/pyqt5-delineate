# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diuiGWIOIU.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(781, 385)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(700, 40))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);")

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"border-color: rgb(85, 0, 0);\n"
"selection-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.splitter.addWidget(self.frame_2)

        self.verticalLayout_2.addWidget(self.splitter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Delineate species delimitation", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"DELINEATE approach to species delimitation (Sukumaran, Holder, and Knowles, 2020).", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"species assignment constraints table  file", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"rooted ultrametric population tree", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Choose Tree file data format {nexus,newick}", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Browse output result folder", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"nexus", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"newick", None))

        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Download", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Clear", None))
    # retranslateUi
