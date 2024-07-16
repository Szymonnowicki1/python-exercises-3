# -*- coding: utf-8 -*-
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

imiona = ['Szymon', 'Tomek', 'Wika', 'Kasia', 'Julia', 'Corso']

celciusz = {'t1' : -10, 't2' : 20, 't3' : 41, 't4' : 18, 't5' : 0}

# %%
x = {number : number ** 2 for number in numbers}
print(x)

# %%
y = {imie : len(imie) for imie in imiona if imie.endswith('a')}
print(y)

# %%
z = {key : celciusz * 1.8 + 32 for key, celciusz in celciusz.items() if celciusz > 20}
print(z)