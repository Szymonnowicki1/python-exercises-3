# -*- coding: utf-8 -*-
import random
movie = ['tytul 1', 'tytul 2', 'tytul 3', 'tytul 4']
nagrodaZSkrzynki = ['glock', 'p90', 'ak-47', 'knife']

from collections import Counter

print(Counter(random.choices(nagrodaZSkrzynki, [70, 20, 8, 2], k = 100)))