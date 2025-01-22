import math
import os
import shutil

# ---------------------------------------
# Macula Negative
# ---------------------------------------

#
# source_Macula_Negative = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/Macula Negative"
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Negative'
# os.mkdir(folder_path)
# destination_macula_negative_train = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Negative'
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/Macula Negative'
# os.mkdir(folder_path)
# destination_macula_negative_validate = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/Macula Negative'
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/Macula Negative'
# os.mkdir(folder_path)
# destination_macula_negative_test = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/Macula Negative'
#
#
# imageList = os.listdir(source_Macula_Negative)
# number_files = len(imageList)
#
# print(number_files)
#
# split1 = math.floor((70 / 100) * number_files)
# split2 = math.floor((85 / 100) * number_files)
#
# print(split1)
#
# # split images
# group_train = imageList[:split1]  # First 70%
# group_validate = imageList[split1:split2]  # Next 15%
# group_test = imageList[split2:]  # Final 15%
#
# # Move files to train folder
# for f in group_train:
#     src_path = os.path.join(source_Macula_Negative, f)
#     dst_path = os.path.join(destination_macula_negative_train, f)
#     shutil.copy2(src_path, dst_path)
#
# # Move files to validate folder
# for f in group_validate:
#     src_path = os.path.join(source_Macula_Negative, f)
#     dst_path = os.path.join(destination_macula_negative_validate, f)
#     shutil.copy2(src_path, dst_path)
#
# # Move files to test folder
# for f in group_test:
#     src_path = os.path.join(source_Macula_Negative, f)
#     dst_path = os.path.join(destination_macula_negative_test, f)
#     shutil.copy2(src_path, dst_path)
#
# print(f"Moved {len(group_train)} files to {destination_macula_negative_train}")
# print(f"Moved {len(group_validate)} files to {destination_macula_negative_validate}")
# print(f"Moved {len(group_test)} files to {destination_macula_negative_test}")


# ---------------------------------------
# Macula Positive
# ---------------------------------------


source_Macula_Positive = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/Macula Positive"

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive'
os.mkdir(folder_path)
destination_macula_positive_train = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/Macula Positive'
os.mkdir(folder_path)
destination_macula_positive_validate = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/Macula Positive'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/Macula Positive'
os.mkdir(folder_path)
destination_macula_positive_test = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/Macula Positive'


imageList = os.listdir(source_Macula_Positive)
number_files = len(imageList)

print(number_files)

split1 = math.floor((70 / 100) * number_files)
split2 = math.floor((85 / 100) * number_files)

print(split1)

# split images
group_train = imageList[:split1]  # First 70%
group_validate = imageList[split1:split2]  # Next 15%
group_test = imageList[split2:]  # Final 15%

# Move files to train folder
for f in group_train:
    src_path = os.path.join(source_Macula_Positive, f)
    dst_path = os.path.join(destination_macula_positive_train, f)
    shutil.copy2(src_path, dst_path)

# Move files to validate folder
for f in group_validate:
    src_path = os.path.join(source_Macula_Positive, f)
    dst_path = os.path.join(destination_macula_positive_validate, f)
    shutil.copy2(src_path, dst_path)

# Move files to test folder
for f in group_test:
    src_path = os.path.join(source_Macula_Positive, f)
    dst_path = os.path.join(destination_macula_positive_test, f)
    shutil.copy2(src_path, dst_path)

print(f"Moved {len(group_train)} files to {destination_macula_positive_train}")
print(f"Moved {len(group_validate)} files to {destination_macula_positive_validate}")
print(f"Moved {len(group_test)} files to {destination_macula_positive_test}")


# ---------------------------------------
# DR0
# ---------------------------------------


source_DR0 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/DR Severity 0"

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 0'
os.mkdir(folder_path)
destination_DR0_train = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 0'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 0'
os.mkdir(folder_path)
destination_DR0_validate = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 0'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 0'
os.mkdir(folder_path)
destination_DR0_test = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 0'


imageList = os.listdir(source_DR0)
number_files = len(imageList)

print(number_files)

split1 = math.floor((70 / 100) * number_files)
split2 = math.floor((85 / 100) * number_files)

print(split1)

# split images
group_train = imageList[:split1]  # First 70%
group_validate = imageList[split1:split2]  # Next 15%
group_test = imageList[split2:]  # Final 15%

# Move files to train folder
for f in group_train:
    src_path = os.path.join(source_DR0, f)
    dst_path = os.path.join(destination_DR0_train, f)
    shutil.copy2(src_path, dst_path)

# Move files to validate folder
for f in group_validate:
    src_path = os.path.join(source_DR0, f)
    dst_path = os.path.join(destination_DR0_validate, f)
    shutil.copy2(src_path, dst_path)

# Move files to test folder
for f in group_test:
    src_path = os.path.join(source_DR0, f)
    dst_path = os.path.join(destination_DR0_test, f)
    shutil.copy2(src_path, dst_path)

print(f"Moved {len(group_train)} files to {destination_DR0_train}")
print(f"Moved {len(group_validate)} files to {destination_DR0_validate}")
print(f"Moved {len(group_test)} files to {destination_DR0_test}")





# ---------------------------------------
# DR01
# ---------------------------------------


source_DR1 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/DR Severity 1"

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1'
os.mkdir(folder_path)
destination_DR1_train = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 1'
os.mkdir(folder_path)
destination_DR1_validate = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 1'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 1'
os.mkdir(folder_path)
destination_DR1_test = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 1'


imageList = os.listdir(source_DR1)
number_files = len(imageList)

print(number_files)

split1 = math.floor((70 / 100) * number_files)
split2 = math.floor((85 / 100) * number_files)

print(split1)

# split images
group_train = imageList[:split1]  # First 70%
group_validate = imageList[split1:split2]  # Next 15%
group_test = imageList[split2:]  # Final 15%

# Move files to train folder
for f in group_train:
    src_path = os.path.join(source_DR1, f)
    dst_path = os.path.join(destination_DR1_train, f)
    shutil.copy2(src_path, dst_path)

# Move files to validate folder
for f in group_validate:
    src_path = os.path.join(source_DR1, f)
    dst_path = os.path.join(destination_DR1_validate, f)
    shutil.copy2(src_path, dst_path)

# Move files to test folder
for f in group_test:
    src_path = os.path.join(source_DR1, f)
    dst_path = os.path.join(destination_DR1_test, f)
    shutil.copy2(src_path, dst_path)

print(f"Moved {len(group_train)} files to {destination_DR1_train}")
print(f"Moved {len(group_validate)} files to {destination_DR1_validate}")
print(f"Moved {len(group_test)} files to {destination_DR1_test}")



# ---------------------------------------
# DR2
# ---------------------------------------


source_DR2 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/DR Severity 2"

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2'
os.mkdir(folder_path)
destination_DR2_train = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 2'
os.mkdir(folder_path)
destination_DR2_validate = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 2'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 2'
os.mkdir(folder_path)
destination_DR2_test = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 2'


imageList = os.listdir(source_DR2)
number_files = len(imageList)

print(number_files)

split1 = math.floor((70 / 100) * number_files)
split2 = math.floor((85 / 100) * number_files)

print(split1)

# split images
group_train = imageList[:split1]  # First 70%
group_validate = imageList[split1:split2]  # Next 15%
group_test = imageList[split2:]  # Final 15%

# Move files to train folder
for f in group_train:
    src_path = os.path.join(source_DR2, f)
    dst_path = os.path.join(destination_DR2_train, f)
    shutil.copy2(src_path, dst_path)

# Move files to validate folder
for f in group_validate:
    src_path = os.path.join(source_DR2, f)
    dst_path = os.path.join(destination_DR2_validate, f)
    shutil.copy2(src_path, dst_path)

# Move files to test folder
for f in group_test:
    src_path = os.path.join(source_DR2, f)
    dst_path = os.path.join(destination_DR2_test, f)
    shutil.copy2(src_path, dst_path)

print(f"Moved {len(group_train)} files to {destination_DR2_train}")
print(f"Moved {len(group_validate)} files to {destination_DR2_validate}")
print(f"Moved {len(group_test)} files to {destination_DR2_test}")


# ---------------------------------------
# DR3
# ---------------------------------------


source_DR3 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/DR Severity 3"

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3'
os.mkdir(folder_path)
destination_DR3_train = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 3'
os.mkdir(folder_path)
destination_DR3_validate = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 3'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 3'
os.mkdir(folder_path)
destination_DR3_test = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 3'


imageList = os.listdir(source_DR3)
number_files = len(imageList)

print(number_files)

split1 = math.floor((70 / 100) * number_files)
split2 = math.floor((85 / 100) * number_files)

print(split1)

# split images
group_train = imageList[:split1]  # First 70%
group_validate = imageList[split1:split2]  # Next 15%
group_test = imageList[split2:]  # Final 15%

# Move files to train folder
for f in group_train:
    src_path = os.path.join(source_DR3, f)
    dst_path = os.path.join(destination_DR3_train, f)
    shutil.copy2(src_path, dst_path)

# Move files to validate folder
for f in group_validate:
    src_path = os.path.join(source_DR3, f)
    dst_path = os.path.join(destination_DR3_validate, f)
    shutil.copy2(src_path, dst_path)

# Move files to test folder
for f in group_test:
    src_path = os.path.join(source_DR3, f)
    dst_path = os.path.join(destination_DR3_test, f)
    shutil.copy2(src_path, dst_path)

print(f"Moved {len(group_train)} files to {destination_DR3_train}")
print(f"Moved {len(group_validate)} files to {destination_DR3_validate}")
print(f"Moved {len(group_test)} files to {destination_DR3_test}")




# ---------------------------------------
# DR4
# ---------------------------------------


source_DR4 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/DR Severity 4"

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4'
os.mkdir(folder_path)
destination_DR4_train = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 4'
os.mkdir(folder_path)
destination_DR4_validate = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 4'

folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 4'
os.mkdir(folder_path)
destination_DR4_test = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 4'


imageList = os.listdir(source_DR4)
number_files = len(imageList)

print(number_files)

split1 = math.floor((70 / 100) * number_files)
split2 = math.floor((85 / 100) * number_files)

print(split1)

# split images
group_train = imageList[:split1]  # First 70%
group_validate = imageList[split1:split2]  # Next 15%
group_test = imageList[split2:]  # Final 15%

# Move files to train folder
for f in group_train:
    src_path = os.path.join(source_DR4, f)
    dst_path = os.path.join(destination_DR4_train, f)
    shutil.copy2(src_path, dst_path)

# Move files to validate folder
for f in group_validate:
    src_path = os.path.join(source_DR4, f)
    dst_path = os.path.join(destination_DR4_validate, f)
    shutil.copy2(src_path, dst_path)

# Move files to test folder
for f in group_test:
    src_path = os.path.join(source_DR4, f)
    dst_path = os.path.join(destination_DR4_test, f)
    shutil.copy2(src_path, dst_path)

print(f"Moved {len(group_train)} files to {destination_DR4_train}")
print(f"Moved {len(group_validate)} files to {destination_DR4_validate}")
print(f"Moved {len(group_test)} files to {destination_DR4_test}")








#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 0'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4'
# os.mkdir(folder_path)
#
#
# # --------------------------
#

#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/Macula Positive'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 0'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 1'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 2'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 3'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 4'
# os.mkdir(folder_path)
#
# # ------------------------------------
#

#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/Macula Positive'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 0'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 1'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 2'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 3'
# os.mkdir(folder_path)
#
# folder_path = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 4'
# os.mkdir(folder_path)