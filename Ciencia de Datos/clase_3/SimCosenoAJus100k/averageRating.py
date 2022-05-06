import numpy as np

def averageRating(df_Data):
  n,m = df_Data.shape
  print(n)
  avgR = []
  for i in range(n):
    row = df_Data.iloc[i,:]
    #print(row)
    avgR.append(row.mean())
  return np.array(avgR)
