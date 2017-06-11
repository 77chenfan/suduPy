# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 14:53:57 2017

@author: u6035034
"""
import Sudo as sd

if __name__ == "__main__":
    mysd = sd.Sudo()    
    mysd.initSuDu("example001.csv")
    print mysd.rowsquare[0].getPossibleValue()
    mysd.startGame()
    mysd.printInfo()
