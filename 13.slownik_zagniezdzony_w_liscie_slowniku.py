# -*- coding: utf-8 -*-
ratings1 = {
                   "Arkadiusz": (2,1,2,3,2,3),
                   "Agnieszka": (4,2,1,3,4)
                 }

# %%
for key in ratings1:
    print(key, ratings1[key])

# %%
people3 = [ 
            "Arkadiusz",
            "Wiola",
            "Kuba"
          ]

# %%
for value in people3:
    print(value)

# %%
people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
          ]

# %%
for dictionary in people2:
    for key in dictionary:
        print(key, dictionary[key])
        
    # Dla każdego słownika w pojemniku people2 
     #       dla każdego klucza w słowniku
     #                 wypisuj (klucze i wartości)

# %%
people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }

# %%
for key in people:
    print('ID :', key)
    for value in people[key]:
        print(value, people[key][value])
        
# %%
print(people.items())

# %%
for id , dictionary in people.items():
    print(id)
    for key in dictionary:
        print(key, dictionary[key])









































