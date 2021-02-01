
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import pandas
from matplotlib.backends.qt_compat import QtWidgets
#from sublime import Ui_MainWindow
import sklearn
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from pyqtgraph import PlotWidget, plot
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice ,QLineSeries
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import numpy as np
from scipy import stats
from glob import iglob
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import io
import csv


class Ui_PreProcessing(object):
    def setupUi(self, PreProcessing):
        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()
        '''screen_resolution = app.desktop().screenGeometry()
                                width, height = screen_resolution.width(), screen_resolution.height()'''
        PreProcessing.setObjectName("PreProcessing")
        PreProcessing.resize((3400/3840)*width,(1400/2160)*height)
        self.centralwidget = QtWidgets.QWidget(PreProcessing)
        self.centralwidget.setObjectName("centralwidget")
        PreProcessing.setCentralWidget(self.centralwidget)

        self.browseFile = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile.setGeometry(QtCore.QRect((200/3840)*width, (50/2160)*height, (350/3840)*width, (50/2160)*height))
        self.browseFile.setObjectName("browseFile")


        self.filenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.filenameLabel.setGeometry(QtCore.QRect((700/3840)*width, (55/2160)*height, (350/3840)*width, (70/2160)*height))
        self.filenameLabel.setObjectName("filenameLabel")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect((40/3840)*width, (120/2160)*height, (3300/3840)*width, (300/2160)*height))
        self.table.setRowCount(12)
        self.table.setColumnCount(32)
        self.table.setObjectName("filenameLabel")

        self.atributelabe = QtWidgets.QLabel(self.centralwidget)
        self.atributelabe.setGeometry(QtCore.QRect((315/3840)*width, (450/2160)*height, (350/3840)*width, (70/2160)*height))
        self.atributelabe.setObjectName("atributelabe")
        self.atributelabe.setText("Variables")
        self.atributelabe.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Typograf;}""")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect((40/3840)*width, (510/2160)*height, (700/3840)*width, (700/2160)*height))
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAlternatingRowColors(True)

        self.selectedlabel = QtWidgets.QLabel(self.centralwidget)
        self.selectedlabel.setGeometry(QtCore.QRect((980/3840)*width, (450/2160)*height, (350/3840)*width, (70/2160)*height))
        self.selectedlabel.setObjectName("selectedlabel")
        self.selectedlabel.setText("Selected Variables")
        self.selectedlabel.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Typograf;}""")


        self.listWidget2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget2.setGeometry(QtCore.QRect((760/3840)*width, (510/2160)*height, (700/3840)*width, (700/2160)*height))
        self.listWidget2.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.listWidget2.setObjectName("listWidget2")
        self.listWidget2.setAlternatingRowColors(True)

        

        self.scaling = QtWidgets.QPushButton(self.centralwidget)
        self.scaling.setGeometry(QtCore.QRect((1500/3840)*width, (520/2160)*height, (350/3840)*width, (50/2160)*height))
        self.scaling.setObjectName("scaling")
        self.scaling.setText("Standardization")

        self.norm = QtWidgets.QPushButton(self.centralwidget)
        self.norm.setGeometry(QtCore.QRect((1500/3840)*width, (590/2160)*height, (350/3840)*width, (50/2160)*height))
        self.norm.setObjectName("norm")
        self.norm.setText("MinMaxScaler")

        self.MaxAbs = QtWidgets.QPushButton(self.centralwidget)
        self.MaxAbs.setGeometry(QtCore.QRect((1500/3840)*width, (660/2160)*height, (350/3840)*width, (50/2160)*height))
        self.MaxAbs.setObjectName("MaxAbs")
        self.MaxAbs.setText("MaxAbsScaler")

        self.LabelEncoder1 = QtWidgets.QPushButton(self.centralwidget)
        self.LabelEncoder1.setGeometry(QtCore.QRect((1500/3840)*width, (730/2160)*height, (350/3840)*width, (50/2160)*height))
        self.LabelEncoder1.setObjectName("LabelEncoder")
        self.LabelEncoder1.setText("LabelEncoder")

        self.normalization = QtWidgets.QPushButton(self.centralwidget)
        self.normalization.setGeometry(QtCore.QRect((1500/3840)*width, (800/2160)*height, (350/3840)*width, (50/2160)*height))
        self.normalization.setObjectName("normalize")
        self.normalization.setText("Normalization")

        self.descrete = QtWidgets.QPushButton(self.centralwidget)
        self.descrete.setGeometry(QtCore.QRect((1500/3840)*width, (870/2160)*height, (350/3840)*width, (50/2160)*height))
        self.descrete.setObjectName("kbins")
        self.descrete.setText("K-bins discretization")

        self.binarization = QtWidgets.QPushButton(self.centralwidget)
        self.binarization.setGeometry(QtCore.QRect((1500/3840)*width, (940/2160)*height, (350/3840)*width, (50/2160)*height))
        self.binarization.setObjectName("binary")
        self.binarization.setText("Binarization")

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect((200/3840)*width, (1230/2160)*height, (350/3840)*width, (50/2160)*height))
        self.save.setObjectName("save")
        self.save.setText("Save File")


        self.perclm = QtWidgets.QPushButton(self.centralwidget)
        self.perclm.setGeometry(QtCore.QRect((2240/3840)*width, (600/2160)*height, (350/3840)*width, (50/2160)*height))
        self.perclm.setObjectName("perclm")
        self.perclm.setText("PerColumn")
        self.perclm.setEnabled(False)

        self.perrow = QtWidgets.QPushButton(self.centralwidget)
        self.perrow.setGeometry(QtCore.QRect((2240/3840)*width, (670/2160)*height, (350/3840)*width, (50/2160)*height))
        self.perrow.setObjectName("perrow")
        self.perrow.setText("PerRow")
        self.perrow.setEnabled(True)

        self.datainfo = QtWidgets.QLabel(self.centralwidget)
        self.datainfo.setGeometry(QtCore.QRect((2800/3840)*width, (450/2160)*height, (350/3840)*width, (70/2160)*height))
        self.datainfo.setObjectName("statisticlabel")
        self.datainfo.setText("Show Missing Values")
        self.datainfo.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Typograf;}""")

        self.infor = QtWidgets.QTextBrowser(self.centralwidget)
        self.infor.setGeometry(QtCore.QRect((2600/3840)*width, (510/2160)*height, (700/3840)*width, (700/2160)*height))
        self.infor.setObjectName("infor")
        self.infor.setStyleSheet(
        """QTextBrowser {
                           font: bold;
                           font-family: Courier;}""")

        

        self.HandleMissingVal = QtWidgets.QPushButton(self.centralwidget)
        self.HandleMissingVal.setGeometry(QtCore.QRect((1500/3840)*width, (1010/2160)*height, (350/3840)*width, (50/2160)*height))
        self.HandleMissingVal.setObjectName("HandleMissingVal")
        self.HandleMissingVal.setText("HandleMissingValues")

        self.Univariate_imputation = QtWidgets.QPushButton(self.centralwidget)
        self.Univariate_imputation.setGeometry(QtCore.QRect((1500/3840)*width, (1100/2160)*height, (400/3840)*width, (50/2160)*height))
        self.Univariate_imputation.setObjectName("Univariate_imputation")
        self.Univariate_imputation.setText("Univariate feature imputation")
        self.Univariate_imputation.hide()


        self.Multivariate_imputation  = QtWidgets.QPushButton(self.centralwidget)
        self.Multivariate_imputation.setGeometry(QtCore.QRect((1950/3840)*width, (1100/2160)*height, (400/3840)*width, (50/2160)*height))
        self.Multivariate_imputation.setObjectName("Multivariate")
        self.Multivariate_imputation.setText("KNNImputer")
        self.Multivariate_imputation.hide()

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect((1500/3840)*width, (1170/2160)*height, (200/3840)*width, (50/2160)*height))
        self.comboBox.hide()

        self.applybutton  = QtWidgets.QPushButton(self.centralwidget)
        self.applybutton.setGeometry(QtCore.QRect((1500/3840)*width, (1240/2160)*height, (350/3840)*width, (50/2160)*height))
        self.applybutton.setObjectName("apply")
        self.applybutton.setText("Apply Handler")
        self.applybutton.hide()

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect((5/3840)*width, (1300/2160)*height, (300/3840)*width, (50/2160)*height))
        self.back.setObjectName("back")
        self.back.setText("Back")
        self.back.setStyleSheet(
        """QPushButton {
                           
                             
border-radius:0;
border:0;

text-align:left;
padding-left:70px;
qproperty-icon:url('back.png');
qproperty-iconSize: 40px 40px;}""")
        


        self.menubar = QtWidgets.QMenuBar(PreProcessing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        PreProcessing.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PreProcessing)
        self.statusbar.setObjectName("statusbar")
        PreProcessing.setStatusBar(self.statusbar)

        self.retranslateUi(PreProcessing)
        QtCore.QMetaObject.connectSlotsByName(PreProcessing)

    def retranslateUi(self, PreProcessing):
        _translate = QtCore.QCoreApplication.translate
        PreProcessing.setWindowTitle(_translate("PreProcessing", "PreProcessing"))
        self.browseFile.setText(_translate("SmainWindow", "Open File"))
        self.browseFile.clicked.connect(self.pushButton_handler)
        self.filenameLabel.setText(_translate("SmainWindow", ""))
        self.listWidget.itemClicked.connect(self.listitemclick)
        self.LabelEncoder1.clicked.connect(self.applyencoder)
        self.scaling.clicked.connect(self.Standardize)
        self.norm.clicked.connect(self.MinMaxScaler)
        self.MaxAbs.clicked.connect(self.MaxAbsScale)
        self.normalization.clicked.connect(self.normalizate)
        self.descrete.clicked.connect(self.descretization)
        self.binarization.clicked.connect(self.binarize)
        self.save.clicked.connect(self.savefile)

        self.perclm.clicked.connect(self.num_missing)
        self.perrow.clicked.connect(self.row_missing)

        self.HandleMissingVal.clicked.connect(self.missingvalueButtons)

        self.Univariate_imputation.clicked.connect(self.univariate)
        self.Multivariate_imputation.clicked.connect(self.multivariate)

        self.applybutton.clicked.connect(self.applyhandling)

        self.comboBox.activated[str].connect(self.comboBox_click)
        self.back.clicked.connect(self.openmainwindow)



    

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(None, 'Open File', r"~/Desktop", '*.csv')
        self.path = filename[0]
        print(self.path)
        with open(self.path, "r") as fpath:
            self.infor.clear()
            self.filenameLabel.setText(str(self.path))
            self.filenameLabel.adjustSize()
            pandas.set_option('display.max_rows', None)
            self.dataset=pandas.read_csv(fpath)
            buf = io.StringIO()
            self.dataset.info(verbose=True, null_counts=True,buf=buf)

            self.infor.append(str(self.dataset.apply(self.missing, axis=0)))

            self.table.setColumnCount(len(self.dataset.columns))
            heads=self.dataset.head(10).to_numpy()
            self.table.clear()
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))
            self.datasetheaders=[]
            self.x = []
            self.listWidget2.clear()
            self.datasetheaders=self.dataset.columns.to_numpy()
            self.listWidget.clear()
          
            for i in range(len(self.datasetheaders)):
                self.listWidget.insertItem(i,self.datasetheaders[i])


      


    def univariate(self):
        self.comboBox.clear()
        self.comboBox.show()
        self.applybutton.show()
        print("yes")
        self.strategyoption='mean'
        strategy_array=['mean','most_frequent','median']
        for i in range(len(strategy_array)):
            self.comboBox.addItem(strategy_array[i])

    def openmainwindow(self):
        try:
            self.window=QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            PreProcessing.hide()
            self.window.show()
        except Exception as e:
            print(repr(e))
                       
                



    def multivariate(self):
        try:
            for i in range(len(self.x)):
                imp = KNNImputer(n_neighbors=2, weights="uniform")
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                x_scaled =imp.fit_transform(temp)
                self.dataset[self.x[i]] = x_scaled


            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))

            self.infor.clear()
            self.infor.append(str(self.dataset.apply(self.missing, axis=0)))
            self.perclm.setEnabled(False)
            self.perrow.setDisabled(False)        

            self.comboBox.hide()  
            self.applybutton.hide() 
            self.Univariate_imputation.hide()
            self.Multivariate_imputation.hide()    

        except Exception as e:
            print(repr(e))            
                




    
    

    def comboBox_click(self,text):
           self.strategyoption=text
              

    def applyhandling(self):
        try:
            for i in range(len(self.x)):
                imp = SimpleImputer(strategy=self.strategyoption)
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                x_scaled =imp.fit_transform(temp)
                self.dataset[self.x[i]] = x_scaled


            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))

            self.infor.clear()
            self.infor.append(str(self.dataset.apply(self.missing, axis=0)))
            self.perclm.setEnabled(False)
            self.perrow.setDisabled(False)        

            self.comboBox.hide()  
            self.applybutton.hide() 
            self.Univariate_imputation.hide()
            self.Multivariate_imputation.hide()    

        except Exception as e:
            print(repr(e))            
                
                
    def row_missing(self):
        self.perrow.setEnabled(False)
        self.perclm.setDisabled(False)
        
        self.infor.clear()
       
        #self.infor.append(str(self.dataset.apply(lambda x: sum(x.isnull()))))
        self.infor.append(str(self.dataset.apply(self.missing, axis=1)))

        
    def num_missing(self):
        self.perclm.setEnabled(False)
        self.perrow.setDisabled(False)
        
        self.infor.clear()
        #self.infor.append(str(self.dataset.apply(lambda x: sum(x.isnull()))))
        self.infor.append(str(self.dataset.apply(self.missing, axis=0)))
         
    def missing(self,x):
        return sum(x.isnull())         

    def listitemclick(self):

        items = self.listWidget.selectedItems()
        self.x = []
        self.listWidget2.clear()
        for i in range(len(items)):
            self.x.append(str(self.listWidget.selectedItems()[i].text()))

        print (self.x)
        for i in range(len(self.x)):
                self.listWidget2.insertItem(i,self.x[i])
                
    def applyencoder(self):
        
        try:
            for i in range(len(self.x)):
                label_encoder = preprocessing.LabelEncoder()
                print(self.x[i])
                self.dataset[self.x[i]]= label_encoder.fit_transform(self.dataset[self.x[i]]) 
                print("done"+str(self.x[i]))
            
    
        
            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                     self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))
  
        except Exception as e:
            print(repr(e))
                
    def Standardize(self):
        try:
            for i in range(len(self.x)):
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                x_scaled = preprocessing.scale(temp)
                self.dataset[self.x[i]] = x_scaled


            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))

        except Exception as e:
            print(repr(e))            

    def MinMaxScaler(self):
        try:
            for i in range(len(self.x)):
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                min_max_scaler = preprocessing.MinMaxScaler()
                x_scaled = min_max_scaler.fit_transform(temp)
                self.dataset[self.x[i]] = x_scaled
                
            
    
        
            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                     self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))
  
        except Exception as e:
            print(repr(e))



        '''min_max_scaler = preprocessing.MinMaxScaler()
                                X_train_minmax = min_max_scaler.fit_transform(self.dataset)
                                df = pandas.DataFrame(data=X_train_minmax)
                                self.dataset=df
                        
                                heads=self.dataset.head().to_numpy()
                                
                                for i in range(5):
                                    for j in range(len(self.dataset.columns)):
                                        self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))'''

    def MaxAbsScale(self):
        try:
            for i in range(len(self.x)):
                max_abs_scaler = preprocessing.MaxAbsScaler()
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                x_scaled = max_abs_scaler.fit_transform(temp)
                self.dataset[self.x[i]] = x_scaled


            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))

        except Exception as e:
             print(repr(e)) 
            

    def normalizate(self):
        try:
            for i in range(len(self.x)):
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                x_scaled = preprocessing.normalize(temp)
                self.dataset[self.x[i]] = x_scaled


            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))

        except Exception as e:
            print(repr(e)) 

    def descretization(self):
        try:
            for i in range(len(self.x)):
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                est  = preprocessing.KBinsDiscretizer(n_bins=5, encode='ordinal',strategy='uniform')
                est.fit(temp)
                x_scaled=est.transform(temp)
                print(x_scaled)
                self.dataset[self.x[i]] = x_scaled


            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))

        except Exception as e:
            print(repr(e))  


    def binarize(self):
        try:
            for i in range(len(self.x)):
                temp = self.dataset[self.x[i]].values.reshape(-1, 1)
                binarizer = preprocessing.Binarizer()
                x_scaled=binarizer.transform(temp)
                print(x_scaled)
                self.dataset[self.x[i]] = x_scaled


            heads=self.dataset.head(10).to_numpy()
        
            for i in range(10):
                for j in range(len(self.dataset.columns)):
                    self.table.setItem(i,j, QTableWidgetItem(str(heads[i][j])))

        except Exception as e:
            print(repr(e))  


    def missingvalueButtons(self):
        self.Univariate_imputation.show()
        self.Multivariate_imputation.show()
                                              

    def savefile(self):
        try:
            h=self.path[-4]+"1.csv"
            self.dataset.to_csv(self.path)
            print(h)
        except Exception as e:
            print(repr(e))
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PreProcessing = QtWidgets.QMainWindow()
    ui = Ui_PreProcessing()
    ui.setupUi(PreProcessing)
    PreProcessing.show()
    sys.exit(app.exec_())
    dataset='temp'
    datasetheaders=[]
    strategyoption='temp'
    x = []
    path="temp"
    
    
