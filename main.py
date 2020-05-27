from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1448, 917)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 380, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_image)

        self.rootImage = QtWidgets.QLabel(self.centralwidget)
        self.rootImage.setGeometry(QtCore.QRect(60, 100, 571, 591))
        self.rootImage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rootImage.setFrameShape(QtWidgets.QFrame.Box)
        self.rootImage.setText("")
        self.rootImage.setObjectName("rootImage")

        self.resContent = QtWidgets.QLabel(self.centralwidget)
        self.resContent.setGeometry(QtCore.QRect(380, 710, 841, 161))
        self.resContent.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.resContent.setFrameShape(QtWidgets.QFrame.Box)
        self.resContent.setObjectName("resContent")

        self.resImage = QtWidgets.QLabel(self.centralwidget)
        self.resImage.setGeometry(QtCore.QRect(820, 80, 571, 591))
        self.resImage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.resImage.setFrameShape(QtWidgets.QFrame.Box)
        self.resImage.setText("")
        self.resImage.setObjectName("resImage")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(60, 10, 81, 81))
        self.logo.setFrameShape(QtWidgets.QFrame.Box)
        self.logo.setText("")
        self.logo.setObjectName("logo")
        lg = QPixmap("./asset/logo.png").scaled(self.logo.frameGeometry().width(), self.logo.frameGeometry().height(), Qt.IgnoreAspectRatio)
        self.logo.setPixmap(lg)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1448, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.width = self.rootImage.frameGeometry().width()
        self.height = self.rootImage.frameGeometry().height()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click me"))
        self.resContent.setText(_translate("MainWindow", "TextLabel"))

    def get_image(self):        
        dlg = QFileDialog()
        filename, _ = dlg.getOpenFileName(self.centralwidget, "Open any file", r"./", "All file (*.JPG, *.PNG, *.GIF, *.TIFF)")
        img = QPixmap(filename).scaled(self.width, self.height,  Qt.IgnoreAspectRatio)
        self.rootImage.setPixmap(img)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

