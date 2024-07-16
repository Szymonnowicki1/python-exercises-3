# -*- coding: utf-8 -*-
namesandsurnames = []

with open('imionanazwiska.txt', 'r') as file:
    for line in file:
        namesandsurnames.append(tuple(line.replace('\n', '').split(' ')))
       
with open('imiona.txt', 'w') as file:
    for item in namesandsurnames:
        print(file.write(item[0] + '\n'))
 # %%       
with open('nazwiska.txt', 'w') as file:
    for item in namesandsurnames:
        try:
            print(file.write(item[1] + '\n'))
        except IndexError:
            print(file.write('\n'))