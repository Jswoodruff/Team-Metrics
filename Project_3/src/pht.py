import pandas as pd
import numpy as np
import os 
from pathlib import Path
import warnings
# import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# df = pd.read_excel(r'C:\Users\jwood\OneDrive\Desktop\Work Folder\Work Folder\Project_2\data\Trend_Full_Data_data (1).xlsx')
# filepath = os.path.join(Path(__file__).parents[1], 'data\Trend_Full_Data_data (1).xlsx')

# filepath= r'C:\Users\Alex Lucchesi\OneDrive\Desktop\pht\Project_2\data\Trend_Full_Data_data (1).xlsx'
filepath = os.path.join(Path(__file__).parents[1], 'data/Trend_Full_Data_data (1).xlsx')


def pht_run_app():
    
    df = pd.read_excel(filepath)

    pht = df[['Complete Date', 'Tech ID', 'PHT Result', 'Region', 'System']]
    wa_pht = pht[pht['Region'] == 'SEATTLE REGION']
    spokane_pht = wa_pht[wa_pht['System'] == "SPOKANE, WA"]
    sea_pht = wa_pht[wa_pht['System'] != "SPOKANE, WA"]
    

    pht_fail = sea_pht['PHT Result'].value_counts().sort_index()[0]
    pht_pass = sea_pht['PHT Result'].value_counts().sort_index()[1]
    pht_pww = sea_pht['PHT Result'].value_counts().sort_index()[3]



    return pht_fail, pht_pass, pht_pww

if __name__ == '__main__':
    print(pht_run_app())
