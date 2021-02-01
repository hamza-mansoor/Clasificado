import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QListWidget, QSizePolicy,QVBoxLayout,QDesktopWidget
from PyQt5.QtGui import QIcon
import pandas
from matplotlib.backends.qt_compat import QtWidgets
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
from sklearn.preprocessing import LabelEncoder
import numpy as np
from scipy import stats
from glob import iglob
import io
import csv
from pandas_profiling import ProfileReport





class Ui_SmainWindow(object):
   
    def setupUi(self, SmainWindow): 
        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()
        '''screen_resolution = app.desktop().screenGeometry()
                                width, height = screen_resolution.width(), screen_resolution.height()'''
        SmainWindow.setObjectName("SmainWindow")
        SmainWindow.resize((3400/3840)*width,(1700/2160)*height)
        SmainWindow.setMaximumSize(QtCore.QSize((3400/3840)*width,(1700/2160)*height))
        SmainWindow.setMinimumSize(QtCore.QSize((3400/3840)*width,(1700/2160)*height))
        self.centralwidget = QtWidgets.QWidget(SmainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect((20/3840)*width, (1070/2160)*height ,(3300/3840)*width, (30/2160)*height))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setObjectName("line")

        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect((1440/3840)*width, (290/2160)*height ,(30/3840)*width, (700/2160)*height))
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setLineWidth(5)
        self.line2.setObjectName("line2")

        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect((2290/3840)*width, (290/2160)*height ,(30/3840)*width, (700/2160)*height))
        self.line3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setLineWidth(5)
        self.line3.setObjectName("line3")
       

        self.layout = QVBoxLayout(self.centralwidget)
        self.fig = Figure(figsize=((8/3840)*width, (6.5/2160)*height ))
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

        self.widget = QWidget(self.centralwidget)
        #self.toolbar = NavigationToolbar(self.canvas, self.widget)
        self.layout.setMenuBar(NavigationToolbar(self.canvas,self.widget))
        self.widget.setLayout(self.layout)
        self.widget.setGeometry((1480/3840)*width,(290/2160)*height,(800/3840)*width,(600/2160)*height)
        
        
        
        
        
        #layout.addWidget(self.canvas)
        '''
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(700, 150, 700, 700))
        self.graphicsView.setObjectName("graphicsView")
        '''
        self.chartView = QChartView(self.centralwidget)
        self.chartView.setGeometry(QtCore.QRect((200/3840)*width, (1090/2160)*height, (1700/3840)*width, (500/2160)*height))
        self.chartView.setObjectName("graphicsView")


        self.browseFile = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile.setGeometry(QtCore.QRect((200/3840)*width, (50/2160)*height, (350/3840)*width, (50/2160)*height))
        self.browseFile.setObjectName("browseFile")


        self.filenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.filenameLabel.setGeometry(QtCore.QRect((700/3840)*width, (55/2160)*height, (350/3840)*width, (70/2160)*height))
        self.filenameLabel.setObjectName("filenameLabel")

        self.datasize = QtWidgets.QLabel(self.centralwidget)
        self.datasize.setGeometry(QtCore.QRect((20/3840)*width, (105/2160)*height, (350/3840)*width, (70/2160)*height))
        self.datasize.setObjectName("datasize")
        self.datasize.setText("Data Shape :")
        self.datasize.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Typograf;}""")

        self.datashape = QtWidgets.QLabel(self.centralwidget)
        self.datashape.setGeometry(QtCore.QRect((250/3840)*width, (105/2160)*height, (350/3840)*width, (70/2160)*height))
        self.datashape.setObjectName("datashape")
        self.datashape.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 12pt;
                           font-family: Typograf;}""")

        self.atributelabe = QtWidgets.QLabel(self.centralwidget)
        self.atributelabe.setGeometry(QtCore.QRect((295/3840)*width, (200/2160)*height, (350/3840)*width, (70/2160)*height))
        self.atributelabe.setObjectName("atributelabe")
        self.atributelabe.setText("Variables")
        self.atributelabe.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Typograf;}""")

        self.statisticlabel = QtWidgets.QLabel(self.centralwidget)
        self.statisticlabel.setGeometry(QtCore.QRect((1020/3840)*width, (200/2160)*height, (350/3840)*width, (70/2160)*height))
        self.statisticlabel.setObjectName("statisticlabel")
        self.statisticlabel.setText("Statistics")
        self.statisticlabel.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Typograf;}""")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect((740/3840)*width, (290/2160)*height, (700/3840)*width, (700/2160)*height))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet(
        """QTextBrowser {
                           font: bold;
                           font-size: 12pt;
                           font-family: Courier;}""")

        self.missingvalulabel = QtWidgets.QLabel(self.centralwidget)
        self.missingvalulabel.setGeometry(QtCore.QRect((2330/3840)*width, (500/2160)*height, (250/3840)*width, (100/2160)*height))
        self.missingvalulabel.setObjectName("missingvalulabel")
        self.missingvalulabel.setText("Show Missing \nValues")
        self.missingvalulabel.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Courier;}""")
        
        self.resetbtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetbtn.setGeometry(QtCore.QRect((2330/3840)*width, (300/2160)*height, (250/3840)*width, (50/2160)*height))
        self.resetbtn.setObjectName("resetbtn")
        self.resetbtn.setText("Reset")
        self.resetbtn.setEnabled(False)

        self.perclm = QtWidgets.QPushButton(self.centralwidget)
        self.perclm.setGeometry(QtCore.QRect((2330/3840)*width, (600/2160)*height, (250/3840)*width, (50/2160)*height))
        self.perclm.setObjectName("perclm")
        self.perclm.setText("PerColumn")
        self.perclm.setEnabled(False)

        self.perrow = QtWidgets.QPushButton(self.centralwidget)
        self.perrow.setGeometry(QtCore.QRect((2330/3840)*width, (670/2160)*height, (250/3840)*width, (50/2160)*height))
        self.perrow.setObjectName("perrow")
        self.perrow.setText("PerRow")
        self.perrow.setEnabled(False)

        self.datainfo = QtWidgets.QLabel(self.centralwidget)
        self.datainfo.setGeometry(QtCore.QRect((2850/3840)*width, (200/2160)*height, (350/3840)*width, (70/2160)*height))
        self.datainfo.setObjectName("statisticlabel")
        self.datainfo.setText("Data Info")
        self.datainfo.setStyleSheet(
        """QLabel {
                           font: bold;
                           font-size: 10pt;
                           font-family: Typograf;}""")
        
        self.infor = QtWidgets.QTextBrowser(self.centralwidget)
        self.infor.setGeometry(QtCore.QRect((2600/3840)*width, (290/2160)*height, (700/3840)*width, (700/2160)*height))
        self.infor.setObjectName("infor")
        self.infor.setStyleSheet(
        """QTextBrowser {
                           font: bold;
                           font-family: Courier;}""")

       
       
        self.calstatistics = QtWidgets.QPushButton(self.centralwidget)
        self.calstatistics.setGeometry(QtCore.QRect((200/3840)*width, (1020/2160)*height, (350/3840)*width, (50/2160)*height))
        self.calstatistics.setObjectName("calstatistics")
        

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect((20/3840)*width, (290/2160)*height, (700/3840)*width, (700/2160)*height))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAlternatingRowColors(True)
       


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect((1480/3840)*width,(120/2160)*height,(800/3840)*width,(50/2160)*height))
        self.comboBox.setObjectName("comboBox")

        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect((1480/3840)*width,(200/2160)*height,(800/3840)*width,(50/2160)*height))
        self.comboBox2.setObjectName("comboBox2")

        self.report = QtWidgets.QPushButton(self.centralwidget)
        self.report.setGeometry(QtCore.QRect((1700/3840)*width, (1020/2160)*height, (300/3840)*width, (50/2160)*height))
        self.report.setObjectName("report")
        self.report.setText("Generate Report")



        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect((5/3840)*width, (1600/2160)*height, (300/3840)*width, (50/2160)*height))
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






        SmainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SmainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, (469/3840)*width, (22/2160)*height))
        self.menubar.setObjectName("menubar")
        SmainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SmainWindow)
        self.statusbar.setObjectName("statusbar")
        SmainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SmainWindow)
        QtCore.QMetaObject.connectSlotsByName(SmainWindow)

        




    def retranslateUi(self, SmainWindow):
        _translate = QtCore.QCoreApplication.translate
        SmainWindow.setWindowTitle(_translate("SmainWindow", "Data Statistical Analysis"))
        self.browseFile.setText(_translate("SmainWindow", "Open File"))
        self.browseFile.clicked.connect(self.pushButton_handler)
        self.filenameLabel.setText(_translate("SmainWindow", ""))
        self.calstatistics.setText(_translate("SmainWindow", "Calculate Statistics"))
        self.calstatistics.clicked.connect(self.cal)
        self.listWidget.clicked.connect(self.listview_clicked)

        self.resetbtn.clicked.connect(self.information)
        self.perclm.clicked.connect(self.num_missing)
        self.perrow.clicked.connect(self.row_missing)
        self.report.clicked.connect(self.generatereport)


            
        
        

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(None, 'Open File', r"~/Desktop", '*.csv')
        path = filename[0]

        with open(path, "r") as fpath:
            self.infor.clear()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.datasetheaders=[]
            self.filenameLabel.setText(str(path))
            self.filenameLabel.adjustSize()
            pandas.set_option('display.max_rows', None)
            self.dataset=pandas.read_csv(fpath)
            buf = io.StringIO()
            self.dataset.info(verbose=True, null_counts=True,buf=buf)
            s = buf.getvalue()
            self.perclm.setDisabled(False)
            self.perrow.setDisabled(False)

            self.infor.append(s)
            SIZE=self.dataset.shape
            self.datashape.setText(str(SIZE))
            self.create_piechart()
            #headers=self.dataset.columns
            self.datasetheaders=self.dataset.columns.to_numpy()
            self.listWidget.clear()
          
            for i in range(len(self.datasetheaders)-1):
                self.listWidget.insertItem(i,self.datasetheaders[i])

            for i in range(len(self.datasetheaders)-1):
                self.comboBox.addItem(self.datasetheaders[i])

            for i in range(len(self.datasetheaders)-1):
                self.comboBox2.addItem(self.datasetheaders[i])    
                
           

            self.setup()

            self.comboBox.currentIndexChanged.connect(self.setup)
            self.comboBox2.currentIndexChanged.connect(self.setup)

            #print(unique_headers)

            '''print ("Missing values per column:")
                                                print(self.dataset.apply(lambda x: sum(x.isnull()))) 
                                    '''


    def generatereport(self):
        try:
            profile = ProfileReport(self.dataset)
            profile.to_file(output_file="AnalysisReport.html")
            print("yes")
        except Exception as e:
            print(repr(e))

        
    def information(self):
        self.infor.clear()
        self.resetbtn.setEnabled(False)
        self.perrow.setDisabled(False)
        self.perclm.setDisabled(False)
        buf = io.StringIO()
        self.dataset.info(verbose=True, null_counts=True,buf=buf)
        s = buf.getvalue()

        self.infor.append(s)

      
            

            
        



    def row_missing(self):
        self.perrow.setEnabled(False)
        self.perclm.setDisabled(False)
        self.resetbtn.setDisabled(False)
        self.infor.clear()
       
        #self.infor.append(str(self.dataset.apply(lambda x: sum(x.isnull()))))
        self.infor.append(str(self.dataset.apply(self.missing, axis=1)))

        
    def num_missing(self):
        self.perclm.setEnabled(False)
        self.perrow.setDisabled(False)
        self.resetbtn.setDisabled(False)
        self.infor.clear()
        #self.infor.append(str(self.dataset.apply(lambda x: sum(x.isnull()))))
        self.infor.append(str(self.dataset.apply(self.missing, axis=0)))
         
    def missing(self,x):
        return sum(x.isnull())




         
 
    def setup(self):
        try:
            print("fig")
            iris=self.dataset 
        
       


            x_index = 0
            y_index = 1
            w=iris.iloc[:,self.comboBox.currentIndex()]
            z=iris.iloc[:,self.comboBox2.currentIndex()]

            y=iris.iloc[:,-1].values

            # this formatter will label the colorbar with the correct target names
            #formatter = plt.FuncFormatter(y)

            #plt.figure(figsize=(5, 4))
        
            ax = self.fig.add_subplot(111)
            ax.clear()
            scatter=ax.scatter(w, z, c=y)
        
            #self.figure.colorbar(ticks=y)

            #ax.xlabel("iris.feature_names[x_index]")
            #ax.ylabel("iris.feature_names[y_index]")
            ax.set_xlabel(self.comboBox.currentText(),  fontsize=25) 
            ax.set_ylabel(self.comboBox2.currentText(), fontsize=25)
            ax.set_title('Scatter Plot',fontsize=25)

            legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
            ax.add_artist(legend1)

            self.widget.adjustSize()
        

            print("fig123456789")

        except Exception as e:
            print(repr(e)) 
               

        
        

        


    def cal(self):
        #self.graphicsView.clear()
        z=self.dataset
        w=z.iloc[:,self.a]
     
        self.textBrowser.setText("Mean:\n"+str(np.mean(w))+"\nMedian:\n"+str(np.median(w))+"\nMode:\n"+str(stats.mode(w))+"\nvariance:\n"+str(np.var(w))+"\nStdev:\n"+str(np.std(w)))
        #self.textBrowser.adjustSize()
        '''
        pen = pg.mkPen(color=(255, 0, 0),width=8)
        self.graphicsView.setBackground('w')
        self.graphicsView.plot(w,symbol='+',symbolSize=30, pen=pen)
        '''
       


    def listview_clicked(self):
        item=self.listWidget.currentRow()
        self.a=item

    def create_piechart(self):
       
        z=self.dataset
        w=z.iloc[:,-1]
        r=w.value_counts()
        p=r.to_numpy()
        y=w.nunique()
       
      
        df_val_counts = pandas.DataFrame(r)
        df_val_counts = df_val_counts.reset_index()
        df_val_counts.columns = ['unique_values', 'counts']
        
        w=df_val_counts.iloc[:,0].to_numpy()
        k=df_val_counts.iloc[:,1].to_numpy()
        res = w.astype(str)
       
        series = QPieSeries()
        for i in range(y):
            series.append(res[i], k[i])
        

        
        
        chart = self.chartView.chart()
        chart.removeAllSeries()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        
        chart.setAnimationOptions(QChart.AllAnimations)
        chart.setTitle("Pie Chart")
        
        
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
      
        #self.chartView = QChartView(chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        
        
        
        #self.setCentralWidget(chartview)    
      
        
              
            


if __name__ == "__main__":
    import sys
    dataset="temp"
    datasetheaders=[]
    a=0;
    app = QtWidgets.QApplication(sys.argv)
    
    SmainWindow = QtWidgets.QMainWindow()
    ui = Ui_SmainWindow()
    ui.setupUi(SmainWindow)
    SmainWindow.show()
    sys.exit(app.exec_())
