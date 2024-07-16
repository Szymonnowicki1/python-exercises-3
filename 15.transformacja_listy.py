# -*- coding: utf-8 -*-
liczby = [1, 2, 3, 4, 5, 6, 7, 8]

# %%
potegaDo2 = []
for element in liczby:
    potegaDo2.append(element ** 2)
    
# %%
print([element ** 2 for element in liczby])

# %%
liczbyParzyste = []
for element in liczby:
    if element % 2 == 0:
        liczbyParzyste.append(element)
        
# %%
liczbyParzyste2 = [element for element in liczby if element % 2 == 0]
        
#  element - co robimy
#  for element in liczby - skąd wybieramy wartości
#  if (element % 2 == 0) - warunek, jakie dokładnie wybieramy wartości

