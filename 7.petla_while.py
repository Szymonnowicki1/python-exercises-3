# -*- coding: utf-8 -*-

liczba = 100

while (liczba <= 100) and (liczba > 0):
    print(liczba)
    liczba -= 1
    
# %%
wynik = 1
x = 0

while x < 3:
    z = int(input('Podaj liczbe : '))
    wynik *= z
    x += 1

print(wynik)

# %%

for i in range(200):
    if (i % 5 == 0) and  (i % 7 != 0 ):
        print(i)

# %%
wynik = 0
z = 0
while z < 3:
    x = int(input('Podaj liczbe dodatnia parzysta : '))
    if x % 2 == 0 and x > 0:
        wynik += x
    else:
        print('Podaj liczbe jeszcze raz')
        continue
    z += 1
        
print('Suma 3 liczb dodatnich parzystych : ', wynik)














































    