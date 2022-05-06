import numpy as np
def predict(vPredict,df_similitud,movieId,df_ratings):
  # index_columns = df_ratings.index.values
  similarToN = 0
  similarToD = 0

  SxNR,Sn = 0,0
  
  for id in movieId:
    #print(df_ratings[i])
 
    try:
      SxNR = (df_similitud.loc[vPredict,id]) * (df_ratings.loc[id,'NR'])
      Sn = abs(df_similitud.loc[vPredict,id])

    except KeyError:
      print("INVERTIR INDEX")
      
    if(np.isnan(SxNR) or np.isnan(Sn)): #aca meda valores nan pero por la dataset
        #continue #pararechazar los valores nan
        SxNR = (df_similitud.loc[id,vPredict]) * (df_ratings.loc[id,'NR'])
        Sn = abs(df_similitud.loc[id,vPredict])

    similarToN += SxNR
    similarToD += Sn
  if(similarToD == 0.0): return 0.0
  p = similarToN/similarToD
  return p
