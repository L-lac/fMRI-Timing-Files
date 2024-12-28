# Overview: :brain:	
This repository contains a Python script that processes a dataset to generate both Excel and txt files formatted for fMRI analysis, specifically DSST. It splits the datset into 5 different subsets based on specific conditions (SetNum and SetType) and calculates the timing information for each trial. The resulting files are stored in 2 separate folders: 
  - excel_files: .xlsx
  - timing_files: .txt files formatted for tools like FSL
    * contains 3 columns each
    * Onset time: start time
    * Duration
    * Parametric Modulation: Always 1 in this scenario
    *  Sample Output:
      ```
      0.0 2.0 1
      10.0 2.0 1
      40.0 2.0 1
      ```
   
This script generates the following subsets, focusing on only correct responses:
* set1_nr_cor
* set1_r_cor
* set1_cor
* set3_cor
* set9_cor

# Future Extensions: :thinking:
> **Important:** 
In the future if you need to further analyze your dataset for the trial_type column
such as having congruent or incongruent_run1.txt files or handling correct/incorrect
responses, use the lamda function. 

### Example Code: 
```python
df_selected['trial_type'] = df_selected.apply(
  lamda row: f"{row['SetType'].lower()}_{'correct' if row['key_dsst_resp.corr'] == 1 else 'incorrect'}",
      axis=1
  )
```
This uses the lamda function to combine SetType and response correctness for column 3 (trial_type) of the Type B files. 

## Contact:
If you have any questions or issues with the code, feel free to contact Lena Lin. :blush:
