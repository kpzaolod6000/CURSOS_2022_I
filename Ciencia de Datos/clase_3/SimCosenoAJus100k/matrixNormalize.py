
import pandas as pd
def getMatrixNor(columns_names,R,NR):
    data_ratings = {
        'R' : R,
        'NR' : NR
    }
    df_ratings = pd.DataFrame(data_ratings,index=columns_names[:len(columns_names)])
    df_ratings = df_ratings[df_ratings.R.notnull()]
    return df_ratings