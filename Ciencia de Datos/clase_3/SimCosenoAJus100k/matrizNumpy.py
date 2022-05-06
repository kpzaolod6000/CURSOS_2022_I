import numpy as np

from numba import jit

from similCosenoAjust import simCosenoAjust

@jit(nopython=True)
def indexMatrix(n_tam,avgR,df_Data):

    data_example = np.empty((n_tam,n_tam))
    data_example[:] = np.nan
    n,m = data_example.shape

    idi = 0
    for i in range(n):
        idj = m-i-1
        for j in range(i+1,m+1):
            data_example[i][idj] = simCosenoAjust(avgR,df_Data[:,i],df_Data[:,j])
            idj-=1
        idi +=1
   
    return data_example