# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:32:01 2017

@author: chen
"""
import square as sq

class columnSquare(sq.square):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={}
    def getPox(self):
        return self.pox

class rowSqaure(sq.square):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={}
    def getPox(self):
        return self.pox


class blockSquare(sq.square):
    def __init__(self):
        self.value=0
        self.pox=0
        self.poy=0
        self.possibleValue={}
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