import pandas as pd
from Generate_Session_File import Generate_Session
import xlwings as xw

def generating_Positions():
    kite=Generate_Session()

    positions=kite.positions()
    positions1=positions["net"]
    # convert into dataframe
    df = pd.DataFrame(data=positions1)
    df.drop(df.columns[[1,2,5,6,8,10,11,12,15,16,17,18,19,20,21,22,23,24,25,26,27,28]], axis=1, inplace=True)
    return df
