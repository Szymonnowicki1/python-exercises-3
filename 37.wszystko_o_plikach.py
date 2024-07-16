# -*- coding: utf-8 -*-

# Operacje na plikach :
# 1 otwieranie
# 2 pisanie
# 3 zamykanie

# r - read(czytanie)
# w - write(pisanie) - jesli plik istnie to usuwa a jak nie to go tworzy
# a - append(dopisanie) 

# %%
file = open('test', 'w')
file.write('sample !')
file.close()
