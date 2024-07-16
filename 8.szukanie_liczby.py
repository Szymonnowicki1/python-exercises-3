# -*- coding: utf-8 -*-

szukanaLiczba = 10
zgadywanaLiczba = 0

while szukanaLiczba != zgadywanaLiczba:
    zgadywanaLiczba = int(input('Zgadnij liczbe : '))
    if szukanaLiczba < zgadywanaLiczba:
       print('Za duza liczba')
    elif szukanaLiczba > zgadywanaLiczba:
        print('Za mala liczba')
    else:
        print('DOBRZE')