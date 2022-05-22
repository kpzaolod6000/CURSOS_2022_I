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
  if sum ==  0: return 10000000.0
  return math.sqrt(sum)


def Euclidiana_D(x1,x2):
  sum = Decimal('0.0')
  len_ = len(x1)
  for i in range(len_):
    if(not np.isnan(x1[i]) and not np.isnan(x2[i])):
        sum += (Decimal(str(x1[i])) - Decimal(str(x2[i])))**Decimal('2')
  if sum ==  0: return Decimal('1000000.0')
  return Decimal(str(math.sqrt(sum)))


from scipy.spatial.distance import euclidean
def Euclidiana_lib(x1,x2):
  rating_x_user= []
  rating_user= []
  for id in range(len(x1)):
    if(not np.isnan(x1[id]) and not np.isnan(x2[id])):
      rating_x_user.append(x1[id])
      rating_user.append(x2[id])
  
  return euclidean(rating_x_user,rating_user)