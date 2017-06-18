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
        self.poy = y
    def setPosition(self,p):
        (x,y)=p
        self.setPox(x)
        self.setPoy(y)    
    def getPos(self):
        return (self.pox,self.poy)  
    def addPossibleValue(self,ps):
        if(type(ps)==list):
            for k in ps:
                assert (k<10 and k>0), "please add number between 1 to 9"
                self.possibleValue.update({k:1})
        elif(type(ps)== int):
            assert (ps<10 and ps>0), "please add number between 1 to 9"
            self.possibleValue.update({ps:1})
    def delPossibleValue(self,ps):
        if(type(ps)==list):
            for k in ps:
                assert (k<10 and k>0), "please del number between 1 to 9"
                #self.possibleValue.update({k:0})
                if( k in self.possibleValue.keys()):
                    self.possibleValue.pop(k)
        elif(type(ps)== int):
            assert (ps<10 and ps>0), "please del number between 1 to 9"
            #self.possibleValue.update({ps:0})
            if( k in self.possibleValue.keys()):            
                self.possibleValue.pop(k)
    def removePossibleValue(self,ps):
        if(type(ps)==list):
            for i in ps:
                self.possibleValue.pop(i)
        elif(type(ps)== int):
            self.possibleValue.pop(ps)
    def setPossibleValue(self):
        self.possibleValue={self.value:1}
    def getPossibleValue(self):
        return self.possibleValue
            

    def isFinish(self):
        return (self.getValue() != 0)
    def printPossibleValue(self):
        print self.possibleValue.keys()