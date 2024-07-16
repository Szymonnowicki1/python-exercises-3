# -*- coding: utf-8 -*-

zbior = {x for x in range(100)}

def czy_wartosc_jest(wartosc):
    if wartosc in zbior:
        return True
    else:
        return False

print(finish(czy_wartosc_jest, 48, 3)

def finish(fun, arg, hmt = 1):
    sum = 0
    for i in range(0, hmt):
        start = time.perf_counter()
        fun(arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum