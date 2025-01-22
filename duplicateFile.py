import os
from collections import Counter

def get_filenames(folder):
    """Retrieve a list of filenames in a folder."""
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def check_for_duplicate_filenames(folder1, folder2, folder3):
    """Check for duplicate filenames across three folders."""
    # Gather filenames from each folder
    filenames1 = get_filenames(folder1)
    filenames2 = get_filenames(folder2)
    filenames3 = get_filenames(folder3)

    # Combine all filenames into one list
    all_filenames = filenames1 + filenames2 + filenames3

    # Count occurrences of each filename
    filename_counts = Counter(all_filenames)

    # Find duplicates
    duplicates = [filename for filename, count in filename_counts.items() if count > 1]

    if duplicates:
        raise ValueError(f"Duplicate filenames found: {', '.join(duplicates)}")
    else:
        print("No duplicate filenames found across the folders.")

# Directories to check
folder1 = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4'
folder2 = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 4'
folder3 = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 4'

# Run the check
try:
    check_for_duplicate_filenames(folder1, folder2, folder3)
except ValueError as e:
    print(e)

# ====================
# --------------------
# ====================
import os


def get_filenames(folder):
    """Retrieve a list of filenames in a folder."""
    return set(f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))


def check_files_in_subfolders(main_folder, subfolder1, subfolder2, subfolder3):
    """Check if filenames in subfolders are also present in the main folder."""

    # Retrieve filenames from the main folder
    main_folder_files = get_filenames(main_folder)

    # Retrieve filenames from the subfolders
    subfolder1_files = get_filenames(subfolder1)
    subfolder2_files = get_filenames(subfolder2)
    subfolder3_files = get_filenames(subfolder3)

    # Compare each subfolder's filenames with the main folder's filenames
    missing_in_subfolder1 = subfolder1_files - main_folder_files
    missing_in_subfolder2 = subfolder2_files - main_folder_files
    missing_in_subfolder3 = subfolder3_files - main_folder_files

    # Raise error if any files are missing
    if missing_in_subfolder1 or missing_in_subfolder2 or missing_in_subfolder3:
        raise ValueError(f"Files missing in subfolders:\n"
                         f"Subfolder1 missing files: {missing_in_subfolder1}\n"
                         f"Subfolder2 missing files: {missing_in_subfolder2}\n"
                         f"Subfolder3 missing files: {missing_in_subfolder3}")
    else:
        print("All filenames in subfolders are present in the main folder.")


# Directories to check
main_folder = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/Sorted-images/DR Severity 4'
subfolder1 = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/test/DR Severity 4'
subfolder2 = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/validate/DR Severity 4'
subfolder3 = 'C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4'

# Run the check
try:
    check_files_in_subfolders(main_folder, subfolder1, subfolder2, subfolder3)
except ValueError as e:
    print(e)
