# -*- coding: utf-8 -*-
import random

def losuje_6_liczb_z_49(ilosc_losowanych_liczb, wszystkie_liczby):
    x = 0
    while x < 6:
        x = x + 1
        print(random.randint(0, wszystkie_liczby))
    

losuje_6_liczb_z_49(6, 49)

# %%
def losowanie(ilosclosowanychliczb, wszystkieliczby):
    print(random.sample(range(wszystkieliczby), ilosclosowanychliczb))
    
losowanie(6, 49)

# %%
import random

def choose_random_numbers(amount, total_amount):
    print(random.sample(range(1, total_amount + 1), amount))

choose_random_numbers(6, 49)
