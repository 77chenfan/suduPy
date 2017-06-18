# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:32:01 2017

@author: chen
"""
import square as sq

class comNineSquare(sq.square):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={}
        self.squares=[]  # add nine basesquares
    def getPox(self):
        return self.pox 
    def addBaseSquare(self, bs):
        self.squares.append(bs)
    def updateBaseSquare(self,index,bs):
        self.squares[index]=bs
    def Excludenumber(self,i):
        pos1=self.squares[i].getPossibleValue()
        lenpos1=len(pos1)
        findXor=10
        pos2={}
        for n in range(9):
            tempos={}
            if(n!=i):
                tempos=self.squares[n].getPossibleValue()
                if(lenpos1==2 and pos1.keys()==tempos.keys()):
                    print "find the same pos"
                    findXor=n
                    
                pos2.update(tempos)
        c=0
        for k in pos1.keys():
            if k not in pos2.keys():
                c=c+1
                print "find a exclude number"
                self.squares[i].setValue(k)
                self.squares[i].setPossibleValue()
                return 1
        if(findXor != 10):
            for n in range(9):
                if(n != findXor and n !=i):
                    self.squares[n].delPossibleValue(pos1.keys())
                
        return 0
class columnSquare(comNineSquare):
    def getPox(self):
        return self.pox

class rowSqaure(comNineSquare):
    def addBaseSquare(self, bs):
        self.squares.append(bs)
    def updateBaseSquare(self,index,bs):
        self.squares[index]=bs
    def getPox(self):
        return self.pox


class blockSquare(comNineSquare):
    def getPox(self):
        return self.pox
        

class biasSquare(sq.square):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={}
    def getPox(self):
        return self.pox