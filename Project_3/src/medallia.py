import pandas as pd
import numpy as np
import os
from pathlib import Path
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

filepath = os.path.join(Path(__file__).parents[1], 'data/Trend_Full_Data_data (1).xlsx')
filepath1 = os.path.join(Path(__file__).parents[1], 'data/TechOps_Responses_20220903_092431.xlsx')
filepath2 = os.path.join(Path(__file__).parents[1], 'data/SBI SMART Report MTD 7.22 to 8.13.22 Team (1).xlsx')


def run_app():

    pht_df = pd.read_excel(filepath)
    df = pd.read_excel(filepath1,
    skiprows=2,
    header=0)
    df_master = pd.read_excel(filepath2,
    sheet_name=-1)

    pht = pht_df[['Complete Date', 'Tech ID', 'PHT Result', 'Region', 'System']]
    wa_pht = pht[pht['Region'] == 'SEATTLE REGION']
    # spokane_pht = wa_pht[wa_pht['System'] == "SPOKANE, WA"]
    # sea_pht = wa_pht[wa_pht['System'] != "SPOKANE, WA"]

    nps = df[['Tech ID', 'SMS tNPS', 'Reason for score']]
    master = df_master[["Tech ID", "Last Name, First Name", "Company"]]

    d = nps.merge(master, how="left", on="Tech ID")

    d['First Name'] = d["Last Name, First Name"].str.split(
        ',', expand=True)[1]
    d['Last Name'] = d["Last Name, First Name"].str.split(
        ',', expand=True)[0]
    d['Tech Name'] = d['First Name'] + \
        ' ' + d['Last Name']

    d.drop(
        columns=[
            'Last Name, First Name',
            'First Name',
            'Last Name'],
        inplace=True)

    d = d[['Tech ID', 'Tech Name', 'Company', 'SMS tNPS', 'Reason for score']]

    d2 = wa_pht.merge(master, how = 'left', on = 'Tech ID')
    
    d2['First Name'] = d2["Last Name, First Name"].str.split(
        ',', expand=True)[1]
    d2['Last Name'] = d2["Last Name, First Name"].str.split(
        ',', expand=True)[0]
    d2['Tech Name'] = d2['First Name'] + \
        ' ' + d2['Last Name']

    d2 = d2[['Tech ID', 'PHT Result', 'Tech Name', 'Company' ]]

    nps_full = d.fillna("No Reply")

    kos_nps = nps_full[nps_full['Company'] == 'KOSCOM']
    sbi_nps = nps_full[nps_full['Company'] == 'SBI']
    beon_nps = nps_full[nps_full['Company'] == 'BEON']
    ukr_nps = nps_full[nps_full['Company'] == 'UKR']

    kos_pht = d2[d2['Company'] == 'KOSCOM']
    k_pht = kos_pht['PHT Result'].value_counts().sort_index()
    k_fail = kos_pht[kos_pht['PHT Result']== 'FAL'].value_counts().sum()
    k_pass = kos_pht[kos_pht['PHT Result']== 'PAS'].value_counts().sum()
    k_pww = kos_pht[kos_pht['PHT Result']== 'PWW'].value_counts().sum()

    sbi_pht = d2[d2['Company'] == 'SBI']
    s_pht = sbi_pht['PHT Result'].value_counts().sort_index()
    s_fail = sbi_pht[sbi_pht['PHT Result']== 'FAL'].value_counts().sum()
    s_pass = sbi_pht[sbi_pht['PHT Result']== 'PAS'].value_counts().sum()
    s_pww = sbi_pht[sbi_pht['PHT Result']== 'PWW'].value_counts().sum()

    beon_pht = d2[d2['Company'] == 'BEON']
    b_pht = beon_pht['PHT Result'].value_counts().sort_index()
    b_fail = beon_pht[beon_pht['PHT Result']== 'FAL'].value_counts().sum()
    b_pass = beon_pht[beon_pht['PHT Result']== 'PAS'].value_counts().sum()
    b_pww = beon_pht[beon_pht['PHT Result']== 'PWW'].value_counts().sum()

    ukr_pht = d2[d2['Company'] == 'UKR']
    u_pht = ukr_pht['PHT Result'].value_counts().sort_index()
    u_fail = ukr_pht[ukr_pht['PHT Result']== 'FAL'].value_counts().sum()
    u_pass = ukr_pht[ukr_pht['PHT Result']== 'PAS'].value_counts().sum()
    u_pww = ukr_pht[ukr_pht['PHT Result']== 'PWW'].value_counts().sum()

    return k_fail, k_pass, k_pww, s_fail, s_pass, s_pww, u_fail, u_pass, u_pww, b_fail, b_pass, b_pww, kos_nps, sbi_nps, beon_nps, ukr_nps, k_pht, s_pht, b_pht, u_pht, d

def per_score(df):
    num_score = 0

    for score in df['SMS tNPS']:
        if score >= 9:
            num_score += 1
        elif score <= 6:
            num_score -= 1

    nps_per = round(((num_score) / (len(df['SMS tNPS']))) * 100, 2)

    return nps_per



if __name__ == '__main__':
    print(run_app(), per_score())
    # print(run_app())
