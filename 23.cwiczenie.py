# -*- coding: utf-8 -*-

import math

from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'prostokat kwadrat trojkat trapez kolo')




print('''Program liczacy pole figur''')
wybor = int(input('''Wybierz figure : 
1 prostokąt
2 kwadrat
3 trojkat
4 trapez
5 kolo 
'''))

if wybor == Menu_Figury.prostokat:
    a = int(input('Podaj dlugosc pierwszego boku :'))
    b = int(input('Podaj dlugosc drugiego boku : '))
    print(poleProstokata(a, b))
    
elif wybor == Menu_Figury.kwadrat:
    a = int(input('Podaj dlugosc boku : '))
    print(poleKwadratu(a))
    
elif wybor == Menu_Figury.trojkat:
    a = int(input('Podaj dlugosc boku : '))
    h = int(input('Podaj wysokosc : '))
    print(poleTrojkata(a, h))
    
elif wybor == Menu_Figury.trapez:
    a = int(input('Podaj dlugosc pierwszego boku :'))
    b = int(input('Podaj dlugosc drugiego boku :'))
    h = int(input('Podaj wysokosc : '))
    print(poleTrapzeu(a, b, h))

elif wybor == Menu_Figury.kolo:
    r = int(input('Podaj dlugosc promienia : '))
    print(poleKola(r))

def poleProstokata(a, b):
    return a * b

def poleKwadratu(a):
    return a ** 2

def poleTrojkata(a, h):
    return (a * h) / 2

def poleTrapzeu(a, b, h):
    return (a + b) * h / 2

def poleKola(r):
    return math.pi * r **2





















