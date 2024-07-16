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

print(json.dumps(film , ensure_ascii=False))

# %%
with open('sample.json', 'w') as file:
    json.dump(film, file, ensure_ascii=False)