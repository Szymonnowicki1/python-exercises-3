# -*- coding: utf-8 -*-

def sumuj_do1(liczba):
    x = sum([liczba for liczba in range(liczba + 1)])
    return(x)

print(sumuj_do1(5))

# %%
def sumuj_do2(liczba):
    return (1 + liczba) / 2 * liczba

print(sumuj_do2(5))

# %%

def sumuj_do3(liczba):
    suma = 0
    for liczba in range(1, liczba + 1):
        suma += liczba
    return suma
        
print(sumuj_do3(5))