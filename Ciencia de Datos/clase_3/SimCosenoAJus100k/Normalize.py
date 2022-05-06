import numpy as np

def equation(vR,min_R,max_R):
  return ((2*(vR-min_R)) - (max_R - min_R))/(max_R-min_R)

def Normalize_(df_Data,R,min_R,max_R):
  NR = R.copy()

  #NR = np.array([])
  for i in range(len(R)):
    #if R[i] != np.nan:
    if not np.isnan(R[i]):
      NR[i] = equation(R[i],min_R,max_R)

  return R,NR
