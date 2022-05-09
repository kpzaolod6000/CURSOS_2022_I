from decimal import Decimal
import numpy as np
import math
from numba import jit

@jit(nopython=True)
def Euclidiana(x1,x2):
  sum = 0
  len_ = len(x1)
  for i in range(len_):
    if(not np.isnan(x1[i]) and not np.isnan(x2[i])):
        sum += (x1[i] - x2[i])**2
  return math.sqrt(sum)


def Euclidiana_D(x1,x2):
  sum = Decimal('0.0')
  len_ = len(x1)
  for i in range(len_):
    if(not np.isnan(x1[i]) and not np.isnan(x2[i])):
        sum += (Decimal(str(x1[i])) - Decimal(str(x2[i])))**Decimal('2')
  return Decimal(str(math.sqrt(sum)))


from scipy.spatial.distance import euclidean
def Euclidiana_lib(x1,x2):
 return euclidean(x1,x2)