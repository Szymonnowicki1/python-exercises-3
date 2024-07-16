# -*- coding: utf-8 -*-
import random

def findprzyblizonavalue(value):
    lowestvalue = value - 0.1 * value
    highestvalue = value + 0.1 * value
    return(random.randint(lowestvalue, highestvalue))

print(findprzyblizonavalue(2000))