# -*- coding: utf-8 -*-
import requests

x = requests.get('http://youtube.pl')
print(x)
x.status_code
