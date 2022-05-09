from decimal import Decimal
import numpy as np
from numba import jit

@jit(nopython=True)
def Manhattan(x1,x2):
  sum = 0
  len_ = len(x1)
  for i in range(len_):
    if(not np.isnan(x1[i]) and not np.isnan(x2[i])):
      sum += abs(x1[i] - x2[i])
  return sum


def Manhattan_D(x1,x2):
  sum = Decimal('0.0')
  len_ = len(x1)
  for i in range(len_):
    if(not np.isnan(x1[i]) and not np.isnan(x2[i])):
      sum += abs(Decimal(str(x1[i])) - Decimal(str(x2[i])))
      #print(abs(x1[i] - x2[i]))
  return sum


from scipy.spatial.distance import cityblock

def Manhattan_lib(x1,x2):
  return cityblock(x1, x2)