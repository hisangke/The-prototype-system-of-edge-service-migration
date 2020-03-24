main.pyproject

{
    "files": ["main.py","Service.py","Graph_Matrix.py","EdgeMigration.py","RandomStorageSize.py","EdgeServiceMigrationUI.py","MaximumFlow.py","EdgeNode.py","LogsTextEditOutput.py","monkey.png"]
}

EdgeMigration.py

from Service import Service
import time
import random

from MaximumFlow import MaximumFlow
from EdgeNode import EdgeNode
adjacencyMatrixData=[
[0.0, 0.0, 0.0, 0.0, 37.5, 0.0, 0.0, 0.0, 0.0, 0.0],
 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 37.5, 0.0, 0.0, 0.0],
 [0.0, 0.0, 0.0, 7.5, 7.5, 108.0, 7.5, 0.0, 108.0, 37.5],
 [0.0, 0.0, 7.5, 0.0, 0.0, 0.0, 7.5, 0.0, 7.5, 0.0],
 [37.5, 0.0, 7.5, 0.0, 0.0, 0.0, 0.0, 37.5, 0.0, 0.0],
 [0.0, 0.0, 108.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
 [0.0, 37.5, 7.5, 7.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
 [0.0, 0.0, 0.0, 0.0, 37.5, 0.0, 0.0, 0.0, 0.0, 108.0],
 [0.0, 0.0, 108.0, 7.5, 0.0, 0.0, 0.0, 0.0, 0.0, 108.0],
 [0.0, 0.0, 37.5, 0.0, 0.0, 0.0, 0.0, 108.0, 108.0, 0.0]]

from LogsTextEditOutput import LogsTextEditOutput

#EdgeMigration(edgeNodeNumber=int(self.tab0UIcomboBox.currentText()),threshold=0.85,textEdit=self.textEdit,adjacencyMatrixData=self.adjacencyMatrixData)

class EdgeMigration:
def __init__(self, edgeNodeNumber=1,textEdit="",adjacencyMatrixData="",migrationResultLabelList=[],edgeNodesConfigureData=[],edgeServicesConfigureData=[]):
        self.edgeServicesConfigureData=edgeServicesConfigureData
        self.edgeNodesConfigureData=edgeNodesConfigureData
        self.textEdit=textEdit
        self.adjacencyMatrixData=adjacencyMatrixData

        self.migrationStorage=0.0
        self.migrationResultLabelList=migrationResultLabelList
        self.edgeNodeNumber=edgeNodeNumber
        self.edgeNodes=[]
        self.installEdgeNode()
        self.migrationServiceArray=[[0 for i in range(self.edgeNodeNumber)] for j in range(self.edgeNodeNumber)]
    def run(self):
        startTime=time.time()
        text="Staring system at:\t"+str(startTime)
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        statu=True
        while(statu):
            statu=False
            self.updateEdges()
            text="-----------------------------------------------------------------------"
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
            self.logs()
            text="-----------------------------------------------------------------------"
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
            if self.getTotalService()==self.getEdgeNode(self.getEdgeNodeNumber()-1).getServicesNumber():
                break
        endTime=time.time()
        text="End system at:\t"+str(endTime)
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        costTime=endTime-startTime
        text="Cost time is:\t"+str(costTime)
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        return [costTime,self.getTotalService()==self.getEdgeNode(self.getEdgeNodeNumber()-1).getServicesNumber()]
def updateEdges(self):
        for index in range(self.getEdgeNodeNumber()):
            edgeNode=self.getEdgeNode(index);
            try:
                edgeNode.updateServices()
            except:
                self.migrationEdgeService(edgeNode,index)
        return True
    def migrationEdgeService(self,edgeNode,edgeNodeIndex):
        #print("$$$$$$$$",self.edgeNodeNumber-1)
        model=MaximumFlow(adjacencyMatrixData=self.adjacencyMatrixData,nodesNumber=self.edgeNodeNumber-1)
        serviceIndex=edgeNode.getMigrationServiceIndex()
        migrationTime=[9999 for i in range(self.edgeNodeNumber)]
        for i in range(self.getEdgeNodeNumber()):
            node=self.getEdgeNode(i)
            if node.preMigrationEdgeService(edgeNode.getService(serviceIndex)):
                if i<(self.getEdgeNodeNumber()-1):
                    migrationTime[i]=edgeNode.getService(serviceIndex).getStorage()/model.value(edgeNodeIndex,i)
                    if i==edgeNodeIndex:
                        migrationTime[i]=9999.0
                    else:
                        migrationTime[i]=900
                        text="********"+str(edgeNodeIndex)+"******** "+str(i)+" ********"+str(edgeNode.getService(serviceIndex).getStorage())+"********** "+str(model.value(edgeNodeIndex,i))
                        #print(text)
                        LogsTextEditOutput(self.textEdit,text=text)
                else:
                    migrationTime[i]=9999.0
        mintimes=9999.0
        index=0
        for var in range(self.getEdgeNodeNumber()-1):
            if migrationTime[var]<=mintimes:
                index=var
                mintimes=migrationTime[var]
        if mintimes==9999.0:
            mintimes=migrationTime[self.getEdgeNodeNumber()-1]
            index=self.getEdgeNodeNumber()-1
        migrationService=edgeNode.getService(serviceIndex)
        node=self.getEdgeNode(index)
        if node.addService(migrationService):
            print("#Before: \n",self.migrationServiceArray)
            self.migrationServiceArray[edgeNodeIndex][index]+=1
            print("#After: \n",self.migrationServiceArray)
            edgeNode.removeService(serviceIndex)
            text="Migration edge service "+str(serviceIndex)+" of "+str(edgeNode.getName())+"("+str(edgeNode.evaluateEdge())+") to edge node "+str(node.getName())+"("+str(node.evaluateEdge())+")"+" and migration time is "+str(mintimes)
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
            if mintimes<900:
                self.edgeServiceMigrationTime+=mintimes
            self.migrationStorage+=migrationService.getStorage()
        return True
def getEdgeNode(self,index):
        if index<self.getEdgeNodeNumber()+1:
            return self.edgeNodes[index]
        else:
            text="Out of range and return the fist edge node!"
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
            return self.edgeNodes[0]
    def getEdgeNodeNumber(self):
        return len(self.edgeNodes)
def logs(self):
        text="This system has "+str(self.getEdgeNodeNumber()-1)+" edge node and a Cloud center."
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        totalService=0
        for index in range(self.getEdgeNodeNumber()):
            edgeNode=self.getEdgeNode(index)
            totalService+=edgeNode.getServicesNumber()
            text="Evaluate "+str(edgeNode.getName())+"\t"+str(edgeNode.evaluateEdge())+"\t"+str(edgeNode.getServicesNumber())
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
        text="The total number of service is "+str(totalService)
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        for var in range(self.edgeNodeNumber-1):
            if var==0:
                text=str("{:>13}".format(""))
                #print(text)
                LogsTextEditOutput(self.textEdit,text=text,newline=False)
            text=str("{:>4}".format(var))+"  "
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text,newline=False,newNumber=False)
        LogsTextEditOutput(self.textEdit,text="\n",newline=False,newNumber=False)
        text=" -----"
        for var in range(self.edgeNodeNumber):
            text+="-----"
        LogsTextEditOutput(self.textEdit,text=text)
        totalMigraitonService=0
        #print()
        for var in range(self.edgeNodeNumber):
            lineText="|"
            #print(lineText,end="")
            for var2 in range(self.edgeNodeNumber):
                totalMigraitonService+=self.migrationServiceArray[var][var2]
                text=str("{:>5}".format(str(self.migrationServiceArray[var][var2])))+" "
                self.migrationResultLabelList[var][var2].setText(text)
                lineText+=text
                #print(text,end="")
            text="|"
            lineText+=text
            LogsTextEditOutput(self.textEdit,text=lineText)
            #print(text)
        text=" -----"
        for var in range(self.edgeNodeNumber):
            text+="-----"
        LogsTextEditOutput(self.textEdit,text=text)
        #print()
        LogsTextEditOutput(self.textEdit,text="")
        text="The total number of migration service is "+str(totalMigraitonService)
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        self.migrationServiceNumber=totalMigraitonService
        return True
    def getMigrationServiceNumber(self):
        totalMigraitonService=0

        for var in range(self.edgeNodeNumber):
            for var2 in range(self.edgeNodeNumber):
                totalMigraitonService+=self.migrationServiceArray[var][var2]
        self.migrationServiceNumber=totalMigraitonService
        return self.migrationServiceNumber
def getEdgeNodeMigrationServiceNumber(self):
        edgeNodetotalMigraitonService=0
        for var in range(self.edgeNodeNumber):
            for var2 in range(self.edgeNodeNumber):
                edgeNodetotalMigraitonService+=self.migrationServiceArray[var][var2]
        return edgeNodetotalMigraitonService
    def getMigrationServiceArray(self):
        return self.migrationServiceArray
    def getTotalService(self):
        totalService=0
        for index in range(self.getEdgeNodeNumber()):
            edgeNode=self.getEdgeNode(index)
            totalService+=edgeNode.getServicesNumber()
        return totalService
    def getEdgeServiceMigrationTime(self):
        return self.edgeServiceMigrationTime
    def getMigrationStorage(self):
        return self.migrationStorage
    def installEdgeNode(self):
        for i in range(self.edgeNodeNumber):
            text="-------------"+str(i)+"---------------"
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
            edgeNodeName="EdgeNode_"+str(i)

            data=self.edgeNodesConfigureData[i]

            edgeNode=EdgeNode(name=edgeNodeName,servicenumber=len(self.edgeServicesConfigureData[i]),cpu=data[0],ram=data[1],
									storage=data[2],threshold=data[3],edgeServicesConfigureData=self.edgeServicesConfigureData[i],textEdit=self.textEdit)
            edgeNode.logs()
            self.edgeNodes.append(edgeNode)
            #print()
            LogsTextEditOutput(self.textEdit,text="")
        #print()
        LogsTextEditOutput(self.textEdit,text="")
        cloudNode=EdgeNode("Cloud",0,1,10000,10000,20000,textEdit=self.textEdit)
        self.edgeNodes.append(cloudNode)
        cloudNode.logs()
        self.edgeNodeNumber=self.getEdgeNodeNumber()
        return True

EdgeNode.py
from Service import Service
from math import exp
from LogsTextEditOutput import LogsTextEditOutput
class EdgeNode:
def __init__(self,name,servicenumber=1,threshold=0.86,cpu=1.4,ram=1,storage=2,edgeServicesConfigureData=[],textEdit=""):
        self.edgeServicesConfigureData=edgeServicesConfigureData
        self.textEdit=textEdit
        self.name=name
        self.servicenumber=servicenumber
        self.threshold=threshold
        self.cpu=cpu
        self.ram=ram
        self.storage=storage
        self.servicesCostCpu=0
        self.servicesCostRam=0
        self.servicesCostStorage=0
        self.services=[]
        self.installService()
        self.updateServicesCost();
        self.textEdit=textEdit
    def preMigrationEdgeService(self,service):
        newcpu=self.getServicesCostCpu()+service.getCpu()+service.getCpu()*(1/3)
        newram=self.getServicesCostRam()+service.getRam()+service.getRam()*(1/3)
        newstorage=self.getServicesCostStorage()+service.getStorage()+service.getStorage()*(1/3)
        statu=(newcpu<self.getCpu())and(newram<self.getRam())and(newstorage<self.getStorage())
        rate=0.95
        ram=newram/self.getRam()
        cpu=newcpu/self.getCpu()
        storage=newstorage/self.getStorage()
        denominator=exp(ram)+exp(cpu)+exp(storage)
        edgeEvaluate=exp(ram)/denominator*ram+exp(cpu)/denominator*cpu+exp(storage)/denominator*storage
        if (ram>rate)or(cpu>rate)or(storage>rate):
            edgeEvaluate=self.threshold
        if (self.threshold>edgeEvaluate)and(statu):
            return True
        else:
            return False

    def updateServices(self):
        for i in range(self.getServicesNumber()):
            edgeEvaluate=self.evaluateEdge()
            if edgeEvaluate>=self.threshold:
                text=str(edgeEvaluate)+">="+str(self.threshold)
                #print(text)
                LogsTextEditOutput(self.textEdit,text=text)
                raise RuntimeError("error: Migration Edge Service for threshold")
            service=self.getService(i)
            statu=service.update(self.getServicesCostRam(),self.getServicesCostCpu(),self.getServicesCostStorage(),self.getRam(),self.getCpu(),self.getStorage())
            self.updateServicesCost()
            if bool(1-statu):
                self.updateServicesCost()
                text="error: Migration Edge Service for resource"
                #print(text)
                LogsTextEditOutput(self.textEdit,text=text)
                break
        self.updateServicesCost()

    def getMigrationServiceIndex(self):
        migrationService=0
        maxValue=-1
        text="getMigrationServiceIndex()"
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        serviceEvaluate=[]
        for index in range(self.getServicesNumber()):

            serviceEvaluate.append(self.evaluateService(index))
            if self.evaluateService(index)>maxValue:
                maxValue=self.evaluateService(index)

                migrationService=index
            text=str(self.evaluateService(index))+" "
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
        text=str(migrationService)
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        return migrationService

    def removeService(self,index):
        del self.services[index]

    def addService(self,service):
        newcpu=self.getServicesCostCpu()+service.getCpu()
        newram=self.getServicesCostRam()+service.getRam()
        newstorage=self.getServicesCostStorage()+service.getStorage()
        statu=(newcpu<self.getCpu())and(newram<self.getRam())and(newstorage<self.getStorage())
        if (self.threshold>self.evaluateEdge())and(statu):
            text=str(self.getName())+"\tinstalled\t"+str(self.getServicesNumber())+" success!"
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
            self.services.append(service)
            return True
        else:
            return False

    def evaluateEdge(self):
        rate=0.99
        ram=self.getServicesCostRam()/self.getRam()
        cpu=self.getServicesCostCpu()/self.getCpu()
        storage=self.getServicesCostStorage()/self.getStorage()
        denominator=exp(ram)+exp(cpu)+exp(storage)
        edgeEvaluate=exp(ram)/denominator*ram+exp(cpu)/denominator*cpu+exp(storage)/denominator*storage
        if (ram>rate)or(cpu>rate)or(storage>rate):
            edgeEvaluate=self.threshold
        return edgeEvaluate

    def evaluateService(self,index):
        service=self.getService(index)
        ram=service.getRam()/self.getServicesCostRam()
        cpu=service.getCpu()/self.getServicesCostCpu()
        storage=service.getStorage()/self.getServicesCostStorage()
        denominator=exp(ram)+exp(cpu)+exp(storage)
        serviceEvaluate=exp(ram)/denominator*ram+exp(cpu)/denominator*cpu+exp(storage)/denominator*storage
        return serviceEvaluate

    def getServicesCostRam(self):
        ram=0
        for i in range(self.getServicesNumber()):
            service= self.getService(i)
            ram+=service.getRam()
        self.servicesCostRam=ram
        return self.servicesCostRam

    def getServicesCostCpu(self):
        cpu=0
        for i in range(self.getServicesNumber()):
            service=self.getService(i)
            cpu+=service.getCpu()
        self.servicesCostCpu=cpu
        return self.servicesCostCpu
    def getServicesCostStorage(self):
        storage=0
        for i in range(self.getServicesNumber()):
            service=self.getService(i)
            storage+=service.getStorage()
        self.servicesCostStorage=storage
        return self.servicesCostStorage

    def logs(self):
        text="The services's logs of "+str(self.getName())+" and the total number of service is "+str(self.getServicesNumber())
        #print(text)
        for i in range(self.getServicesNumber()):
            service=self.getService(i)

            text="Service "+str(i)+" "
            #print(text,end='  ')
            LogsTextEditOutput(self.textEdit,text=text,newline=True,newNumber=False)
            service.logs()
            LogsTextEditOutput(self.textEdit,text="\n",newline=False,newNumber=False)
        text="Total cost of "+str(self.getName())+" Cpu: "+str(self.getServicesCostCpu())+" Ram: "+str(self.getServicesCostRam())+" Storage: "+str(self.getServicesCostStorage())
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text,newline=True)
        return True
    def getServicesNumber(self):
        return len(self.services)
    def getService(self,index):
        if index<self.getServicesNumber():
            return self.services[index]
        else:
            text="\n\nOut of range and return the fist service!"
            #print(text)
            LogsTextEditOutput(self.textEdit,text=text)
            return self.services[0];

    def getRam(self):
        return self.ram
    def getCpu(self):
        return self.cpu
    def getStorage(self):
        return self.storage
    def getName(self):
        return self.name
    def updateServicesCost(self):
        ram=0
        cpu=0
        storage=0
        for i in range(self.getServicesNumber()):
            ram+=self.getService(i).getRam()
            cpu+=self.getService(i).getCpu()

            storage+=self.getService(i).getStorage()
        self.servicesCostCpu=cpu
        self.servicesCostRam=ram
        self.servicesCostStorage=storage
    def installService(self):
        text=str(self.getName())+" prepare install "+str(self.servicenumber)+" services"
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text)
        for index in range(self.servicenumber):
            data=self.edgeServicesConfigureData[index]
            service=Service(resourcerand=False,
                            initCpu=data[0],
                            initRam=data[1],
                            initStorage=data[2],
                            ratio=data[3]
                           ,textEdit=self.textEdit)
            if bool(1-self.addService(service)):
                break
        self.servicenumber=self.getServicesNumber()
        return True



EdgeServiceMigrationUI.py

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
                keys=line.split(" ")

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
                        Break
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

Graph_Matrix.py

import networkx as nx
import numpy as np
class Graph_Matrix:
def __init__(self, vertices=[],
 matrix=[]):
        self.matrix = matrix
        self.edges_dict = {}
        self.edges_array = []
        self.vertices = vertices
        self.num_edges = 0
        if len(matrix) > 0:
            if len(vertices) != len(matrix[0]):
                raise IndexError
            self.edges = self.getAllEdges()
            self.num_edges = len(self.edges)
        elif len(vertices) > 0:
            self.matrix = [[0 for col in range(len(vertices))] for row in range(len(vertices))]
        self.num_vertices = len(self.matrix)

    def isOutRange(self, x):
        try:
            if x >= self.num_vertices or x <= 0:
                raise IndexError
        except IndexError:
            print("节点下标出界")
    def isEmpty(self):
        if self.num_vertices == 0:
            self.num_vertices = len(self.matrix)
        return self.num_vertices == 0

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = len(self.vertices) + 1
        for i in range(self.getVerticesNumbers()):
            self.matrix[i].append(0)
        self.num_vertices += 1
        nRow = [0] * self.num_vertices
        self.matrix.append(nRow)

    def getVertex(self, key):
        pass
    def add_edges_from_list(self, edges_list):  # edges_list : [(tail, head, weight),()]
        for i in range(len(edges_list)):
            self.add_edge(edges_list[i][0], edges_list[i][1], edges_list[i][2], )
    def add_edge(self, tail, head, cost=0):
        if tail not in self.vertices:
            self.add_vertex(tail)
        if head not in self.vertices:
            self.add_vertex(head)
        self.matrix[self.vertices.index(tail)][self.vertices.index(head)] = cost
        self.edges_dict[(tail, head)] = cost
        self.edges_array.append((tail, head, cost))
        self.num_edges = len(self.edges_dict)
    def getEdges(self, V):
        pass
    def getVerticesNumbers(self):
        if self.num_vertices == 0:
            self.num_vertices = len(self.matrix)
        return self.num_vertices
    def getAllVertices(self):
        return self.vertices
def getAllEdges(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if 0 < self.matrix[i][j] < float('inf'):
                    self.edges_dict[self.vertices[i], 
self.vertices[j]] = self.matrix[i][j]
                    self.edges_array.append([self.vertices[i], self.vertices[j], self.matrix[i][j]])
        return self.edges_array
    def __repr__(self):
        return str(''.join(str(i) for i in self.matrix))
    def to_do_vertex(self, i):
        print('vertex: %s' % (self.vertices[i]))
    def to_do_edge(self, w, k):
        print('edge tail: %s, edge head: %s, weight: %s' % (self.vertices[w], self.vertices[k], str(self.matrix[w][k])))

LogsTextEditOutput.py
import sys
import os
import PySide2
from PySide2.QtWidgets import *

from PySide2 import QtCore, QtWidgets, QtGui
import random

import networkx
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

def LogsTextEditOutput(textEdit,text="",newline=True,newNumber=True):

    if not hasattr(LogsTextEditOutput,"lineNumber"):
        LogsTextEditOutput.lineNumber=0

    textEditCursor = textEdit.textCursor()
    textEditCursor.movePosition(QtGui.QTextCursor.End)
    if newNumber:
        if newline:
            textEditCursor.insertText("["+str("{:>8}".format(LogsTextEditOutput.lineNumber))+"] "+text+"\n")
        else:
            textEditCursor.insertText(text)
    else:
        if newline:
            textEditCursor.insertText("["+str("{:>8}".format(LogsTextEditOutput.lineNumber))+"] "+text)
        else:
            textEditCursor.insertText(text)

    LogsTextEditOutput.lineNumber+=1

    textEdit.setTextCursor(textEditCursor)
    textEdit.ensureCursorVisible()

main.py
import sys
from PySide2.QtWidgets import QApplication

from EdgeServiceMigrationUI import EdgeServiceMigrationUI
from MaximumFlow import MaximumFlow
import networkx as nx



from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash=QSplashScreen()
    pixmap=QtGui.QPixmap(QtGui.QImage("C:/Users/user/Desktop/monkey.png"))
    splash.setPixmap(pixmap)
    splash.show()

    mainWindow = EdgeServiceMigrationUI()
    w=1050
    h=350
    mainWindow.resize(w, h)
	mainWindow.setMaximumSize(w, h)

    mainWindow.setMinimumSize(w, h)

    mainWindow.show()
    splash.finish(mainWindow)
    sys.exit(app.exec_())

MaximumFlow.py

import networkx as nx
from Graph_Matrix import Graph_Matrix
class MaximumFlow:
def __init__(self,adjacencyMatrixData,nodesNumber=10):
        self.adjacencyMatrixData=adjacencyMatrixData
        self.nodesNumber=nodesNumber
        self.my_graph=Graph_Matrix(vertices=list(range(len(adjacencyMatrixData[0]))),matrix=adjacencyMatrixData) #vertices=[], matrix=[]
        self.created_graph=self.__create_undirected_matrix()
        self.G=self.__draw_undircted_graph()
    def __create_undirected_matrix(self):
        nodes=list(range(len(self.adjacencyMatrixData[0])))
        return Graph_Matrix(nodes,self.adjacencyMatrixData)
    def __draw_undircted_graph(self):
        graph=nx.Graph()
        for node in self.created_graph.vertices:
            graph.add_node(node)
        for edge in self.created_graph.edges:
            graph.add_edge(edge[0],edge[1],cost=6)
        return graph
    def value(self,source,target):
        graph=nx.Graph()
        for edge in self.G.edges():
            new_edge=(edge[0],edge[1],self.adjacencyMatrixData[edge[0]][edge[1]])
            graph.add_edge(new_edge[0],new_edge[1],capacity=new_edge[2])
        flow_value, flow_dict = nx.maximum_flow(graph, source, target)
        return flow_value

RandomStorageSize.py

import numpy as np
def RandomStorageSize():
	data=[233.0,30.8,110.0,54.7,77.3,103.0,44.6,83.2,97.7,170,230,4.78,4.73,506.0,507.0,527.0,548.0]
	data=[d/1024.0 for d in data]
    return np.random.choice(data,1).tolist()[0]

Service.py


import networkx as nx
import numpy as np
import random

import RandomStorageSize
from LogsTextEditOutput import LogsTextEditOutput
class Service:
    def __init__(self,resourcerand=True,initCpu=0.01,initRam=0.001,initStorage=0.004619140625,ratio=0.03,textEdit=""):
        self.textEdit=textEdit
        if resourcerand:
            self.initCpu=random.uniform(0.01,0.1)
            #self.initCpu=0.01
            self.cpu=self.initCpu
            self.initRam=random.uniform(0.001,0.03)
            #self.initRam=0.001
            self.ram=self.initRam
            self.initStorage=RandomStorageSize.RandomStorageSize()
            #self.initStorage=0.224609375
            #self.initStorage=0.004619140625
            self.storage=self.initStorage
            self.ratio=random.uniform(0.001,0.03)
            #self.ratio=0.03
        else:
            self.initCpu=initCpu
            #self.initCpu=0.01
            self.cpu=self.initCpu
            self.initRam=initRam
            #self.initRam=0.001
            self.ram=self.initRam
            self.initStorage=initStorage
            #self.initStorage=0.224609375
            #self.initStorage=0.004619140625
            self.storage=self.initStorage
            self.ratio=ratio

    def getRam(self):
        return self.ram
    def getCpu(self):
        return self.cpu
    def getStorage(self):
        return self.storage
    def getRatio(self):
		return self.ratio
    def update(self,costram,costcpu,coststorage,ram,cpu,storage):
         newram=self.initRam*self.getRatio()+costram
         newcpu=self.initCpu*self.getRatio()+costcpu
         newstorage=self.initStorage*self.getRatio()+coststorage
         if (newram<ram)and(newcpu<cpu)and(newstorage<storage):
             self.ram=self.getRam()+self.initRam*self.getRatio()

             self.cpu=self.getCpu()+self.initCpu*self.getRatio()
             self.storage=self.getStorage()+self.initStorage*self.getRatio()
             return True
         else:
             self.ram=self.getRam()+ram-costram

             self.cpu=self.getCpu()+cpu-costcpu
             self.storage=self.getStorage()+storage-coststorage
             return False
    def logs(self):
        text="Cpu:"+str(self.getCpu())+"\tRam:"+str(self.getRam())+"\tStorage:"+str(self.getStorage())
        #print(text)
        LogsTextEditOutput(self.textEdit,text=text,newline=False)
        return True

