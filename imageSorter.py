import os
import shutil
import pandas as pd

#------------------------
#Sort ICDR images
#------------------------


label_df = pd.read_csv('labels_mbrset_modified.csv')

# create class directories
for _, row in label_df.iterrows():
    f = row['file']  # File name
    l = row['final_icdr']  # Label (subdirectory name)

    label_dir = os.path.join('C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images', str(l))
    os.makedirs(label_dir, exist_ok=True)  # Create directory if it doesn't exist

    shutil.copy(f'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/images/{f}', f'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/{l}/{f}')


#------------------------
#Sort Macula Edema images
#------------------------

for _, row in label_df.iterrows():
    f = row['file']  # File name
    l = row['final_edema']  # Label (subdirectory name)

    label_dir = os.path.join('C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images', str(l))
    os.makedirs(label_dir, exist_ok=True)  # Create directory if it doesn't exist

    shutil.copy(f'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/images/{f}', f'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/{l}/{f}')
