# -*- coding: utf-8 -*-
import requests

r = requests.get('https://jsonplaceholder.typicode.com/todos')


def funkcja_ktora_podaje_najwieksza_wartosc(mydict):
    return  [
        key
        for key, value in mydict.items()
        if value == max(mydict.value())
    ]

funkcja_ktora_podaje_najwieksza_wartosc(pokoje)