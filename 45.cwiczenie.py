# -*- coding: utf-8 

def otwieranie_pliku(plik):
    try:
        with open(plik , 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('error')
        
x = input('jaki plik otworzyc?')


y = otwieranie_pliku(x)
