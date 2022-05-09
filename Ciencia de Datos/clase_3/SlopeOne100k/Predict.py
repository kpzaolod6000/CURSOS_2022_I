import numpy as np
def getPredict(df_Data,Matrixdev,cardinls,user_predict,item_cal,columns_names):
    columns_names.remove(item_cal)

    #print(columns_names)
    sum_devc = 0
    sum_card = 0
    for name in columns_names:
        data = df_Data.loc[user_predict,name]
        #print(data)
        if (not np.isnan(data)):
            sum_devc += (data + Matrixdev.loc[item_cal,name]) * cardinls.loc[name,item_cal]
            sum_card += cardinls.loc[name,item_cal]
            # print(data, ' ',cardinls.loc[name,item_cal], ' ' , Matrixdev.loc[item_cal,name])

    # print(" sumatoria de(devi,j * u)c: ", sum_devc)
    # print(" sumatoria de(cardinales): ", sum_card)
    if sum_card == 0: return 0
    return sum_devc/sum_card

