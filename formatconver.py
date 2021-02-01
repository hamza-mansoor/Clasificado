

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QListWidget, QSizePolicy,QVBoxLayout,QDesktopWidget
from scipy.io import arff
import pandas

class Ui_MainWindowf(object):
    def setupUi(self, MainWindow):
        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browseFile = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile.setGeometry(QtCore.QRect((200/3840)*width, (50/2160)*height, (350/3840)*width, (50/2160)*height))
        self.browseFile.setObjectName("browseFile")


        self.filenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.filenameLabel.setGeometry(QtCore.QRect((700/3840)*width, (55/2160)*height, (350/3840)*width, (70/2160)*height))
        self.filenameLabel.setObjectName("filenameLabel")

        self.conver = QtWidgets.QPushButton(self.centralwidget)
        self.conver.setGeometry(QtCore.QRect((200/3840)*width, (150/2160)*height, (350/3840)*width, (50/2160)*height))
        self.conver.setObjectName("conver")
        self.conver.hide()


        self.responce = QtWidgets.QLabel(self.centralwidget)
        self.responce.setGeometry(QtCore.QRect((700/3840)*width, (150/2160)*height, (350/3840)*width, (70/2160)*height))
        self.responce.setObjectName("responce")

        self.savefile = QtWidgets.QPushButton(self.centralwidget)
        self.savefile.setGeometry(QtCore.QRect((200/3840)*width, (250/2160)*height, (350/3840)*width, (50/2160)*height))
        self.savefile.setObjectName("savefile")
        self.savefile.hide()


        self.msgback = QtWidgets.QLabel(self.centralwidget)
        self.msgback.setGeometry(QtCore.QRect((700/3840)*width, (250/2160)*height, (350/3840)*width, (70/2160)*height))
        self.msgback.setObjectName("msgback")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", ".arff to .csv conversion"))
        self.browseFile.setText(_translate("SmainWindow", "Open File"))
        self.browseFile.clicked.connect(self.pushButton_handler)
        self.filenameLabel.setText(_translate("SmainWindow", ""))
        self.conver.setText("Convert File")
        self.savefile.setText("Save File")
        self.conver.clicked.connect(self.convert)
        self.savefile.clicked.connect(self.save)

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(None, 'Open File', r"~/Desktop", '*.arff')
        self.path = filename[0]

        with open(self.path, "r") as fpath:
            self.filenameLabel.setText(str(self.path))
            self.filenameLabel.adjustSize()  
            self.dataset=arff.loadarff(fpath)
            self.conver.show()
        
    def convert(self):
        self.df = pandas.DataFrame(self.dataset[0])
        print(self.df)
        self.responce.setText("File is Successfully converted to .csv format")
        self.responce.adjustSize() 
        self.savefile.show()

    def save(self):
        try:
            self.df.to_csv(self.path)
            self.msgback.setText("File is saved")
            self.msgback.adjustSize() 
        except Exception as e:
            print(repr(e))    
        

if __name__ == "__main__":
    import sys
    dataset="temp"
    df=""
    path="temp"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowf()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
