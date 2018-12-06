# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:32:01 2017

@author: chen
"""
#import square as sq
import baseSquare as basesquare

class keyEle():
    def __init__(self,key):
        self.key = key
        self.value=[]
        self.size=0
        self.sum=0
    def __str__(self):
        return str(self.value)
    def add(self,ele):
        self.value.append(ele)
        self.size +=1
        self.sum +=ele
    def isSameVaule(self,other):
        return(self.size == other.size and self.value == other.value)
        
    __repr__ = __str__

class keyList():
    def __init__(self):
        self.keylist = {}
        self.size = 0
    def __str__(self):
        return str(self.keylist)
    def add(self,ele):
        self.keylist.update({ele.key:ele})
        self.size += 1
    def get(self,key):
        return self.keylist.get(key)
    def haskey(self,key):
        return self.keylist.has_key(key)
    def setThresHold(self,threshold):
        self.threshold = threshold
    def getElesByThreshold(self,threshold):
        result=keyList()
        for k in self.keylist:
            if(self.keylist.get(k).size <= threshold):
                result.add(self.keylist.get(k))
        return result
                
                
            
            
        

class comNineSquare(basesquare.baseSquare):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={}
        #default all places have value
        self.stillNeedValue={}
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
        findXor=[]
        pos2={}
        for n in range(9):
            tempos={}
            if(n!=i):
                tempos=self.squares[n].getPossibleValue()
                #find keys are the same and clean other block
                if(pos1.keys()==tempos.keys()):
                    print "find the same pos"
                    findXor.append(n)
                    
                pos2.update(tempos)
        c=0
        for k in pos1.keys():
            if k not in pos2.keys():
                c=c+1
                print "find a exclude number"
                self.squares[i].setValue(k)
                self.squares[i].setPossibleValue()
                return 1
        #clean the other block when x blocks has the same x number
        if(findXor != [] and len(findXor) == lenpos1-1):
            for n in range(9):
                if(n not in findXor and n !=i):
                    self.squares[n].delPossibleValue(pos1.keys())                
        return 0
    def updateStillNeedValue(self,ps):
        if(isinstance(ps,int)):
            #not still need
            self.stillNeedValue.update({ps:0})
        elif(isinstance(ps,list)):
            for k in ps:
                self.stillNeedValue.update({k:0})
        elif(isinstance(ps,dict)):
            self.stillNeedValue.update(ps)
            
    def addPossibleValue(self,ps):
        super(comNineSquare,self).addPossibleValue(ps)
        #self.updateStillNeedValue(ps)
        
    def printStillNeedValue(self):
        print self.stillNeedValue
class columnSquare(comNineSquare):
    def getPox(self):
        return self.pox
    def updateStillNeedValue(self,ps):
        super(columnSquare,self).updateStillNeedValue(ps)
        if(isinstance(ps,basesquare.baseSquare)):
            posValue = ps.getPossibleValue().keys()
            n=ps.pox
            for k in range(10):
                if(k==0):
                    continue
                if(k in posValue):
                    v=self.stillNeedValue.get(k)&(511-pow(2,n))
                    self.stillNeedValue.update({k:v})
                else:
                    v=self.stillNeedValue.get(k)|pow(2,n)
                    self.stillNeedValue.update({k:v})

class rowSqaure(comNineSquare):
    def addBaseSquare(self, bs):
        self.squares.append(bs)
    def updateBaseSquare(self,index,bs):
        self.squares[index]=bs
    def getPox(self):
        return self.pox
    def updateStillNeedValue(self,ps):
        super(rowSqaure,self).updateStillNeedValue(ps)
        if(isinstance(ps,basesquare.baseSquare)):
            posValue = ps.getPossibleValue().keys()
            n=ps.poy
            for k in range(10):
                if(k==0):
                    continue
                if(k in posValue):
                    v=self.stillNeedValue.get(k)&(511-pow(2,n))
                    self.stillNeedValue.update({k:v})
                else:
                    v=self.stillNeedValue.get(k)|pow(2,n)
                    self.stillNeedValue.update({k:v})
        print str(self.stillNeedValue)
        


class blockSquare(comNineSquare):
    def getPox(self):
        return self.pox
    def updateStillNeedValue(self,ps):
        super(blockSquare,self).updateStillNeedValue(ps)
        if(isinstance(ps,basesquare.baseSquare)):
            posValue = ps.getPossibleValue().keys()
            n=(ps.poy%3)+(ps.pox%3)*3
            for k in range(10):
                if(k==0):
                    continue
                if(k in posValue):
                    v=self.stillNeedValue.get(k)&(511-pow(2,n))
                    self.stillNeedValue.update({k:v})
                else:
                    v=self.stillNeedValue.get(k)|pow(2,n)
                    self.stillNeedValue.update({k:v})
        

class biasSquare(basesquare.baseSquare):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={}
    def getPox(self):
        return self.pox