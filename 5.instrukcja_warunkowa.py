# -*- coding: utf-8 -*-

wybor = int(input('1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 5 - potegowanie, 6 - modulo : '))
a = int(input('Podaj pierwsza liczbe : '))
b = int(input('Podaj druga liczbe : '))

if wybor == 1:
    print(a + b)
elif wybor == 2:
    print(a - b)
elif wybor == 3:
    print(a * b)
elif wybor == 4:
    if b == 0:
        print('Nie dziel przez 0')
    else:
        print(a / b)        
elif wybor == 5:
    print(a ** b)
elif wybor == 6:
    print(a % b)
else:
    print('ERROR')