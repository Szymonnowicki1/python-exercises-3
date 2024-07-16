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

# %%
import time

# %%
def finish(fun, arg, hmt = 1):
    sum = 0
    for i in range(0, hmt):
        start = time.perf_counter()
        fun(arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum
# %%
print(finish(sumuj_do1, 1000000, 25 ))

# %%
zbior = {x for x in range(100)}

def czy_wartosc_jest(wartosc):
    if wartosc in zbior:
        return True
    else:
        return False

print(finish(czy_wartosc_jest, 48,)



















    