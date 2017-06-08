# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 14:53:57 2017

@author: u6035034
"""

import baseSquare as bs


if __name__ == "__main__":
    one =bs.baseSquare()
    a=[1,2,3,4,5,6,7,8]
    one.removePossibleValue(a)
    print one.getPossibleValue()
    print one.getValue()