import numpy as np
from numba import jit

@jit(nopython=True)
def desStandard(item_1, item_2):
    n = len(item_1)
    us = 0 
    card = 0
    for i in range(n):
        if(not np.isnan(item_1[i]) and not np.isnan(item_2[i])):
            card += 1
            us += (item_1[i] - item_2[i])

    if card == 0: return 0,0
    # print("desviacion Numerador: ",us)
    # print("cardinalidad: ",card)
    return us/card,card