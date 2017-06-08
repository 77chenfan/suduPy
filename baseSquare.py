# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 11:38:22 2017

@author: u6035034
"""    
        
import square as sq

class baseSquare(sq.square):
    def setValue(self,v):
        assert (v<10 and v>0),"please set a number between 1-9"
        self.value = v
    def setPox(self,x):
        assert (x<10 and x>0),"set pox need between 1-9"
        self.pox = x
    def setPoy(self,y):
        assert (y<10 and y>0),"set poy need between 1-9"
        self.pox = y
        












