import pandas as pd
import numpy as np

df = pd.read_csv('labels_mbrset.csv')

print( df.head())

# -----------------------------
# code below is to remove rows containing blank values for final icdr and final edema column in CSV file
# -----------------------------


df['final_edema'].replace('', np.nan, inplace=True)
df['final_icdr'].replace('', np.nan, inplace=True)


df.dropna(subset=['final_edema'], inplace=True)
df.dropna(subset=['final_icdr'], inplace=True)


print(df.iloc[:30])

df.to_csv('labels_mbrset_modified.csv', index=False)

df2 = pd.read_csv('labels_mbrset_modified.csv')


# --------------------------------------
# the below code is to create new csv files based on values for final icdr and final edema values
# ---------------------------------------

df2.loc[df2['final_icdr'] == 4].to_csv('DRSeverityGrade4.csv', index=False)
df2.loc[df2['final_icdr'] == 3].to_csv('DRSeverityGrade3.csv', index=False)
df2.loc[df2['final_icdr'] == 2].to_csv('DRSeverityGrade2.csv', index=False)
df2.loc[df2['final_icdr'] == 1].to_csv('DRSeverityGrade1.csv', index=False)
df2.loc[df2['final_icdr'] == 0].to_csv('DRSeverityGrade0.csv', index=False)


df2.loc[df2['final_edema'] == 'yes'].to_csv('EdemaPositive.csv', index=False)
df2.loc[df2['final_edema'] == 'no'].to_csv('EdemaNegative.csv', index=False)



