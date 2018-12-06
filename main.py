# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 14:53:57 2017

@author: u6035034
"""
import Sudo as sd
from datetime import datetime
import sys

if __name__ == "__main__":
    filename=sys.argv[1]
    #filename="example009.csv"
    mysd = sd.Sudo()
    starttime=datetime.now()
    mysd.initSuDu(filename)
    print mysd.colunmsquare[8].getPossibleValue()
    mysd.startGame()
    mysd.printInfo()
    mysd.printPosValue()
    mysd.printNineSquare(mysd.blocksquare)
    endtime=datetime.now()
    print "this sudo use "
    print (endtime - starttime)