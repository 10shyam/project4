import pandas as pd
import dataframe_image as dfi

def Calculate_Total_M2M(positions):
    positions1=positions["net"]
    Total_M2M=0
    for x in range(len(positions1)):
        Total_M2M=Total_M2M+positions1[x]["m2m"]

    Total_M2M=round(Total_M2M, 2)
    return Total_M2M


def update_TotalM2M_Image(positions):
    
    positions1=positions["net"]
    Total_M2M=Calculate_Total_M2M(positions)
    # convert into dataframe
    df = pd.DataFrame(data=positions1)
    df.drop(df.columns[[1,2,5,6,8,10,11,12,15,16,17,18,19,20,21,22,23,24,25,26,27,28]], axis=1, inplace=True)
    df1=df.round({"average_price":1, "last_price":2, "unrealised":3})
    df1.drop(df.columns[[1,6]], axis=1, inplace=True)  
    df1.loc[len(df1.index)] = ['Total', "....", "...","...",Total_M2M]
    dfi.export(df1, 'Total_M2M_Image.png')
    print(df1)

def update_positions_table(positions):
    
    positions1=positions["net"]
    Total_M2M=Calculate_Total_M2M(positions)
    # convert into dataframe
    df = pd.DataFrame(data=positions1)
    df.drop(df.columns[[1,2,5,6,8,10,11,12,15,16,17,18,19,20,21,22,23,24,25,26,27,28]], axis=1, inplace=True)
    df1=df.round({"average_price":1, "last_price":2, "unrealised":3})
    #df1.drop(df.columns[[1,6]], axis=1, inplace=True)  
    #df1.loc[len(df1.index)] = ['Total', 'Total', 'Total','Total',Total_M2M]
    return df1

