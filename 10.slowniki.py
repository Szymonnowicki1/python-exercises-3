# -*- coding: utf-8 -*-
pokoje = { 1 : 'kuchnia', 2 : 'salon', 3 : 'WC'}

# %%
pokoje[4] = 'lazienka'

# %%
pokoje.update({5 : 'jadalnia'})

# %%
pokoje.pop(2)

# %%
pokoje.popitem()

# %%
print(len(pokoje))

# %%
pokoje.clear()