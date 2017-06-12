# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:55:23 2017

@author: chen
"""

import baseSquare as bs
import nineBaseSquare as nbs
import copy

class Sudo(object):
    def __init__(self):
        self.basesquare = [[] for h in range(9)]
        self.rowsquare = []
        self.colunmsquare=[]
        self.blocksquare=[]
        self.initNineSqaure()
        self.basecount=0
        self.count =0

    def initNineSqaure(self):
        for i in range(9):
            row=nbs.rowSqaure()
            self.rowsquare.append(row)
            
            column=nbs.columnSquare()
            self.colunmsquare.append(column)
            
            block=nbs.blockSquare()
            self.blocksquare.append(block)
    def initSuDu(self,filename):
        f=open(filename,'r')
        i=0
        for line in f.readlines():
            numbers=line.split(',')
            j=0
            for n in numbers:
                one=bs.baseSquare()
                v=int(n)
                blocknum=j/3+(i/3)*3
                one.setPosition((i+1,j+1))
                posvalue={}
                if(v!=0):
                    one.setValue(v)
                    self.rowsquare[i].addPossibleValue(v)
                    self.colunmsquare[j].addPossibleValue(v)
                    self.blocksquare[blocknum].addPossibleValue(v)
                    self.count=self.count+1
                    self.basecount =self.basecount+1
                else:
                    posvalue=copy.copy(self.rowsquare[i].getPossibleValue())
                    posvalue.update(self.colunmsquare[j].getPossibleValue())
                    posvalue.update(self.blocksquare[blocknum].getPossibleValue())
                    one.delPossibleValue(posvalue.keys())
                    #value=one.updatePossibleValue()
    #                if(i == j):
    #                    biassquare[0].addPossibleValue(v)
    #                elif(8== (i+j)):
    #                    biassquare[1].addPossibleValue(v)
                j=j+1
                self.basesquare[i].append(one)
            i=i+1
            
        self.printResult()
        self.printNineSquare(self.rowsquare)
        self.printNineSquare(self.colunmsquare)
        self.printNineSquare(self.blocksquare)
        self.printInfo()
    def startGame(self):
        time=0
        run=2
        while(run):
            run=run-1
            if(self.count >self.basecount):
                run=1
            time=time+1
            self.basecount=self.count
            self.checkPossibleValue()
            print "run %d times, the base is %d, now numbers is %d"%(time,self.basecount,self.count)

    def checkPossibleValue(self):
        for i in range(9):
            for j in range(9):
                v=self.basesquare[i][j].getValue()
                blocknum=j/3+(i/3)*3
                pvs=self.rowsquare[2].getPossibleValue()
                posvalue={}
                if(v!=0):
                    self.rowsquare[i].addPossibleValue(v)
                    self.colunmsquare[j].addPossibleValue(v)
                    self.blocksquare[blocknum].addPossibleValue(v)
                else:
                    posvalue=copy.copy(self.rowsquare[i].getPossibleValue())
                    posvalue.update(self.colunmsquare[j].getPossibleValue())
                    posvalue.update(self.blocksquare[blocknum].getPossibleValue())
                    self.basesquare[i][j].delPossibleValue(posvalue.keys())
                    value=self.basesquare[i][j].updatePossibleValue()
                    if(value!=0):
                        print (i,j)
                        self.count=self.count+1
                        print self.rowsquare[i].getPossibleValue()
                        print self.colunmsquare[j].getPossibleValue()
                        print self.blocksquare[blocknum].getPossibleValue()
                        print posvalue
                        self.rowsquare[i].addPossibleValue(value)
                        self.colunmsquare[j].addPossibleValue(value)
                        self.blocksquare[blocknum].addPossibleValue(value)
                        print "get a number"                   
                    else:
                        posv=self.ExculdeNumber(i,j)
                        if(len(posv)==1):
                            print posv
                            print (i,j)
                            print "exculde a number"
    def printInfo(self):
        self.printResult()
        print "the base is %d, now numbers is %d"%(self.basecount,self.count)
    def printResult(self):
        for lsquare in self.basesquare:
            line=""
            for j in lsquare:
                line=line+ "%d,"%(j.getValue())
            print line
    def printNineSquare(self,ninesquare):
        for r in ninesquare:
            r.printPossibleValue()
    
    def printCount(self):
        print "Now sudo has filled %d numbers"%self.count
    def ExculdeNumber(self,i,j):
        (r1,r2)=self.caculateNumber(i)
        (c1,c2)=self.caculateNumber(j)
#        print (r1,r2)
#        print "caculate number"
#        print (c1,c2)
        colposvalue={}
        rowposvalue={}
        for k in self.rowsquare[r1].getPossibleValue().keys():
            if(k in self.rowsquare[r2].getPossibleValue().keys()):
                rowposvalue.update({k:1})
        for k in self.colunmsquare[c1].getPossibleValue().keys():
            if(k in self.colunmsquare[c2].getPossibleValue().keys()):
                colposvalue.update({k:1})
        for k in rowposvalue.keys():
            if(k not in colposvalue.keys()):
                rowposvalue.pop(k)
        return rowposvalue
        
    def caculateNumber(self,m):
        v=m%3
        if(v==0):
            return(m+1,m+2)
        elif(v==1):
            return(m-1,m+1)
        elif(v==2):
            return(m-2,m-1)
        