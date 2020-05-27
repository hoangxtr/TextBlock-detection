# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/xuanhoang232k/Desktop/infore/textblock app/test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 350, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(100, 60, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.pushButton.clicked.connect(self.foo)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def foo(self):
        # dlg = QtWidgets.QFileDialog(self)
        # dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("Text file (*.txt)")
        # if dlg.exec_():
        #     filenames = dlg.selectedFiles()
        #     print(filenames)
        # else: print("Can't excute ...")

        # path = self.workspaceField.value()
        # if not isPathValid(path):
        # path = expandPath('~')
        dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.AnyFile)
        dlg.getOpenFileName(self.centralwidget, "Open any file", r"/home/xuanhoang232k/Pictures/")
        self.

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click me"))

app = QApplication(sys.argv)
win = QMainWindow()
ui  = Ui_MainWindow()
ui.setupUi(win)
win.show()
sys.exit(app.exec_())
