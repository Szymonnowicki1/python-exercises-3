# -*- coding: utf-8 -*-
A = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}
B = {1, 2, 55, 66, 77}

# %%
A.add(44)

# %%
print(set(A))

# %%
print(A&B)
print(A|B)
print(A-B)

# %%
A.discard(44)