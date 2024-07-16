# -*- coding: utf-8 -*-
import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/todos')
tasks = json.loads(r.text)
