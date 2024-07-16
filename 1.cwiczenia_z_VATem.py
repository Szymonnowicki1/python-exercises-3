# -*- coding: utf-8 -*-

cenaNettoKursu = 35
VAT = 21
cenaBruttoKursu = cenaNettoKursu * (1 + VAT / 100)
obliczonyVAT = (1 + VAT / 100)

# %%
cenaNettoAjax = 25
Vat = 20
cenaBruttoAjax = cenaNettoAjax  * (1 + VAT / 100)

# %%
cenaBruttoOprogramowania = 165
VAT = 23
cenaNettoOprogramowania = cenaBruttoOprogramowania / obliczonyVAT
