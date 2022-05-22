from decimal import Decimal
import numpy as np
import math
from numba import jit

@jit(nopython=True)
def Pearson(x,y):
  n_Reg = len(x)
  
  x_y = 0 # x*y
  s_x = 0 # sumatoria(x)
  s_y = 0 # sumatoria(y)
  s_x2 = 0 ## sumatoria de cuadrados(x)
  s_y2 = 0 ## sumatoria de cuadrados(x)
  n = 0
  for i in range(n_Reg):
    if(not np.isnan(x[i]) and not np.isnan(y[i])):
      n += 1
      x_y += (x[i] *  y[i])
      s_x += x[i]
      s_y += y[i]
      s_x2 += x[i]**2
      s_y2 += y[i]**2

      #print(x[i],' * ', y[i] ,' : ',x_y)
        

  if n == 0:
    s_x_s_y = 0
    s_x2N = 0
    s_y2N = 0
  else:
    s_x_s_y = (s_x * s_y)/n # sumatoria(x*y)/n
    s_x2N = (s_x**2)/n # sumatoria de X al cuadrado sobre n
    s_y2N = (s_y**2)/n # sumatoria de Y al cuadrado sobre n
  
  #print(s_x_s_y)
  #print(s_x2N)
  #print(s_y2N)
  denominator = math.sqrt(s_x2 - s_x2N) * math.sqrt(s_y2 - s_y2N)
  if x_y == 0: return -100000.0 
  if denominator == 0:
    r = 0
  else:
    r = (x_y - s_x_s_y) / denominator

  return r



#@jit(nopython=True)
def Pearson_D(x,y):
  n_Reg = len(x)
  
  x_y = Decimal('0.0') # x*y
  s_x = Decimal('0.0') # sumatoria(x)
  s_y = Decimal('0.0') # sumatoria(y)
  s_x2 = Decimal('0.0') ## sumatoria de cuadrados(x)
  s_y2 = Decimal('0.0') ## sumatoria de cuadrados(x)
  n = Decimal('0.0')
  for i in range(n_Reg):
    if(not np.isnan(x[i]) and not np.isnan(y[i])):
      n += 1
      x_y += (Decimal(str(x[i])) *  Decimal(str(y[i])))
      s_x += Decimal(str(x[i]))
      s_y += Decimal(str(y[i]))
      s_x2 += Decimal(str(x[i]))**Decimal('2')
      s_y2 += Decimal(str(y[i]))**Decimal('2')

      #print(x[i],' * ', y[i] ,' : ',x_y)
        

  if n == 0:
    s_x_s_y = 0
    s_x2N = 0
    s_y2N = 0
  else:
    s_x_s_y = (s_x * s_y)/n # sumatoria(x*y)/n
    s_x2N = (s_x**Decimal('2'))/n # sumatoria de X al cuadrado sobre n
    s_y2N = (s_y**Decimal('2'))/n # sumatoria de Y al cuadrado sobre n
    
  #print(s_x_s_y)
  #print(s_x2N)
  #print(s_y2N)
  denominator = (Decimal(str(math.sqrt(s_x2 - s_x2N))) * Decimal(str(math.sqrt(s_y2 - s_y2N))))

  if x_y == 0: return  Decimal('-100000.0')
  if(denominator == 0):
    r = 0
  else:
    r = (x_y - s_x_s_y) / denominator
  return r


@jit(nopython=True)
def Pearson_lib(x1,x2):

  # column_movieId = np.intersect1d(x1,x2)
  
  rating_x_user= []
  rating_user= []
  for id in range(len(x1)):
    if(not np.isnan(x1[id]) and not np.isnan(x2[id])):
      rating_x_user.append(x1[id])
      rating_user.append(x2[id])
  
  pearson = np.corrcoef(rating_x_user, rating_user)[0,1]
  if  np.isnan(pearson) :return 0
  return pearson