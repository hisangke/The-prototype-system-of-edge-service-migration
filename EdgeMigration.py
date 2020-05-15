from Service import Service
import time
import random
from MaximumFlow import MaximumFlow
from EdgeNode import EdgeNode
adjacencyMatrixData=[[0.0, 0.0, 0.0, 0.0, 37.5, 0.0, 0.0, 0.0, 0.0, 0.0],
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
            edgeNode=EdgeNode(name=edgeNodeName,
                                    servicenumber=len(self.edgeServicesConfigureData[i]),
                                    cpu=data[0],
                                    ram=data[1],
                                    storage=data[2],
                                    threshold=data[3],
                                    edgeServicesConfigureData=self.edgeServicesConfigureData[i],
                                    textEdit=self.textEdit
                                    )
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










