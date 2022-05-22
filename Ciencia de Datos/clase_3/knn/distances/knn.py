from distances.pearson import Pearson,Pearson_D,Pearson_lib
from distances.coseno import Coseno,Coseno_D,Coseno_lib

def Knn(data,n_users,metric,id_user):

  distances = []
  # dist = []
  
  for i in range(len(n_users)):
    if n_users[i] != n_users[id_user]:
      d = metric(data[:,i],data[:,id_user])
      ##d puedes cero si los valores son muy cercanos o si no hay ninguna valor coherente
      distances.append((n_users[i],d))
  #     dist.append(d)
      
  # dist.sort()
  # print(dist)
  if metric == Pearson or metric == Pearson_D or metric == Pearson_lib or metric == Coseno or metric == Coseno_D or metric == Coseno_lib:
    distances.sort(key=lambda x: x[1], reverse=True) # lambda artistTuple invoca los elementos que tienen en distances
  else:
    distances.sort(key=lambda x: x[1], reverse=False)

  return distances
