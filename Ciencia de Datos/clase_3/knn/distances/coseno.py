from decimal import Decimal
import numpy as np
import math
from numba import jit
@jit(nopython=True)
def Coseno(x,y):
  n_Reg = len(x)
  x_y = 0
  x2 = 0
  y2 = 0
  for i in range(n_Reg):
    if(not np.isnan(x[i]) and not np.isnan(y[i])):
      x_y += x[i] * y[i]
      x2 += x[i]**2
      y2 += y[i]**2

  # print(x_y)
  # print(math.sqrt(x2))
  # print(math.sqrt(y2))
  
  denominator = (math.sqrt(x2) * math.sqrt(y2))
  if x_y == 0: return -1000000.0
  if denominator == 0 : return 0
  
  cos_ = (x_y)/denominator
  return cos_


def Coseno_D(x,y):
  n_Reg = len(x)
  x_y = Decimal('0.0')
  x2 = Decimal('0.0')
  y2 = Decimal('0.0')
  for i in range(n_Reg):
    if(not np.isnan(x[i]) and not np.isnan(y[i])):
      x_y += Decimal(str(x[i])) * Decimal(str(y[i]))
      x2 += Decimal(str(x[i]))**Decimal('2')
      y2 += Decimal(str(y[i]))**Decimal('2')

  # print(x_y)
  # print(math.sqrt(x2))
  # print(math.sqrt(y2))
  denominator = (Decimal(str(math.sqrt(x2))) * Decimal(str(math.sqrt(y2))))
  if x_y == 0: return Decimal('-1000000.0')
  if denominator == 0 : return Decimal('0.0')
  cos_ = (x_y)/denominator
  return cos_

from scipy import spatial
def Coseno_lib(x1,x2):

  rating_x_user= []
  rating_user= []
  for id in range(len(x1)):
    if(not np.isnan(x1[id]) and not np.isnan(x2[id])):
      rating_x_user.append(x1[id])
      rating_user.append(x2[id])
  
  return 1 - spatial.distance.cosine(rating_x_user,rating_user)