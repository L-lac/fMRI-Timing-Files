# Extracts the necessary columns for generating a Type A Timing File
# Lena Lin 

import pandas as pd
import os

file_path = 'CBAS0004_dsst_2024-12-11_14h22.35.334.csv'
df = pd.read_csv(file_path)

#checks all the necessary columns are present in the file 
if{'SetNum', 'SetType', 'stimulus_start_time', 'stimulus_end_time'}.issubset(df.columns):
  df_selected = df[['SetNum', 'SetType', 'stimulus_start_time', 'stimulus_end_time']].copy ()
  # calculating response time 
  df_selected['responseRT'] = df_selected['stimulus_end_time'] - df_selected['stimulus_start_time']
  #Creating new Excel file 
  output_file = 'type_A_timing_file.xlsx'
  df_selected.to_excel(output_file, index = False)
  print("Data has been processed and saved to new file.")
else: print("Required columns are not present in the dataset.")
