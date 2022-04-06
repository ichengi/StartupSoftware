# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 600)
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(20, 380, 121, 111))
        font = QFont()
        font.setPointSize(15)
        self.StartButton.setFont(font)
        self.MessageShow = QTextBrowser(self.centralwidget)
        self.MessageShow.setObjectName(u"MessageShow")
        self.MessageShow.setGeometry(QRect(435, 0, 361, 571))
        font1 = QFont()
        font1.setPointSize(12)
        self.MessageShow.setFont(font1)
        self.MessageShow.setLineWidth(1)
        self.BlueStacks = QCheckBox(self.centralwidget)
        self.BlueStacks.setObjectName(u"BlueStacks")
        self.BlueStacks.setGeometry(QRect(30, 140, 141, 41))
        self.BlueStacks.setFont(font1)
        self.BlueStacks.setChecked(True)
        self.MAA = QCheckBox(self.centralwidget)
        self.MAA.setObjectName(u"MAA")
        self.MAA.setGeometry(QRect(30, 110, 141, 41))
        self.MAA.setFont(font1)
        self.MAA.setChecked(True)
        self.QQ = QCheckBox(self.centralwidget)
        self.QQ.setObjectName(u"QQ")
        self.QQ.setGeometry(QRect(30, 80, 141, 41))
        self.QQ.setFont(font1)
        self.QQ.setChecked(True)
        self.FinalShell = QCheckBox(self.centralwidget)
        self.FinalShell.setObjectName(u"FinalShell")
        self.FinalShell.setGeometry(QRect(30, 230, 151, 41))
        self.FinalShell.setFont(font1)
        self.FinalShell.setChecked(True)
        self.FlashPlayer = QCheckBox(self.centralwidget)
        self.FlashPlayer.setObjectName(u"FlashPlayer")
        self.FlashPlayer.setGeometry(QRect(30, 290, 151, 41))
        self.FlashPlayer.setFont(font1)
        self.FlashPlayer.setChecked(True)
        self.CMD = QCheckBox(self.centralwidget)
        self.CMD.setObjectName(u"CMD")
        self.CMD.setGeometry(QRect(30, 260, 151, 41))
        self.CMD.setFont(font1)
        self.CMD.setChecked(True)
        self.Navicat = QCheckBox(self.centralwidget)
        self.Navicat.setObjectName(u"Navicat")
        self.Navicat.setGeometry(QRect(30, 200, 151, 41))
        self.Navicat.setFont(font1)
        self.Navicat.setChecked(True)
        self.Chrome = QCheckBox(self.centralwidget)
        self.Chrome.setObjectName(u"Chrome")
        self.Chrome.setGeometry(QRect(30, 170, 141, 41))
        self.Chrome.setFont(font1)
        self.Chrome.setChecked(True)
        self.PyCharm = QCheckBox(self.centralwidget)
        self.PyCharm.setObjectName(u"PyCharm")
        self.PyCharm.setGeometry(QRect(30, 20, 141, 41))
        self.PyCharm.setFont(font1)
        self.PyCharm.setChecked(True)
        self.WeChat = QCheckBox(self.centralwidget)
        self.WeChat.setObjectName(u"WeChat")
        self.WeChat.setGeometry(QRect(30, 50, 141, 41))
        self.WeChat.setFont(font1)
        self.WeChat.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 795, 33))
        self.menuBar.setFont(font)
        self.startPro = QMenu(self.menuBar)
        self.startPro.setObjectName(u"startPro")
        self.Prolist = QButtonGroup()
        self.Prolist.setExclusive(False)
        self.Prolist.addButton(self.PyCharm)
        self.Prolist.addButton(self.WeChat)
        self.Prolist.addButton(self.QQ)
        self.Prolist.addButton(self.MAA)
        self.Prolist.addButton(self.BlueStacks)
        self.Prolist.addButton(self.Chrome)
        self.Prolist.addButton(self.Navicat)
        self.Prolist.addButton(self.FinalShell)
        self.Prolist.addButton(self.CMD)
        self.Prolist.addButton(self.FlashPlayer)
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.startPro.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)



    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4fbf\u6377\u5c0f\u7a0b\u5e8f", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"LinkStart!", None))
        # self.Prolist.setText(QCoreApplication.translate("MainWindow", u"Prolist", None))
        self.BlueStacks.setText(QCoreApplication.translate("MainWindow", u"BlueStacks", None))
        self.MAA.setText(QCoreApplication.translate("MainWindow", u"MAA", None))
        self.QQ.setText(QCoreApplication.translate("MainWindow", u"QQ", None))
        self.FinalShell.setText(QCoreApplication.translate("MainWindow", u"FinalShell", None))
        self.FlashPlayer.setText(QCoreApplication.translate("MainWindow", u"FlashPlayer", None))
        self.CMD.setText(QCoreApplication.translate("MainWindow", u"CMD", None))
        self.Navicat.setText(QCoreApplication.translate("MainWindow", u"Navicat", None))
        self.Chrome.setText(QCoreApplication.translate("MainWindow", u"Chrome", None))
        self.PyCharm.setText(QCoreApplication.translate("MainWindow", u"PyCharm", None))
        self.WeChat.setText(QCoreApplication.translate("MainWindow", u"WeChat", None))
        self.startPro.setTitle(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u5f00\u59cb", None))
    # retranslateUi

