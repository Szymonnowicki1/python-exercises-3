# -*- coding: utf-8 -*-

with open('oceany.txt', 'r') as plik:
    print(plik.readline())
    print(plik.readline())
    print(plik.tell())
    print(plik.readline())
    print(plik.readline())
    plik.seek(5)