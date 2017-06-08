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
        self.possibleValue=[1,2,3,4,5,6,7,8,9]
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
    def addPossibleValue(self,p):
        self.possibleValue.append(p)
    
    def removePossibleValue(self,p):
        self.possibleValue.remove(p)
        assert self.possibleValue.count >0, "possible value is empty, failed"
        if(self.possibleValue.count ==1):
            self.value = self.possibleValue.pop
    def getPossibleValue(self):
        return self.possibleValue

    def isFinish(self):
        return (self.getValue() != 0)