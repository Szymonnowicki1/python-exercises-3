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

x = json.dumps(film)

print(x)

# %%
y = json.loads(x)

# %%
with open('sample.json', 'r') as file:
    wynik = json.load(file)