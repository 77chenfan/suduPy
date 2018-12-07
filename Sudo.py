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
                    one.setPossibleValue()
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
                self.basesquare[i].append(one)
                self.rowsquare[i].addBaseSquare(one)
                self.colunmsquare[j].addBaseSquare(one)
                self.blocksquare[blocknum].addBaseSquare(one)
                self.rowsquare[i].setPox(i+1)
                self.colunmsquare[j].setPoy(j+1)
                self.blocksquare[blocknum].setPox(blocknum+1)
                self.blocksquare[blocknum].setPoy(blocknum+1)
                j=j+1
            i=i+1
            
        #self.printResult()
        #self.printNineSquare(self.rowsquare)
        #self.printNineSquare(self.colunmsquare)
        #self.printNineSquare(self.blocksquare)
        self.printInfo()
    def startGame(self):
        time=0
        run=2
        while(run):
            run=run-1
            time=time+1
            self.basecount=self.count
            self.checkPossibleValue()
            if(self.count >self.basecount):
                run=run+1
            print "run %d times, the base is %d, now numbers is %d"%(time,self.basecount,self.count)

    def checkPossibleValue(self):
        for i in range(9):
            for j in range(9):
                v=self.basesquare[i][j].getValue()
                blocknum=j/3+(i/3)*3
                posvalue={}
                if(v!=0):
                    self.rowsquare[i].addPossibleValue(v)
                    self.colunmsquare[j].addPossibleValue(v)
                    self.blocksquare[blocknum].addPossibleValue(v)
                else:
                    rowPoss=copy.copy(self.rowsquare[i].getPossibleValue())
                    columnPoss=copy.copy(self.colunmsquare[j].getPossibleValue())
                    blockPoss=copy.copy(self.blocksquare[blocknum].getPossibleValue())
                    
                    posvalue.update(rowPoss)
                    posvalue.update(columnPoss)
                    posvalue.update(blockPoss)
                    self.basesquare[i][j].delPossibleValue(posvalue.keys())
                    value=self.basesquare[i][j].updatePossibleValue()
                    if(value!=0):
                        print (i,j)
                        self.count=self.count+1
#                        print self.rowsquare[i].getPossibleValue()
#                        print self.colunmsquare[j].getPossibleValue()
#                        print self.blocksquare[blocknum].getPossibleValue()
#                        print posvalue
                        self.rowsquare[i].addPossibleValue(value)
                        self.colunmsquare[j].addPossibleValue(value)
                        self.blocksquare[blocknum].addPossibleValue(value)
                        print "get a number"
                    else:
                        oneSquare =self.basesquare[i][j]
                        #print "start to update value"
                        #self.rowsquare[i].updateStillNeedValue(oneSquare)
                        #self.colunmsquare[j].updateStillNeedValue(oneSquare)
                        #self.blocksquare[blocknum].updateStillNeedValue(oneSquare)
                        sb=self.scanNineBlocks("block",i,j)
                        if(sb==0):
                            sb=self.scanNineBlocks("row",i,j)
                        if(sb==0):
                            sb=self.scanNineBlocks("colunm",i,j)
#                        sb=self.blocksquare[blocknum].Excludenumber((i%3)*3+j%3)
#                        if(sb==0):
#                            sb=self.rowsquare[i].Excludenumber(j)
#                        if(sb==0):
#                            sb=self.colunmsquare[j].Excludenumber(i)
                        self.count=self.count+sb
    def scanNineBlocks(self,tp,i,j):
        if(tp == "block"):
            nineSquare=self.blocksquare[j/3+(i/3)*3]
            num=(i%3)*3+j%3
        elif(tp == "row"):
            nineSquare=self.rowsquare[i]
            num=j
        elif(tp == "colunm"):
            nineSquare=self.colunmsquare[j]
            num=i
        pos1=nineSquare.squares[num].getPossibleValue()
        lenpos1=len(pos1)
        if(lenpos1 > 0 ):
            findXor=[]
            pos2={}
            posStat=nbs.keyList()
            for n in range(9):
                tempos={}
                tempos=nineSquare.squares[n].getPossibleValue()
                for k in tempos:
                    if(posStat.haskey(k)):
                        v=posStat.get(k)
                        v.add(n)
                        #posStat.update({k:v})
                    else:
                        v= nbs.keyEle(k)
                        v.add(n)
                        posStat.add(v)
                if(n!=num):
                    #find keys are the same and clean other block
                    if(pos1.keys()==tempos.keys()):
                        print "find the same pos"
                        findXor.append(n)
                        
                    pos2.update(tempos)
            nineSquare.stillNeedValue = self.judeNineSquare(posStat)
            fixvalues= self.findSameEle(nineSquare.stillNeedValue)
            self.processFixValues(nineSquare,fixvalues)
            
            c=0
            for k in pos1.keys():
                if k not in pos2.keys():
                    c=c+1
                    print "find a exclude number"
                    nineSquare.squares[num].setValue(k)
                    nineSquare.squares[num].setPossibleValue()
                    self.rowsquare[i].addPossibleValue(k)
                    self.colunmsquare[j].addPossibleValue(k)
                    self.blocksquare[j/3+(i/3)*3].addPossibleValue(k)
                    return 1
            #clean the other block when x blocks has the same x number
            if(findXor != [] and len(findXor) == lenpos1-1):
                for n in range(9):
                    if(n not in findXor and n !=num):
                        nineSquare.squares[n].delPossibleValue(pos1.keys())
                if(len(findXor)==1):
                    x=nineSquare.squares[findXor[0]].pox
                    y=nineSquare.squares[findXor[0]].poy
                    if(x == i+1):
                        if(tp == 'block'):
                            for n in range(9):
                                if(n !=y-1 and n !=j):
                                    self.rowsquare[i].squares[n].delPossibleValue(pos1.keys())
                        if(tp == 'row' and j/3 == (y-1)/3):
                            for n in range(9):
                                if(n !=((x-1)%3)*3+(y-1)%3 and n !=(i%3)*3+j%3):
                                    self.blocksquare[j/3+(i/3)*3].squares[n].delPossibleValue(pos1.keys())
                    if(y == j+1):
                        if(tp == 'block'):
                            for n in range(9):
                                if(n !=x-1 and n != i):
                                    self.colunmsquare[j].squares[n].delPossibleValue(pos1.keys())
                        if(tp == 'colunm' and i/3 == (x-1)/3):
                            for n in range(9):
                                if(n !=((x-1)%3)*3+(y-1)%3 and n !=(i%3)*3+j%3):
                                    self.blocksquare[j/3+(i/3)*3].squares[n].delPossibleValue(pos1.keys())                   
    
                if(len(findXor) == 2):
                    x=nineSquare.squares[findXor[0]].pox
                    y=nineSquare.squares[findXor[0]].poy
                    x1=nineSquare.squares[findXor[1]].pox
                    y1=nineSquare.squares[findXor[1]].poy
                    if(x == i+1 and x1 == i+1):
                        if(tp == 'block'):
                            for n in range(9):
                                if(n !=y-1 and n !=j and n!= y1-1):
                                    self.rowsquare[i].squares[n].delPossibleValue(pos1.keys())
                        if(tp == 'row' and j/3 == (y-1)/3 and j/3 == (y1-1)/3):
                            for n in range(9):
                                if(n !=((x-1)%3)*3+(y-1)%3 and n !=(i%3)*3+j%3 and n!=((x1-1)%3)*3+(y1-1)%3):
                                    self.blocksquare[j/3+(i/3)*3].squares[n].delPossibleValue(pos1.keys())
                    if(y == j+1 and y1 == j+1):
                        if(tp == 'block'):
                            for n in range(9):
                                if(n !=x-1 and n != i and n!= x1-1):
                                    self.colunmsquare[j].squares[n].delPossibleValue(pos1.keys())
                        if(tp == 'colunm' and i/3 == (x-1)/3 and i/3 == (x1-1)/3):
                            for n in range(9):
                                if(n !=((x-1)%3)*3+(y-1)%3 and n !=(i%3)*3+j%3 and n!=(x1-1)%3*3 +(y1-1)%3):
                                    self.blocksquare[j/3+(i/3)*3].squares[n].delPossibleValue(pos1.keys())                   

                
        return 0
    def judeNineSquare(self,posStat):
        #define a threshold
        threshold = posStat.size/2
        tStat = posStat.getElesByThreshold(threshold)
        return tStat
        
    def printInfo(self):
        self.printResult()
        print "the base is %d, now numbers is %d"%(self.basecount,self.count)
    def printResult(self):
        for lsquare in self.basesquare:
            line=""
            for j in lsquare:
                v = j.getValue()
                line=line+ "%d,"%(v)
            print line
    def printPosValue(self):
        for lsquare in self.basesquare:
            for j in lsquare:
                v = j.getValue()
                if(v == 0):
                    print "the number is %s, and pos value is %s"%(str(j.getPos()),str(j.getPossibleValue().keys()))
    def printNineSquare(self,ninesquare):
        for r in ninesquare:
            #r.printPossibleValue()
            r.printStillNeedValue()
    
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
        
    def findSameEle(self,kl):
        result={}
        sumkeydict={}
        for ele in kl.keylist.values():
            if(sumkeydict.has_key(ele.sum)):
                v = sumkeydict.get(ele.sum)
                v.append(ele)
                sumkeydict.update({ele.sum:v})
            else:
                sumkeydict.update({ele.sum:[ele]})
        for ele in sumkeydict.values():
            if(len(ele) == 2 and ele[0].isSameVaule(ele[1]) and ele[0].size == 2):
                result.update({ele[0].sum:ele})
        return result
    def processFixValues(self,nineSquare,eleDict):
        for eleList in eleDict.values():
            print "the process fix value %s at %s"%(str(eleList),str(nineSquare.getPos()))
            if(len(eleList) == 2 and eleList[0].size == 2):
                k1=eleList[0].key
                k2=eleList[1].key
                sq1=nineSquare.squares[eleList[0].value[0]]
                sq2=nineSquare.squares[eleList[0].value[1]]
                sq1.setPossibleValue()
                sq1.addPossibleValue([k1,k2])
                sq2.setPossibleValue()
                sq2.addPossibleValue([k1,k2])
                if(sq1.pox == sq2.pox):
                    for n in range(9):
                        if(n!=sq1.poy-1 and n!=sq2.poy-1):
                            self.rowsquare[sq1.pox-1].squares[n].delPossibleValue([k1,k2])
                        if((sq1.poy-1)/3== (sq2.poy-1)/3 and  n !=((sq1.pox-1)%3)*3+(sq1.poy-1)%3 and n!=((sq2.pox-1)%3)*3+(sq2.poy-1)%3):
                            self.blocksquare[(sq1.poy-1)/3+((sq1.pox-1)/3)*3].squares[n].delPossibleValue([k1,k2])
                elif(sq1.poy == sq2.poy):
                   for n in range(9):
                        if(n!=sq1.pox-1 and n!=sq2.pox-1):
                           self.colunmsquare[sq1.poy-1].squares[n].delPossibleValue([k1,k2])
                        if((sq1.pox-1)/3 == (sq2.pox-1)/3 and  n !=((sq1.pox-1)%3)*3+(sq1.poy-1)%3 and n!=((sq2.pox-1)%3)*3+(sq2.poy-1)%3):
                            self.blocksquare[(sq1.poy-1)/3+((sq1.pox-1)/3)*3].squares[n].delPossibleValue([k1,k2])


                    
            