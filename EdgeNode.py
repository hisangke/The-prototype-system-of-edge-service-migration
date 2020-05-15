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
