# -*- coding: utf-8 -*-
import json

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

w = json.dumps(film, indent=2, sort_keys=True)

# %%
with open('sample.json', 'r') as file:
    wynik = json.load(file)
    
# %%
import pprint
print(wynik)
pprint.pprint(wynik)