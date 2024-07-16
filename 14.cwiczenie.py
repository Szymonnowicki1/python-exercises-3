# -*- coding: utf-8 -*-

slownik = {}

# %%
while(True):
    w = int(input('''Czesc, wybierz liczbe:
                  1 zeby dodac definicje
                  2 zeby wyszukac definicje
                  3 zeby usunac definicje
                  4 zeby zakonczyc program'''))
                  
    
    if w == 1:
        klucz = input('Podaj slowo do zdefiniowania :')
        definicja = input('Podaj definicje :')
        slownik[klucz] = definicja
    elif w == 2:
        klucz = input('Czego szukasz ?')
        if klucz in slownik:
            print(slownik[klucz])
        else:
            print('nie znaleziono defnicji o nazwie', klucz)
    elif w == 3:
        klucz = input('Jaka definicje usunac?')
        if klucz in slownik:
            del slownik[klucz]
        else:
            print('Nie ma takiej definicji')
    elif w == 4:
        print('Dzieki, zamykamy program')
        break