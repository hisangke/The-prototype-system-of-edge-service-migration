# This Python file uses the following encoding: utf-8
import sys
import os
import PySide2
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets, QtGui
import random
import networkx
from LogsTextEditOutput import LogsTextEditOutput
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class EdgeServiceMigrationUI(QTabWidget):
    def __init__(self, parent=None):
        super(EdgeServiceMigrationUI, self).__init__(parent)
        self.setWindowTitle("Edge Service Migration Simulation System")
        self.tab0 = QListWidget()
        self.tab0.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tab1 = QWidget()
        self.tab2=QTabWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.tab0UIcomboBox=QComboBox()

        self.tab0UIstatu=False

        self.addTab(self.tab0, "Tab 0")
        self.tab0UI()
        self.edgeNodesConfigureList=[]
        self.edgeServicesConfigureList=[]
        self.edgeServicesLabelList=[]
        self.adjacencyMatrix=[]
        self.adjacencyMatrixSpinBox=[]
        self.adjacencyMatrixData=[]
        self.edgeNodesConfigureData=[]
        self.edgeServicesConfigureData=[]
        self.migrationResultLabelList=[]


        self.textEdit=QTextEdit()

    def edgeNodesConfigureListValueChanged(self):
        self.edgeNodesConfigureData=[[] for index in range(int(self.tab0UIcomboBox.currentText()))]
        QtCore.qDebug("Value Change")
        for index in range(int(self.tab0UIcomboBox.currentText())):
            data=[]
            for i in range(len(self.edgeNodesConfigureList[index])):
                data.append(self.edgeNodesConfigureList[index][i].value())
            self.edgeNodesConfigureData[index]=data


    def tab0UIcomboxBoxSelectionChanged(self):
        self.tab0UILabel.setText("EdgeNodeNumber: "+str(self.tab0UIcomboBox.currentText()))
        #self.tab0UIcomboBox.hide()
        self.edgeServicesConfigureList=[[] for i in range(int(self.tab0UIcomboBox.currentText()))]
        self.edgeServicesConfigureData=[[] for i in range(int(self.tab0UIcomboBox.currentText()))]
        nodeswindow=QMainWindow()
        realmScroll = QScrollArea(nodeswindow)
        nodeswindow.setCentralWidget(realmScroll)
        realmScroll.setWidgetResizable(True)
        container = QWidget()
        container.setMinimumHeight(0)
        realmScroll.setWidget(container)
        nodesLayout = QFormLayout(container)
        self.statuList=[False for i in range(int(self.tab0UIcomboBox.currentText()))]
        self.edgeNodesConfigureList=[]
        for index in range(int(self.tab0UIcomboBox.currentText())):

            hbox = QHBoxLayout()
            hbox1 = QHBoxLayout()
            hbox1.addWidget(QLabel("EdgeNode"+str("{:>5}".format(index))+":  Cpu: "),0,QtCore.Qt.AlignLeft)
            hbox1_spinbox=QDoubleSpinBox()
            hbox1_spinbox.setFixedWidth(150)
            hbox1_spinbox.setMaximum(1000.0)
            hbox1_spinbox.setDecimals(15)
            hbox1_spinbox.setSingleStep(0.0000000000001)
            hbox1_spinbox.setValue(1.4)
            hbox1_spinbox.valueChanged.connect(self.edgeNodesConfigureListValueChanged)
            hbox1.addWidget(hbox1_spinbox,0,QtCore.Qt.AlignLeft)
            hbox1.addStretch(2)

            hbox.addLayout(hbox1)

            hbox2 = QHBoxLayout()
            hbox2.addWidget(QLabel("        RAM: "),0,QtCore.Qt.AlignLeft)
            hbox2_spinbox=QDoubleSpinBox()
            hbox2_spinbox.setFixedWidth(150)
            hbox2_spinbox.setMaximum(1000.0)
            hbox2_spinbox.setDecimals(15)
            hbox2_spinbox.setSingleStep(0.0000000000001)
            hbox2_spinbox.setValue(1.0)
            hbox2_spinbox.valueChanged.connect(self.edgeNodesConfigureListValueChanged)
            hbox2.addWidget(hbox2_spinbox,0,QtCore.Qt.AlignLeft)
            hbox2.addStretch(2)
            hbox.addLayout(hbox2)

            hbox3 = QHBoxLayout()
            hbox3.addWidget(QLabel("Storage: "),0,QtCore.Qt.AlignLeft)
            hbox3_spinbox=QDoubleSpinBox()
            hbox3_spinbox.setFixedWidth(150)
            hbox3_spinbox.setDecimals(15)
            hbox3_spinbox.setSingleStep(0.0000000000001)
            hbox3_spinbox.setMaximum(1000.0)
            hbox3_spinbox.setValue(2.0)
            hbox3.addWidget(hbox3_spinbox,0,QtCore.Qt.AlignLeft)
            hbox3_spinbox.valueChanged.connect(self.edgeNodesConfigureListValueChanged)
            hbox3.addStretch(2)
            hbox.addLayout(hbox3)

            hbox4 = QHBoxLayout()
            hbox4.addWidget(QLabel("Threshold: "),0,QtCore.Qt.AlignLeft)
            hbox4_spinbox=QDoubleSpinBox()
            hbox4_spinbox.setFixedWidth(150)
            hbox4_spinbox.setDecimals(15)
            hbox4_spinbox.setSingleStep(0.0000000000001)
            hbox4_spinbox.setMaximum(1000.0)
            hbox4_spinbox.setValue(0.68)
            hbox4.addWidget(hbox4_spinbox,0,QtCore.Qt.AlignLeft)
            hbox4_spinbox.valueChanged.connect(self.edgeNodesConfigureListValueChanged)
            hbox4.addStretch(2)
            hbox.addLayout(hbox4)

            nodesLayout.addRow(hbox)

            edgeNodeConfigure=[hbox1_spinbox,hbox2_spinbox,hbox3_spinbox,hbox4_spinbox]
            self.edgeNodesConfigureList.append(edgeNodeConfigure)
        if self.tab0UIstatu:
            self.tab0UIlayout.removeRow(self.tab0UInodeswindow)

        self.tab0UIlayout.insertRow(2,nodeswindow)
        self.tab0UInodeswindow=nodeswindow

        if bool(1-self.tab0UIstatu):
            self.addTab(self.tab2,"Tab 2")
            self.tab2UI()
        self.tab0UIstatu=True

        self.edgeNodesConfigureData=[[] for index in range(int(self.tab0UIcomboBox.currentText()))]

        for index in range(int(self.tab0UIcomboBox.currentText())):
            data=[]
            for i in range(len(self.edgeNodesConfigureList[index])):
                data.append(self.edgeNodesConfigureList[index][i].value())
            self.edgeNodesConfigureData[index]=data


    def tab0UI(self):
        self.tab0UIlayout = QFormLayout()

        self.tab0UIcomboBox.setFixedWidth(100)
        self.tab0UIcomboBox.addItems([str(index) for index in range(1000)])
        self.tab0UILabel=QLabel("EdgeNodeNumber: 0 ")
        layout=QHBoxLayout()
        layout.addWidget(self.tab0UILabel,0,QtCore.Qt.AlignLeft)
        layout.addWidget(self.tab0UIcomboBox,0,QtCore.Qt.AlignLeft)
        layout.addStretch(2)

        self.tab0UIlayout.insertRow(0,layout)
        self.setTabText(0, "Edge Node Configure")
        # 在标签1中添加这个帧布局
        self.tab0.setLayout(self.tab0UIlayout)
        self.tab0UIcomboBox.currentIndexChanged.connect(self.tab0UIcomboxBoxSelectionChanged)
    # 同理如上
    def tab1UI(self):
        def adjacencyMatrixSpinBoxChanged():
            self.adjacencyMatrixData=[]
            for index1 in range(int(self.tab0UIcomboBox.currentText())):
                data=[]
                for index2 in range(int(self.tab0UIcomboBox.currentText())):
                    data.append(self.adjacencyMatrixSpinBox[index1][index2].value())
                    #QtCore.qDebug(str(self.adjacencyMatrixSpinBox[index1][index2].value()))
                self.adjacencyMatrixData.append(data)

        self.setTabText(2, "Edge Node Adjacency Matrix")
        window=QMainWindow()
        realmScroll = QScrollArea(window)
        window.setCentralWidget(realmScroll)
        realmScroll.setWidgetResizable(True)
        container = QWidget()
        container.setMinimumHeight(0)
        realmScroll.setWidget(container)
        nodesLayout = QFormLayout(container)

        buttonHbox = QHBoxLayout()
        importButton=QPushButton("Import Data From File")
        #importButton.setStyleSheet('QPushButton {background-color: red;}')
        importButton.clicked.connect(self.getFiles)
        importButton.resize(150, 480)
        importButton.setMaximumSize(150, 480)
        importButton.setMaximumSize(150, 480)
        buttonHbox.addWidget(importButton,0,QtCore.Qt.AlignLeft)

        def submitAdjacencyMatrixData():
            importButton.setEnabled(False)
            submitButton.setEnabled(False)
            self.addTab(self.tab4, "Tab 4")
            self.tab4UI()
            self.addTab(self.tab3, "Tab 3")
            self.tab3UI()
            self.addTab(self.tab5, "Tab 5")
            self.tab5UI()


        submitButton=QPushButton("Submit Adjacency Matrix")
        #submitButton.setStyleSheet('QPushButton {background-color: red;}')
        submitButton.clicked.connect(submitAdjacencyMatrixData)
        submitButton.resize(150, 480)
        submitButton.setMaximumSize(150, 480)
        submitButton.setMaximumSize(150, 480)
        buttonHbox.addWidget(submitButton,0,QtCore.Qt.AlignLeft)

        nodesLayout.addRow(buttonHbox)
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel(),0,QtCore.Qt.AlignLeft)
        for index in range(int(self.tab0UIcomboBox.currentText())):
            hbox.addWidget(QLabel(" Node "+str(index)),0,QtCore.Qt.AlignLeft)
        nodesLayout.insertRow(2,hbox)

        self.adjacencyMatrixSpinBox=[[] for index in range(int(self.tab0UIcomboBox.currentText()))]

        for index in range(int(self.tab0UIcomboBox.currentText())):
            hbox = QHBoxLayout()
            spinBoxList=[]
            hbox.addWidget(QLabel("Node "+str(index)),0,QtCore.Qt.AlignLeft)
            for _ in range(int(self.tab0UIcomboBox.currentText())):
                spinBox=QDoubleSpinBox()
                spinBox.setFixedWidth(150)
                spinBox.setMaximum(1000.0)
                spinBox.valueChanged.connect(adjacencyMatrixSpinBoxChanged)
                hbox.addWidget(spinBox,0,QtCore.Qt.AlignLeft)
                spinBoxList.append(spinBox)
            self.adjacencyMatrixSpinBox[index]=spinBoxList
            nodesLayout.insertRow(-1,hbox)

        layout = QFormLayout()
        layout.insertRow(2,window)
        self.tab1.setLayout(layout)
        self.adjacencyMatrixData=[]
        for index1 in range(int(self.tab0UIcomboBox.currentText())):
            data=[]
            for index2 in range(int(self.tab0UIcomboBox.currentText())):
                data.append(self.adjacencyMatrixSpinBox[index1][index2].value())
                #QtCore.qDebug(str(self.adjacencyMatrixSpinBox[index1][index2].value()))
            self.adjacencyMatrixData.append(data)


    def getFiles(self):
        def adjacencyMatrixSpinBoxChanged():
            self.adjacencyMatrixData=[]
            for index1 in range(int(self.tab0UIcomboBox.currentText())):
                data=[]
                for index2 in range(int(self.tab0UIcomboBox.currentText())):
                    data.append(self.adjacencyMatrixSpinBox[index1][index2].value())
                    #QtCore.qDebug(str(self.adjacencyMatrixSpinBox[index1][index2].value()))
                self.adjacencyMatrixData.append(data)



        dig=QFileDialog()
        dig.setFileMode(QFileDialog.AnyFile)
        dig.setFilter(QtCore.QDir.Files)
        if dig.exec_():
            filenames=dig.selectedFiles()
            if len(filenames)!=1:
                dial = QMessageBox()
                dial.setText(u"Adjacency matrix file not selected\n"+r"Reselect the adjacency matrix file? ")
                dial.setWindowTitle("Caution!")
                dial.setIcon(QMessageBox.Question)
                dial.addButton('No', QMessageBox.RejectRole)
                usunT = dial.addButton('Yes', QMessageBox.YesRole)
                dial.exec_()
                if dial.clickedButton() == usunT:
                    self.getFiles()
                else:
                    return
            file=open(filenames[0],'r')
            for num,line in enumerate(file):
                line=line.replace("\n","")
                keys=line.split(",")
                print(keys,len(keys),int(self.tab0UIcomboBox.currentText()))
                if len(keys)!=int(self.tab0UIcomboBox.currentText()):
                    dial = QMessageBox()
                    dial.setText(u"The document does not meet the requirements("+str(self.tab0UIcomboBox.currentText())+" nodes)\n"+"Reselect the adjacency matrix file? ")
                    dial.setWindowTitle("Caution!")
                    dial.setIcon(QMessageBox.Question)
                    dial.addButton('No', QMessageBox.RejectRole)
                    usunT = dial.addButton('Yes', QMessageBox.YesRole)
                    dial.exec_()
                    if dial.clickedButton() == usunT:
                        self.getFiles()
                    else:
                        break
                    break
                for index in range(len(keys)):
                    self.adjacencyMatrixSpinBox[num][index].setValue(float(keys[index]))
                adjacencyMatrixSpinBoxChanged()
            file.close()

    def tab5UI(self):
        self.setTabText(5, "Edge Service Migration Result")

        window=QMainWindow()
        realmScroll = QScrollArea(window)
        window.setCentralWidget(realmScroll)
        realmScroll.setWidgetResizable(True)
        container = QWidget()
        container.setMinimumHeight(0)
        realmScroll.setWidget(container)
        nodesLayout = QFormLayout(container)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel(str("{:>7}".format("Node"))),0,QtCore.Qt.AlignCenter)
        for j in range(int(self.tab0UIcomboBox.currentText())):
            label=QLabel(str("{:>3}".format(j)))
            hbox.addWidget(label,0,QtCore.Qt.AlignCenter)
        label=QLabel(str("cloud".format(j)))
        hbox.addWidget(label,0,QtCore.Qt.AlignCenter)
        nodesLayout.insertRow(-1,hbox)


        self.migrationResultLabelList=[[] for index in range(int(self.tab0UIcomboBox.currentText())+1)]
        for j in range(int(self.tab0UIcomboBox.currentText())+1):
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(str("{:>5}".format(j))+" "),0,QtCore.Qt.AlignCenter)
            labelList=[]
            for i in range(int(self.tab0UIcomboBox.currentText())+1):
                label=QLabel(str("{:>5}".format("")))
                labelList.append(label)
                hbox.addWidget(label,0,QtCore.Qt.AlignCenter)
            self.migrationResultLabelList[j]=labelList
            nodesLayout.insertRow(-1,hbox)

        layout = QFormLayout()
        layout.insertRow(2,window)

        self.tab5.setLayout(layout)

    def tab3UI(self):
        def startButtonClicked():
            self.startButton.setEnabled(False)
            from EdgeMigration import EdgeMigration
            self.textEdit.clear()

            edgeNodeNumber=int(self.tab0UIcomboBox.currentText())
##########################################################################
            #print("#####",self.edgeServicesConfigureData)

            system=EdgeMigration(edgeNodeNumber=edgeNodeNumber,
                                                textEdit=self.textEdit,
                                                adjacencyMatrixData=self.adjacencyMatrixData,
                                                migrationResultLabelList=self.migrationResultLabelList,
                                                edgeNodesConfigureData=self.edgeNodesConfigureData,
                                                edgeServicesConfigureData=self.edgeServicesConfigureData)
            statu=False
            i=0
            while bool(1-statu):
                costTime,statu=system.run()
                QtCore.qDebug(str(i)+": "+str(costTime)+" "+str(statu))
                i+=1

                if i==3:
                    break


            LogsTextEditOutput(textEdit=self.textEdit,text=str(costTime))
            self.startButton.setEnabled(True)
            #self.addTab(self.tab5, "Tab 5")
            #self.tab5UI()
##########################################################################

        self.textEdit.setReadOnly(True)
        self.textEdit.resize(700,300)
        self.textEdit.setMinimumSize(700,300)
        self.setTabText(3, "Edge Node Topology")
        self.setTabText(4, "Logs Information")

        nodesLayout = QFormLayout()

        hbox = QHBoxLayout()
        self.startButton=QPushButton('Start')
        #self.startButton.setStyleSheet('QPushButton {background-color: red;}')
        self.startButton.clicked.connect(startButtonClicked)

        self.startButton.resize(150, 480)
        self.startButton.setMaximumSize(150, 480)
        self.startButton.setMaximumSize(150, 480)

        hbox.addWidget(self.startButton,0,QtCore.Qt.AlignLeft)
        nodesLayout.insertRow(2,hbox)

        nodesLayout.addRow(self.textEdit)

        layout = QFormLayout()
        #layout.insertRow(2,window)
        layout.addRow(nodesLayout)
        self.tab3.setLayout(layout)

    def tab4UI(self):

        self.setTabText(4, "Logs Information")
        window=QMainWindow()
        realmScroll = QScrollArea(window)
        window.setCentralWidget(realmScroll)
        realmScroll.setWidgetResizable(True)
        container = QWidget()
        container.setMinimumHeight(0)
        realmScroll.setWidget(container)
        nodesLayout = QFormLayout(container)

        self.adjacencyMatrixData=[]
        for index1 in range(int(self.tab0UIcomboBox.currentText())):
            tempdata=[]
            for index2 in range(int(self.tab0UIcomboBox.currentText())):
                tempdata.append(self.adjacencyMatrixSpinBox[index1][index2].value())
            self.adjacencyMatrixData.append(tempdata)

        data=self.adjacencyMatrixData
        edges=[]
        nodes=[i for i in range(len(data))]
        for col in range(len(data)):
            for row in range(len(data[0])):
                if data[row][col]>0.0:
                    edges.append((row,col,data[row][col]))
        import matplotlib.pyplot as plt
        import networkx as nx

        G1 = nx.Graph()
        G1.add_nodes_from(nodes)
        G1.add_weighted_edges_from(edges)
        nx.draw(G1,with_labels=True, font_weight='bold',node_size=600,font_size=18)
        plt.savefig("./topology.png")


        hbox = QHBoxLayout()
        label=QLabel()
        pixmap=QtGui.QPixmap(QtGui.QImage("./topology.png"))
        pixmap = pixmap.scaled(350, 350, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        label.setPixmap(pixmap)
        os.remove("./topology.png")


        hbox.addWidget(label,0,QtCore.Qt.AlignCenter)


        nodesLayout.insertRow(2,hbox)

        layout = QFormLayout()
        layout.insertRow(2,window)
        self.tab4.setLayout(layout)




    def edgeServicesConfigureListValueChanged(self):
        #QtCore.qDebug("Value Change "+str(self.tab2.currentIndex())+" "+str(len(self.edgeServicesConfigureList)))
        edgeServices=self.edgeServicesConfigureList[self.tab2.currentIndex()]#[hbox1_spinbox,hbox2_spinbox,hbox3_spinbox]

        for index in range(len(edgeServices)):
            hbox1_spinbox,hbox2_spinbox,hbox3_spinbox,hbox4_spinbox=edgeServices[index]
            QtCore.qDebug(str(hbox1_spinbox.value())+" "+str(hbox2_spinbox.value())+" "+str(hbox3_spinbox.value())+" "+str(hbox4_spinbox.value()))

        self.edgeServicesConfigureData=[[] for i in range(int(self.tab0UIcomboBox.currentText()))]
        for index1 in range(int(self.tab0UIcomboBox.currentText())):
            edgeServices=self.edgeServicesConfigureList[index1]
            data=[]
            for index2 in range(len(edgeServices)):
                hbox1_spinbox,hbox2_spinbox,hbox3_spinbox,hbox4_spinbox=edgeServices[index2]
                data.append([hbox1_spinbox.value(),hbox2_spinbox.value(),hbox3_spinbox.value(),hbox4_spinbox.value()])
            self.edgeServicesConfigureData[index1]=data


    def tab2UI(self):
        subcomboBoxList=[]
        layoutList=[]
        servicesWindowList=[[] for i in range(1000)]
        self.setTabText(1, "Edge Service Configure")



        def subcomboxBoxSelectionChanged():

            servicesWindow=QMainWindow()
            realmScroll = QScrollArea(servicesWindow)
            servicesWindow.setCentralWidget(realmScroll)
            realmScroll.setWidgetResizable(True)
            container = QWidget()
            container.setMinimumHeight(0)
            realmScroll.setWidget(container)
            nodesLayout = QFormLayout(container)
            edgeServices=[]

            self.edgeServicesLabelList[self.tab2.currentIndex()].setText("EdgeServiceNumber: "+str(subcomboBoxList[self.tab2.currentIndex()].currentText()))
            #subcomboBoxList[self.tab2.currentIndex()].hide()

            statu=False
            for index in range(len(subcomboBoxList)):
                if int(subcomboBoxList[index].currentText())>0:
                    statu=True
                else:
                    statu=False
            if statu:

                self.addTab(self.tab1, "Tab 1")
                self.tab1UI()

            if str(self.tab2.currentIndex())!=str("-1"):
                for index in range(int(subcomboBoxList[self.tab2.currentIndex()].currentText())):
                    hbox = QHBoxLayout()
                    hbox1 = QHBoxLayout()
                    hbox1.addWidget(QLabel("EdgeService"+str("{:>5}".format(index))+":  Cpu: "),0,QtCore.Qt.AlignLeft)
                    hbox1_spinbox=QDoubleSpinBox()
                    hbox1_spinbox.setFixedWidth(150)
                    hbox1_spinbox.setDecimals(15)
                    hbox1_spinbox.setSingleStep(0.0000000000001)
                    hbox1_spinbox.setMaximum(1000.0)
                    hbox1_spinbox.setValue(0.01)
                    hbox1_spinbox.valueChanged.connect(self.edgeServicesConfigureListValueChanged)
                    hbox1.addWidget(hbox1_spinbox,0,QtCore.Qt.AlignLeft)
                    hbox1.addStretch(2)
                    hbox.addLayout(hbox1)

                    hbox2 = QHBoxLayout()
                    hbox2.addWidget(QLabel("         RAM: "),0,QtCore.Qt.AlignLeft)
                    hbox2_spinbox=QDoubleSpinBox()
                    hbox2_spinbox.setFixedWidth(150)
                    hbox2_spinbox.setDecimals(15)
                    hbox2_spinbox.setSingleStep(0.0000000000001)
                    hbox2_spinbox.setValue(0.001)
                    hbox2_spinbox.setMaximum(1000.0)
                    hbox2_spinbox.valueChanged.connect(self.edgeServicesConfigureListValueChanged)
                    hbox2.addWidget(hbox2_spinbox,0,QtCore.Qt.AlignLeft)
                    hbox2.addStretch(2)
                    hbox.addLayout(hbox2)

                    hbox3 = QHBoxLayout()
                    hbox3.addWidget(QLabel("Storage: "),0,QtCore.Qt.AlignLeft)
                    hbox3_spinbox=QDoubleSpinBox()
                    hbox3_spinbox.setFixedWidth(150)
                    hbox3_spinbox.setDecimals(15)
                    hbox3_spinbox.setSingleStep(0.0000000000001)
                    hbox3_spinbox.setMaximum(1000.0)
                    hbox3_spinbox.setValue(0.004619140625)
                    hbox3.addWidget(hbox3_spinbox,0,QtCore.Qt.AlignLeft)
                    hbox3_spinbox.valueChanged.connect(self.edgeServicesConfigureListValueChanged)
                    hbox3.addStretch(2)
                    hbox.addLayout(hbox3)

                    hbox4 = QHBoxLayout()
                    hbox4.addWidget(QLabel("Ratio: "),0,QtCore.Qt.AlignLeft)
                    hbox4_spinbox=QDoubleSpinBox()
                    hbox4_spinbox.setFixedWidth(150)
                    hbox4_spinbox.setDecimals(15)
                    hbox4_spinbox.setSingleStep(0.0000000000001)
                    hbox4_spinbox.setMaximum(1000.0)
                    hbox4_spinbox.setValue(0.03)
                    hbox4.addWidget(hbox4_spinbox,0,QtCore.Qt.AlignLeft)
                    hbox4_spinbox.valueChanged.connect(self.edgeServicesConfigureListValueChanged)
                    hbox4.addStretch(2)
                    hbox.addLayout(hbox4)

                    nodesLayout.addRow(hbox)
                    edgeServiceConfigure=[hbox1_spinbox,hbox2_spinbox,hbox3_spinbox,hbox4_spinbox]
                    edgeServices.append(edgeServiceConfigure)

            self.edgeServicesConfigureList[self.tab2.currentIndex()]=edgeServices
            #QtCore.qDebug(str(self.tab2.currentIndex())+str(len(servicesWindowList)))
            if self.statuList[self.tab2.currentIndex()]:
                layoutList[self.tab2.currentIndex()].removeRow(servicesWindowList[self.tab2.currentIndex()][-1])
            self.statuList[self.tab2.currentIndex()]=True

            layoutList[self.tab2.currentIndex()].insertRow(2,servicesWindow)
            servicesWindowList[self.tab2.currentIndex()].append(servicesWindow)

            self.edgeServicesConfigureData=[[] for i in range(int(self.tab0UIcomboBox.currentText()))]
            for index1 in range(int(self.tab0UIcomboBox.currentText())):
                edgeServices=self.edgeServicesConfigureList[index1]
                data=[]
                for index2 in range(len(edgeServices)):
                    hbox1_spinbox,hbox2_spinbox,hbox3_spinbox,hbox4_spinbox=edgeServices[index2]
                    data.append([hbox1_spinbox.value(),hbox2_spinbox.value(),hbox3_spinbox.value(),hbox4_spinbox.value()])
                self.edgeServicesConfigureData[index1]=data




        for i in range(int(self.tab0UIcomboBox.currentText())):
            subTab=QWidget()
            layout = QFormLayout()
            subcomboBox=QComboBox()
            subcomboBox.setFixedWidth(100)
            subcomboBox.addItems([str(index) for index in range(1000)])
            subcomboBox.currentIndexChanged.connect(subcomboxBoxSelectionChanged)
            label=QLabel("EdgeServiceNumber: 0 ")
            self.edgeServicesLabelList.append(label)

            firstLayout=QHBoxLayout()
            firstLayout.addWidget(label,0,QtCore.Qt.AlignLeft)
            firstLayout.addWidget(subcomboBox,0,QtCore.Qt.AlignLeft)
            firstLayout.addStretch(2)
            layout.insertRow(0,firstLayout)

            #layout.addRow("EdgeServiceNumber:",subcomboBox)

            subTab.setLayout(layout)
            subcomboBoxList.append(subcomboBox)
            layoutList.append(layout)
            self.tab2.addTab(subTab, "EdgeNode "+str(i))

