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
