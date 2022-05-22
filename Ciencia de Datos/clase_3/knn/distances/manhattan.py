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
# @jit(nopython=True)
def Manhattan_lib(x1,x2):
  
  rating_x_user= []
  rating_user= []
  for id in range(len(x1)):
    if(not np.isnan(x1[id]) and not np.isnan(x2[id])):
      rating_x_user.append(x1[id])
      rating_user.append(x2[id])
  
  return cityblock(rating_x_user, rating_user)