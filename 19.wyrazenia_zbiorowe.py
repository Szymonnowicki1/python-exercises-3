# -*- coding: utf-8 -*-
imiona = {'Adam', 'bartek', 'czarek', 'jacek'}

# %%
a = {name.capitalize()  for name in imiona if name[0] != 'b'}
print(a)