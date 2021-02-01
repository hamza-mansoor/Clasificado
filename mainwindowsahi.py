


from PyQt5 import QtCore, QtGui, QtWidgets
#import forlogo_rc
from prepro import Ui_PreProcessing
from statisticswindowsublimesahi import Ui_SmainWindow
from classfiers import Ui_MainWindow1
from formatconver import Ui_MainWindowf

class Ui_MainWindow(object):

    def openWindowprepro(self):
        try:
            self.window=QtWidgets.QMainWindow()
            self.ui = Ui_PreProcessing()
            self.ui.setupUi(self.window)
            #MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(repr(e))
        

    def openWindowstatistics(self):
        try:
            self.window=QtWidgets.QMainWindow()
            self.ui = Ui_SmainWindow()
            self.ui.setupUi(self.window)
            #MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(repr(e))    


    def openWindowclassifiers(self):
        try:
            self.window=QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow1()
            self.ui.setupUi(self.window)
            #MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(repr(e))       

    def openfileconvert(self):
        try:
            self.window=QtWidgets.QMainWindow()
            self.ui = Ui_MainWindowf()
            self.ui.setupUi(self.window)
            #MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(repr(e))        
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(True)
       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 5, 500, 500))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 900, 200, 50))
        self.label.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 930, 430, 50))
        self.label.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 960, 200, 50))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 990, 200, 50))
        self.label_5.setObjectName("label_5")
        self.prepros = QtWidgets.QPushButton(self.centralwidget)
        self.prepros.setGeometry(QtCore.QRect(50, 570, 350, 60))
        self.prepros.setObjectName("prepros")
        self.statistics = QtWidgets.QPushButton(self.centralwidget)
        self.statistics.setGeometry(QtCore.QRect(500, 570, 350, 60))
        self.statistics.setObjectName("statistics")
        self.classify = QtWidgets.QPushButton(self.centralwidget)
        self.classify.setGeometry(QtCore.QRect(950, 570, 350, 60))
        self.classify.setObjectName("classify")
        self.convertion = QtWidgets.QPushButton(self.centralwidget)
        self.convertion.setGeometry(QtCore.QRect(1400, 570, 500, 60))
        self.convertion.setObjectName("convertion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clasificado"))
        self.label_2.setText(_translate("MainWindow", "Clasificado"))
        self.label_3.setText(_translate("MainWindow", "A Project By University Of Lahore"))
        self.label_4.setText(_translate("MainWindow", "Islamabad"))
        self.label_5.setText(_translate("MainWindow", "Pakistan"))
        self.prepros.setText(_translate("MainWindow", "Pre-Processing"))
        self.statistics.setText(_translate("MainWindow", "Data Analysis"))
        self.classify.setText(_translate("MainWindow", "Classification"))
        self.convertion.setText(_translate("MainWindow", ".ARFF to .CSV Conversion"))

        self.prepros.clicked.connect(self.openWindowprepro)
        self.statistics.clicked.connect(self.openWindowstatistics)
        self.classify.clicked.connect(self.openWindowclassifiers)
        self.convertion.clicked.connect(self.openfileconvert)

        self.statistics.setStyleSheet(
        """QPushButton {
                           
                             background-color:#ADD8E6;
                                border-style: outset;
                                border-width: 2px;
                                border-radius: 10px;
                                border-color: beige;
                                font: bold 30px;
                                min-width: 10em;
                                padding: 6px;}""")

        self.prepros.setStyleSheet(
        """QPushButton {
                           
                             background-color:#ADD8E6;
                                border-style: outset;
                                border-width: 2px;
                                border-radius: 10px;
                                border-color: beige;
                                font: bold 30px;
                                min-width: 10em;
                                padding: 6px;}""")

        self.classify.setStyleSheet(
        """QPushButton {
                           
                             background-color:#ADD8E6;
                                border-style: outset;
                                border-width: 2px;
                                border-radius: 10px;
                                border-color: beige;
                                font: bold 30px;
                                min-width: 10em;
                                padding: 6px;}""")

        self.convertion.setStyleSheet(
        """QPushButton {
                           
                             background-color:#ADD8E6;
                                border-style: outset;
                                border-width: 2px;
                                border-radius: 10px;
                                border-color: beige;
                                font: bold 30px;
                                min-width: 10em;
                                padding: 6px;}""")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
