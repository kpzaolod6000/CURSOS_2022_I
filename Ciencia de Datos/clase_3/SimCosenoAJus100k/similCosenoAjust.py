import numpy as np
from numba import jit
@jit(nopython=True)
def simCosenoAjust(avgR,v_item1,v_item2):

  R_r = 0
  R_item1 = 0
  R_item2 = 0

  for i in range(len(v_item2)):
    if(not np.isnan(v_item1[i]) and not np.isnan(v_item2[i])):
      R_r += (v_item1[i] - avgR[i]) * (v_item2[i] - avgR[i])
      R_item1 += pow(v_item1[i] - avgR[i],2)
      R_item2 += pow(v_item2[i] - avgR[i],2)
  
  denominator = (np.sqrt(R_item1) * np.sqrt(R_item2))
  if(denominator == 0.0): return 0.0
  
  return (R_r)/denominator
