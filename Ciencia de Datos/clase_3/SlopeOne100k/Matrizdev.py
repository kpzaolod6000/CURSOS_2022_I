
import pandas as pd
import numpy as np

def matrixDev(np_Matrix,cardinls,columns_names):
    df_cardinls = pd.DataFrame(cardinls, columns = columns_names,index=columns_names)
    df_similitud = pd.DataFrame(np_Matrix, columns = columns_names,index=columns_names)
    return df_similitud,df_cardinls