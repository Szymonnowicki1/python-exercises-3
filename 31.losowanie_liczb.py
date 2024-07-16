# -*- coding: utf-8 -*-
import random

def willweaponhit(weaponchancestohit):
    x = random.randrange(0, 101)
    if x < weaponchancestohit:
        return 'hit'
    else:
        return 'not hit'
    
print(willweaponhit(50))\

# %%
x = 0
lista = []
while x < 20:
    x = x + 1
    lista.append(willweaponhit(80))
    
print(lista.count('hit'))
    
