
import pandas as pd
import numpy as np

def MatrixSCA(np_Matrix,columns_names):
    columns_namesR = columns_names[::-1]
    df_similitud = pd.DataFrame(np_Matrix, columns = columns_namesR[0:len(columns_namesR)-1],index=columns_names[0:len(columns_names)-1])

    return df_similitud