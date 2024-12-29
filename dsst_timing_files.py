# Extracting DSST Timing Files
#Script creates and prints an Excel and txt file for each subset of data: set1_nr_cor, set1_r_cor, set1_cor, set3_cor, and set9_cor

import pandas as pd
import os

file_path = 'CBAS0004_dsst_2024-12-11_14h22.35.334.csv'
df = pd.read_csv(file_path)

#checks all the necessary columns are present in the file 
required_columns = {'SetNum', 'SetType', 'stimulus_start_time', 'stimulus_end_time', 'key_dsst_resp.corr'}
if not required_columns.issubset(df.columns):
    raise ValueError(f"Dataset must contain the following columns: {required_columns}")
    
df_selected = df[['SetNum', 'SetType', 'stimulus_start_time', 'stimulus_end_time', 'key_dsst_resp.corr']].copy()
# calculating response time (2nd column of Type B file)
df_selected['Duration'] = df_selected['stimulus_end_time'] - df_selected['stimulus_start_time']

df_selected['Parametric Modulation'] = 1

#Separates it into 5 types of files: 1_r, 1_nr, 1 combining r and nr, 3 and 9 
#Based on SetNum and SetType 
subsets = {
    "set1_nr_cor": df[(df['SetNum'] == 1) & (df['SetType'] == "nr") & (df['key_dsst_resp.corr'] == 1)],
    "set1_r_cor": df[(df['SetNum'] == 1) & (df['SetType'] == "r") & (df['key_dsst_resp.corr'] == 1)],
    "set1_cor": df[(df['SetNum'] == 1) & (df['key_dsst_resp.corr'] == 1)],
    "set3_cor": df[(df['SetNum'] == 3) & (df['key_dsst_resp.corr'] == 1)],
    "set9_cor": df[(df['SetNum'] == 9) & (df['key_dsst_resp.corr'] == 1)],
}

#Adds 'Duration' and 'Parametric Modulation' to each subset
for subset_name, subset_data in subsets.items():
    subsets[subset_name] = subset_data.copy()  # Make a copy to avoid modifying the original df
    subsets[subset_name]['Duration'] = subsets[subset_name]['stimulus_end_time'] - subsets[subset_name]['stimulus_start_time']
    subsets[subset_name]['Parametric Modulation'] = 1

#Folders to save new Excel and timing file 
excel_folder = 'dsst_excel_files'
timing_folder = 'dsst_timing_files'
os.makedirs(excel_folder, exist_ok=True)
os.makedirs(timing_folder, exist_ok=True)

#Iterates through each set 
for subset_name, set_data in subsets.items():
  if not set_data.empty:
    #Saves it as an Excel file in the specified folder 
    excel_file = os.path.join(excel_folder, f"{subset_name}.xlsx")
    set_data.to_excel(excel_file, index=False)
        
    #Creates a txt file for each subset containing 3 columns: Onset time, Duration, and Parametric Modulation
    txt_file = os.path.join(timing_folder, f"{subset_name}.txt")
    timing_df = set_data[['stimulus_start_time', 'Duration', 'key_dsst_resp.corr']]
    #Renames stimulus_start_time as Onset Time 
    timing_df.columns = ['Onset Time', 'Duration', 'Parametric Modulation']
      
    #For formating purposes of the Type C txt file 
    with open(txt_file, 'w') as f:
        for _, row in timing_df.iterrows():
            #Consistent spacing
            f.write(f"{row['Onset Time']:.1f} {row['Duration']:.1f} {int(row['Parametric Modulation'])}\n")

    print(f"Timing file created: {txt_file}")

