import numpy as np
from numba import jit

from desEstandar import desStandard

@jit(nopython=True)
def indexMatrix(n_tam,df_Data):
    data_example = np.empty((n_tam,n_tam))
    data_example[:] = 0
    n,m = data_example.shape

    cardinls = np.empty((n_tam,n_tam))
    cardinls[:] = 0
    

    for i in range(n):
        for j in range(m):
            if i != j :
                dev, card = desStandard(df_Data[:,i],df_Data[:,j])
                data_example[j][i] = dev
                cardinls[j][i] = card
    return data_example,cardinls