import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import pandas
import sklearn
from sklearn.ensemble import *
from sklearn.linear_model import *
from sklearn.naive_bayes import *
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from glob import iglob
from libsvm import *
import time
import csv
from sklearn.metrics import accuracy_score
import numpy as np
     
      

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()
        '''screen_resolution = app.desktop().screenGeometry()
                                width, height = screen_resolution.width(), screen_resolution.height()'''
        width_per=(0.5)*width
        height_per=(0.5)*height
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width_per, height_per)
        MainWindow.setMaximumSize(QtCore.QSize(width_per, height_per))
        MainWindow.setMinimumSize(QtCore.QSize(width_per, height_per))
       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect((200/3840)*width, (50/2160)*height, (350/3840)*width, (50/2160)*height))
        self.openfile.setObjectName("openfile")

        self.filename = QtWidgets.QLabel(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect((700/3840)*width, (55/2160)*height, (350/3840)*width, (70/2160)*height))
        self.filename.setObjectName("filename")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect((220/3840)*width, (95/2160)*height, (350/3840)*width, (70/2160)*height))
        self.label.setObjectName("label")
        

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect((1370/3840)*width, (95/2160)*height, (350/3840)*width, (70/2160)*height))
        self.label_2.setObjectName("label_2")

        self.classifiers = QtWidgets.QListWidget(self.centralwidget)
        self.classifiers.setGeometry(QtCore.QRect((20/3840)*width, (150/2160)*height, (600/3840)*width, (700/2160)*height))
        self.classifiers.setObjectName("classifiers")

        self.modificationlabel = QtWidgets.QLabel(self.centralwidget)
        self.modificationlabel.setGeometry(QtCore.QRect((630/3840)*width, (160/2160)*height, (350/3840)*width, (150/2160)*height))
        self.modificationlabel.setObjectName("label_2")
        self.modificationlabel.hide()

        self.modify_label1 = QtWidgets.QLabel(self.centralwidget)
        self.modify_label1.setGeometry(QtCore.QRect((630/3840)*width, (320/2160)*height, (350/3840)*width, (100/2160)*height))
        self.modify_label1.setObjectName("modify_label1")
        self.modify_label1.hide()

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect((630/3840)*width, (440/2160)*height, (200/3840)*width, (50/2160)*height))
        self.comboBox.hide()

        self.modify_label2 = QtWidgets.QLabel(self.centralwidget)
        self.modify_label2.setGeometry(QtCore.QRect((630/3840)*width, (510/2160)*height, (350/3840)*width, (100/2160)*height))
        self.modify_label2.setObjectName("modify_label2")
        self.modify_label2.hide()


        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect((630/3840)*width, (630/2160)*height, (200/3840)*width, (50/2160)*height))
        self.comboBox2.hide()

        self.modify_label3 = QtWidgets.QLabel(self.centralwidget)
        self.modify_label3.setGeometry(QtCore.QRect((630/3840)*width, (700/2160)*height, (350/3840)*width, (100/2160)*height))
        self.modify_label3.setObjectName("modify_label3")
        self.modify_label3.hide()

        self.comboBox3 = QtWidgets.QSpinBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect((630/3840)*width, (820/2160)*height, (200/3840)*width, (50/2160)*height))
        self.comboBox3.setRange(1, 100)
        self.comboBox3.setSingleStep(1)
        self.comboBox3.hide()


        self.printResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.printResult.setGeometry(QtCore.QRect((1000/3840)*width, (150/2160)*height, (900/3840)*width, (700/2160)*height))
        self.printResult.setObjectName("printResult")

        self.calresult = QtWidgets.QPushButton(self.centralwidget)
        self.calresult.setGeometry(QtCore.QRect((1300/3840)*width, (870/2160)*height, (400/3840)*width, (50/2160)*height))
        self.calresult.setObjectName("calresult")

        self.compare = QtWidgets.QPushButton(self.centralwidget)
        self.compare.setGeometry(QtCore.QRect((1300/3840)*width, (970/2160)*height, (400/3840)*width, (50/2160)*height))
        self.compare.setObjectName("compare")
        self.compare.setText('Compare Algorithms')

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect((40/3840)*width, (870/2160)*height, (200/3840)*width, (50/2160)*height))
        self.label_3.setObjectName("label_3")

        self.select_test_range = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.select_test_range.setGeometry(QtCore.QRect((250/3840)*width, (870/2160)*height, (200/3840)*width, (50/2160)*height))
        self.select_test_range.setRange(0.2, 0.8)
        self.select_test_range.setSingleStep(0.2)
        self.select_test_range.setObjectName("select_test_range")

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect((5/3840)*width, (980/2160)*height, (300/3840)*width, (50/2160)*height))
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




        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Classification"))

        self.calresult.setText(_translate("MainWindow", "Calculate Result"))
      
        self.calresult.clicked.connect(self.cal)

        self.label.setText(_translate("MainWindow", "Classifiers"))
        self.label_2.setText(_translate("MainWindow", "Output Result"))
        self.label_3.setText(_translate("MainWindow", "Select Test Size"))
        

        self.compare.clicked.connect(self.comparing)
        self.openfile.setText(_translate("MainWindow", "Open File"))
       
        self.openfile.clicked.connect(self.pushButton_handler)

        self.printResult.setStyleSheet(
        """QTextBrowser {
                           font: bold;
                           font-size: 12pt;
                           font-family: Courier;}""")

        
        self.classifiers.setAlternatingRowColors(True)
        self.classifiers.setStyleSheet(
        """QListWidget {
                           
                           font-size: 10pt;
                           font-family: Typograf;}""")

        l1_childs=["DecisionTree","RandomForest","Support Vector Machine","BernoulliNB","ComplementNB","GaussianNB","MultinomialNB","LogisticRegression","KNeighborsClassifier","Multi-layer Perceptron",
        "ExtraTreeClassifier","AdaBoost","Bagging","GradientBoostingClassifier","VotingClassifier"]
        #self.classifiers.setAlternatingRowColors(True)
        print(len(l1_childs))
        for i in range(len(l1_childs)):
            self.classifiers.insertItem(i,l1_childs[i])
            
        
        self.classifiers.clicked.connect(self.listview_clicked)

        

    def pushButton_handler(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(None, 'Open File', r"~/Desktop", '*.csv')
        path = filename[0]

        with open(path, "r") as fpath:
            self.filename.setText(str(path))
            self.filename.adjustSize()
            self.dataset=pandas.read_csv(fpath)
            
           
        
    def comparing(self):
        self.printResult.clear()
        x=self.dataset.iloc[:,:-1].values
        y=self.dataset.iloc[:,-1].values
        self.test_rang=float(self.select_test_range.value())
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=self.test_rang)

        try:
            
            
            model=tree.DecisionTreeClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Daccuracy = accuracy_score(y_test, result)
            

            
           
            model=RandomForestClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Raccuracy = accuracy_score(y_test, result)
            


           
           
            model=BaggingClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Baccuracy = accuracy_score(y_test, result)
            


            
           
            model=AdaBoostClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Aaccuracy = accuracy_score(y_test, result)
            


            
          
            model=LogisticRegression()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Laccuracy = accuracy_score(y_test, result)
            


            
           
            model=svm.SVC(kernel='linear')
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Saccuracy = accuracy_score(y_test, result)
            


           
           
            model=GaussianNB()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Gaccuracy = accuracy_score(y_test, result)
            


            
           
            model=KNeighborsClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            end1 = time.time()
            Kaccuracy = accuracy_score(y_test, result)
           


            
            
            model=MLPClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Maccuracy = accuracy_score(y_test, result)
            


            
            
            model=ExtraTreesClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Eaccuracy = accuracy_score(y_test, result)
            


            
            
            model=GradientBoostingClassifier()
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Caccuracy = accuracy_score(y_test, result)
            


           
            
            model=VotingClassifier([('lsvc', svm.LinearSVC()),
                                              ('knn', neighbors.KNeighborsClassifier()),
                                              ('rfor', RandomForestClassifier())])
            model.fit(x_train,y_train)
            result=model.predict(x_test)
            Vaccuracy = accuracy_score(y_test, result)
            


            self.printResult.setText("DecisionTreeClassifier\n"+"accuracy  "+str(Daccuracy)+"\n\n"+"RandomForest\n"+"accuracy  "+str(Raccuracy)+"\n\n"+"Bagging\n"+"accuracy  "+str(Baccuracy)+"\n\n"+"AdaBoost\n"+"accuracy  "+str(Aaccuracy)+"\n\n"+"LogisticRegression\n"+"accuracy  "+str(Laccuracy)+"\n\n"+ "svm.SVC\n"+"accuracy  "+str(Saccuracy)+"\n\n"+"GaussianNB\n"+"accuracy  "+str(Gaccuracy)+"\n\n"+"KNeighborsClassifier\n"+"accuracy  "+str(Kaccuracy)+"\n\n"+"MLPClassifier\n"+"accuracy  "+str(Maccuracy)+"\n\n"+"ExtraTreesClassifier\n"+"accuracy  "+str(Eaccuracy)+"\n\n"+"GradientBoostingClassifier\n"+"accuracy  "+str(Caccuracy)+"\n\n"+"VotingClassifier\n"+"accuracy  "+str(Vaccuracy)+"\n\n")
        except Exception as e:
            print(repr(e))


    def listview_clicked(self):
       
        item=self.classifiers.currentItem()
        self.a=str(item.text())

        if(self.a=="LogisticRegression"):
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.show()
            self.modify_label2.show()
            self.modify_label1.setText("Select\nSolver")
            self.modify_label2.setText("Select\nMulti_class Option")
            self.solver_option="newton-cg"
            self.multiclass_option="auto"
            self.comboBox.show()
            self.comboBox2.show()
            self.comboBox3.hide()
            self.modify_label3.hide()
            self.modificationlabel.setText("Modify\n"+self.a)
            solvers_array=['newton-cg','lbfgs','liblinear','sag','saga']
            multiclass_array=['auto','ovr']
            
            for i in range(len(solvers_array)):
                self.comboBox.addItem(solvers_array[i])
            for i in range(len(multiclass_array)):
                self.comboBox2.addItem(multiclass_array[i])

        elif(self.a=="RandomForest"):
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.show()
            self.modify_label2.show()
            self.modify_label3.show()
            self.modify_label1.setText("Select\nbootstrap")
            self.modify_label2.setText("Select\nmax_features")
            self.modify_label3.setText("Select\nn_estimators")
            self.bootstrip_option="True"
            self.max_features_option="auto"
            self.n_estimators_option=10
            self.comboBox.show()
            self.comboBox2.show()
            self.comboBox3.show()
            self.modificationlabel.setText("Modify\n"+self.a)
            max_features_option_array=['auto','sqrt','log2']
            bootstrip_option_array=['True','False']
            for i in range(len(bootstrip_option_array)):
                self.comboBox.addItem(bootstrip_option_array[i])
            for i in range(len(max_features_option_array)):
                self.comboBox2.addItem(max_features_option_array[i])

        elif(self.a=="DecisionTree"):
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.show()
            self.modify_label2.show()
            
            self.modify_label1.setText("Select\ncriterion")
            self.modify_label2.setText("Select\nmax_features")
            
            self.criterion_option="gini"
            self.max_features_option="auto"
            
            self.comboBox.show()
            self.comboBox2.show()
            self.comboBox3.hide()
            self.modify_label3.hide()
            self.modificationlabel.setText("Modify\n"+self.a)
            max_features_option_array=['auto','sqrt','log2']
            criterion_array=['gini','entropy']
            for i in range(len(criterion_array)):
                self.comboBox.addItem(criterion_array[i])
            for i in range(len(max_features_option_array)):
                self.comboBox2.addItem(max_features_option_array[i])  

        elif(self.a=="Support Vector Machine"):
            try:
                self.modificationlabel.show()
                self.comboBox.clear()
                self.comboBox2.clear()
                self.modify_label1.show()
                self.modify_label2.show()
            
                self.modify_label1.setText("Select\nkernel")
                self.modify_label2.setText("Select\ngamma")
            
                self.kernal_option="rbf"
                self.gamma_option="auto"
            
                self.comboBox.show()
                self.comboBox2.show()
                self.comboBox3.hide()
                self.modify_label3.hide()
                self.modificationlabel.setText("Modify\n"+self.a)
                kernal_option_array=['rbf','linear','poly','sigmoid']
                gamma_option_array=['auto','scale']
                for i in range(len(kernal_option_array)):
                    self.comboBox.addItem(kernal_option_array[i])
                    
                for i in range(len(gamma_option_array)):
                    self.comboBox2.addItem(gamma_option_array[i]) 
            except Exception as e:
                print(repr(e)) 
                   
                
        
        elif self.a=="BernoulliNB":
            self.modificationlabel.hide()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.hide()
            self.modify_label2.hide()
            self.modify_label3.hide()
            self.comboBox.hide()
            self.comboBox2.hide()
            self.comboBox3.hide()

        elif self.a=="ComplementNB":
            self.modificationlabel.hide()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.hide()
            self.modify_label2.hide()
            self.modify_label3.hide()
            self.comboBox.hide()
            self.comboBox2.hide()
            self.comboBox3.hide()
            
        elif self.a=="GaussianNB":
            self.modificationlabel.hide()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.hide()
            self.modify_label2.hide()
            self.modify_label3.hide()
            self.comboBox.hide()
            self.comboBox2.hide()
            self.comboBox3.hide()
            
        elif self.a=="MultinomialNB":
            self.modificationlabel.hide()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.hide()
            self.modify_label2.hide()
            self.modify_label3.hide()
            self.comboBox.hide()
            self.comboBox2.hide()
            self.comboBox3.hide()     

        elif(self.a=="KNeighborsClassifier"):
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.show()
            self.modify_label2.show()
            self.modify_label3.show()
            self.modify_label1.setText("Select\nalgorithm")
            self.modify_label2.setText("Select\nweights")
            self.modify_label3.setText("Select\nn_neighbors")
            self.algorithm_option="auto"
            self.weights_option="uniform"
            self.comboBox.show()
            self.comboBox2.show()
            self.comboBox3.show()
            self.modificationlabel.setText("Modify\n"+self.a)
            algorithm_option_option_array=['auto','ball_tree','kd_tree','brute']
            weights_option_array=['uniform','distance']
            for i in range(len(algorithm_option_option_array)):
                self.comboBox.addItem(algorithm_option_option_array[i])
            for i in range(len(weights_option_array)):
                self.comboBox2.addItem(weights_option_array[i])    

        elif self.a=="ExtraTreeClassifier":
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.show()
            self.modify_label2.show()
            
            self.modify_label1.setText("Select\ncriterion")
            self.modify_label2.setText("Select\nmax_features")
            self.modify_label3.setText("Select\nn_estimators")
            self.criterion_option="gini"
            self.max_features_option="auto"
            
            self.comboBox.show()
            self.comboBox2.show()
            self.comboBox3.show()
            self.modify_label3.show()
            self.modificationlabel.setText("Modify\n"+self.a)
            max_features_option_array=['auto','sqrt','log2']
            criterion_array=['gini','entropy']
            for i in range(len(criterion_array)):
                self.comboBox.addItem(criterion_array[i])
            for i in range(len(max_features_option_array)):
                self.comboBox2.addItem(max_features_option_array[i]) 

        elif self.a=="GradientBoostingClassifier":
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.hide()
            self.modify_label2.show()
            
            
            self.modify_label2.setText("Select\n loss")
            self.modify_label3.setText("Select\nn_estimators")
            self.lose_option="deviance"
            #self.max_features_option="auto"
            
            self.comboBox.hide()
            self.comboBox2.show()
            self.comboBox3.show()
            self.modify_label3.show()
            self.modificationlabel.setText("Modify\n"+self.a)
            lose_option_array=['deviance','exponential']
            
            for i in range(len(lose_option_array)):
                self.comboBox2.addItem(lose_option_array[i])

        elif self.a=="AdaBoost":
            self.modificationlabel.hide()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.hide()
            self.modify_label2.hide()
            self.modify_label3.hide()
            self.comboBox.hide()
            self.comboBox2.hide()
            self.comboBox3.hide()

        elif self.a=="Multi-layer Perceptron":
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.show()
            self.modify_label2.show()
            
            self.modify_label1.setText("Select\n activation")
            self.modify_label2.setText("Select\n solver")
            
            self.kernal_option="relu"
            self.gamma_option="adam"
            
            self.comboBox.show()
            self.comboBox2.show()
            self.comboBox3.hide()
            self.modify_label3.hide()
            self.modificationlabel.setText("Modify\n"+self.a)
            kernal_option_array=['relu','identity','logistic','tanh']
            gamma_option_array=['adam','sgd','lbfgs']
            for i in range(len(kernal_option_array)):
                self.comboBox.addItem(kernal_option_array[i])
            for i in range(len(gamma_option_array)):
                self.comboBox2.addItem(gamma_option_array[i]) 

        elif self.a=="VotingClassifier":
            self.modificationlabel.show()
            self.comboBox.clear()
            self.comboBox2.clear()
            self.modify_label1.hide()
            self.modify_label2.hide()
            self.modify_label3.hide()
            self.comboBox.hide()
            self.comboBox2.hide()
            self.comboBox3.hide()
            self.modificationlabel.setText("VotingClassifier is feeded by \nLinearSVC\nKNeighborsClassifier\nRandomForestClassifier")
            
            self.modify_label3.adjustSize()
            
                
            
                


           

                

                       


                  

        self.comboBox.activated[str].connect(self.comboBox_click)
        self.comboBox2.activated[str].connect(self.comboBox2_click)


               
       
        
    
    def comboBox_click(self,text):
           self.solver_option=text
           self.bootstrip_option=text
           self.criterion_option=text
           self.kernal_option=text
           self.algorithm_option=text
           self.lose_option=text


    def comboBox2_click(self,text):
           self.multiclass_option=text
           self.max_features_option=text  
           self.gamma_option=text
           self.weights_option=text     

    def cal(self):
            x=self.dataset.iloc[:,:-1].values
            y=self.dataset.iloc[:,-1].values
            self.test_rang=float(self.select_test_range.value())
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=self.test_rang)
            if self.a=="DecisionTree":
                
                
                model=tree.DecisionTreeClassifier(criterion =self.criterion_option, 
                               max_features = self.max_features_option)
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            
            elif self.a=="RandomForest":
                self.n_estimators_option=self.comboBox3.value()
                if self.bootstrip_option == "True":
                    self.bootstrap_true_false=True
                elif self.bootstrip_option == "False":
                    self.bootstrap_true_false=False
                model = RandomForestClassifier(n_estimators=self.n_estimators_option, 
                               bootstrap = self.bootstrap_true_false,
                               max_features = self.max_features_option)
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            
            elif self.a=="Bagging":
                model=BaggingClassifier()
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="AdaBoost":
                model=AdaBoostClassifier()
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="LogisticRegression":

                model=LogisticRegression(solver=self.solver_option,multi_class=self.multiclass_option)
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="Support Vector Machine":
                try:
                    model=svm.SVC(kernel=self.kernal_option,gamma=self.gamma_option)
                    start = time.time()
                    model.fit(x_train,y_train)
                    end = time.time()
                    start2 = time.time()
                    result=model.predict(x_test)
                    end2 = time.time()
                    training_time=(end - start)*1000
                
                    self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                except Exception as e:
                    print(repr(e))
                
                
            elif self.a=="BernoulliNB":
                model=BernoulliNB()
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="ComplementNB":
                model=ComplementNB()
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="GaussianNB":
                model=GaussianNB()
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="MultinomialNB":
                model=MultinomialNB()
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                

            elif self.a=="KNeighborsClassifier":
                self.n_neighbors_option=self.comboBox3.value()
                model=KNeighborsClassifier(n_neighbors=self.n_neighbors_option, weights=self.weights_option, algorithm=self.algorithm_option)
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="Multi-layer Perceptron":
                model=MLPClassifier(activation=self.kernal_option,solver=self.gamma_option)
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="ExtraTreeClassifier":
                self.n_estimators_option=self.comboBox3.value()
                model=ExtraTreesClassifier(n_estimators=self.n_estimators_option,criterion =self.criterion_option, 
                               max_features = self.max_features_option)
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="GradientBoostingClassifier":
                self.n_estimators_option=self.comboBox3.value()
                
                model=GradientBoostingClassifier(loss=self.lose_option, 
                               n_estimators=self.n_estimators_option)
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                
            elif self.a=="VotingClassifier":
                model=VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])
                start = time.time()
                model.fit(x_train,y_train)
                end = time.time()
                start2 = time.time()
                result=model.predict(x_test)
                end2 = time.time()
                training_time=(end - start)*1000
                
                self.printResult.setText("Selected Classifier: "+self.a+"\n\nTraning Time: "+str(training_time)+" ms"+"\n\nConfusion Matrix:\n"+str(confusion_matrix(y_test, result))+"\n\n\n"+classification_report(y_test,result))
                

                

        
            
        
            
    def clickBox(self,state):
        if state == Qt.Checked:
            self.multiclass_option="ovr"      
                    
             
    def LogisticRegression_solver(self, i):
        self.solver_option=str(i.text())
        
                  
 
         

if __name__ == "__main__":
    import sys
    modifyclassifier=""
    dataset="temp"
    a="temp"
    #LogisticR
    solver_option="temp"
    multiclass_option="auto"
    #randomforest
    bootstrip_option=""
    max_features_option=""
    n_estimators_option=0
    bootstrap_true_false=True
    #Decissiontree
    criterion_option=""
    #SVM
    kernal_option=""
    gamma_option=""
    #KNN
    algorithm_option=""
    weights_option=""
    n_neighbors_option=0
    #GBTS
    lose_option=""




    test_rang=float(0.20)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

