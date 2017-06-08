# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 13:47:09 2017

@author: u6035034
"""

class square(object):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
    def setValue(self,v):
        self.value=v
    def getValue(self):
        return self.value
    def setPox(self,x):
        self.pox = x
    def setPoy(self,y):
        self.pox = y
    def setPosition(self,p):
        (x,y)=p
        self.setPox(x)
        self.setPoy(y)    
    def getPos(self):
        return (self.pox,self.poy)  
    def updatePossibleValue(self,ps):
        for k in ps.keys:
            assert (k<10 and k>0),"please set number between 1 to 9"
            assert (ps[k]==0 or ps[k]==1), "value only support 1 or 0"
        self.possibleValue.update(ps)
        self.__updatePossibleValue()
    def removePossibleValue(self,ps):
        if(type(ps)==list):
            for i in ps:
                self.possibleValue.pop(i)
        elif(type(ps)== int):
            self.possibleValue.pop(ps)
    def __updatePossibleValue(self):
        for p in self.possibleValue:
            if(self.possibleValue[p]==0):
                self.possibleValue.pop(p)
        if(len(self.possibleValue)==1):
            v=self.possibleValue.keys()
            self.setValue(v.pop())
    def getPossibleValue(self):
        self.__updatePossibleValue()
        return self.possibleValue
            

    def isFinish(self):
        return (self.getValue() != 0)