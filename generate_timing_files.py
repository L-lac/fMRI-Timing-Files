# Extracting DSST Timing Files
# Lena Lin :)

import pandas as pd
import os

file_path = 'CBAS0004_dsst_2024-12-11_14h22.35.334.csv'
df = pd.read_csv(file_path)

#checks all the necessary columns are present in the file 
required_columns = {'SetNum', 'SetType', 'stimulus_start_time', 'stimulus_end_time', 'key_dsst_resp.corr'}
if not required_columns.issubset(df.columns):
    raise ValueError(f"Dataset must contain the following columns: {required_columns}")
  
# calculating response time (2nd column of Type B file)
df_selected['Duration'] = df_selected['stimulus_end_time'] - df_selected['stimulus_start_time']
  
#Uses lambda function to check if the response is correct or incorrect then combines it with the trial type
#3rd column of Type B file
df_selected['trial_type'] = df_selected.apply(
  lamda row: f"{row['SetType'].lower()}_{'correct' if row['key_dsst_resp.corr'] == 1 else 'incorrect'}",
      axis=1
  )

df_selected['Parametric Modulation'] = 1

#Separates it into 5 types of files: 1_r, 1_nr, 1 combining r and nr, 3 and 9 
#Based on SetNum and SetType 
subsets = {
  "1_nr": df[(df['SetNum'] == 1) & (df['key_dsst_resp.corr'] == 0)],
  "1_r": df[(df['SetNum'] == 1) & (df['key_dsst_resp.corr'] == 1)],
  "1_combined": df[df['SetNum'] == 1],
  "3": df[df['SetNum'] == 3],
  "9": df[df['SetNum'] == 9],
}

#Folders to save new Excel and timing file 
excel_folder = 'dsst_excel_files'
timing_folder = 'dsst_timing_files'
os.makedirs(excel_folder, exist_ok=True)
os.makedirs(timing_folder, exist_ok=True)

#Iterates through each set 
for subset_name, set_data in set_definitions.items():
  if not set_data.empty:
    #Saves it as an Excel file in the specified folder and prints a confirmation message after completion 
    excel_file = os.path.join(excel_folder, f"{set_name}.xlsx")
    set_data.to_excel(excel_file, index=False)
    print(f"Excel file created: {excel_file}")
    
    #Creates a txt file for each subset containing 3 columns: Onset time, Duration, and Parametric Modulation
    txt_file = os.path.join(txt_folder, f"{set_name}.txt")
    timing_df = set_data[['stimulus_start_time', 'Duration', 'Parametric Modulation']]
    # Rename for clarity
    timing_df.columns = ['Onset Time', 'Duration', 'Parametric Modulation']  
    #For Formatting purposes of the Type C file 
    timing_df.to_csv(txt_file, sep='\t', index=False, header=False) 
    print(f"Text file created: {txt_file}")   
  

