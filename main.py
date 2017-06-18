# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 14:53:57 2017

@author: u6035034
"""
import Sudo as sd
from datetime import datetime

if __name__ == "__main__":
    mysd = sd.Sudo()
    starttime=datetime.now()
    mysd.initSuDu("example008.csv")
    print mysd.colunmsquare[8].getPossibleValue()
    mysd.startGame()
    mysd.printInfo()
    endtime=datetime.now()
    print "this sudo use "
    print (endtime - starttime)