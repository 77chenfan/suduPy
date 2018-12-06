# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 11:38:22 2017

@author: u6035034
"""    
        
import square as sq


class baseSquare(sq.square):
    def setValue(self,v):
        assert (v<10 and v>0),"please set a number between 1-9,the input is %d"%v
        self.value = v
    def setPox(self,x):
        assert (x<10 and x>0),"set pox need between 1-9,the input is %d"%x
        self.pox = x
    def setPoy(self,y):
        assert (y<10 and y>0),"set poy need between 1-9,the input is %d"%y
        self.poy = y
    def updatePossibleValue(self):
        pv=0
        v=0
        for p in self.possibleValue.keys():
            if(self.possibleValue[p]==1):
                pv=pv+1
                v=p
        if(pv==1):
            print self.possibleValue
            print self.getPos()
            print v
            self.setValue(v)
            self.setPossibleValue()
            return v
        else:
            return 0

    def getPossibleValue(self):
        return self.possibleValue
    def getValue(self):
        #self.__updatePossibleValue()
        return self.value









