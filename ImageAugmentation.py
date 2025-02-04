import os
import shutil
import tensorflow as tf
from PIL import Image

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Directory paths
original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4"
save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (rotation)"
save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (vflip)"
save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (hflip)"


# Initialising the ImageDataGenerator classes
datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)

# Loop through all images in the original image folder
for filename in os.listdir(original_img_folder):
    # Construct the full file path
    original_img_path = os.path.join(original_img_folder, filename)

    # Load the image
    img = tf.keras.utils.load_img(original_img_path)

    # Convert the image to an array
    x = tf.keras.utils.img_to_array(img)

    # Reshape the input image for the generator
    x = x.reshape((1,) + x.shape)

    # Copy the original image to the save directory
    # shutil.copy(original_img_path, save_dir)

    image = Image.open(original_img_path)
    rotated_img = image.rotate(15, expand=False, resample=Image.BICUBIC)
    rotated_filename = f"{os.path.splitext(filename)[0]}_rotation15.jpg"
    rotated_img.save(os.path.join(save_dir_rotation, rotated_filename))


    # Apply horizontal flip augmentation
    i = 0
    for batch in datagen_horizontal_flip.flow(x, batch_size=1,
                                              save_to_dir=save_dir_hflip,
                                              save_prefix=f"{os.path.splitext(filename)[0]}_horizontal_flip",
                                              save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one horizontally flipped image
            break

    # Apply vertical flip augmentation
    i = 0
    for batch in datagen_vertical_flip.flow(x, batch_size=1,
                                            save_to_dir=save_dir_vflip,
                                            save_prefix=f"{os.path.splitext(filename)[0]}_vertical_flip",
                                            save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one vertically flipped image
            break


original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3"
save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (rotation)"
save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (vflip)"
save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (hflip)"


# Initialising the ImageDataGenerator classes
datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)

# Loop through all images in the original image folder
for filename in os.listdir(original_img_folder):
    # Construct the full file path
    original_img_path = os.path.join(original_img_folder, filename)

    # Load the image
    img = tf.keras.utils.load_img(original_img_path)

    # Convert the image to an array
    x = tf.keras.utils.img_to_array(img)

    # Reshape the input image for the generator
    x = x.reshape((1,) + x.shape)

    # Copy the original image to the save directory
    # shutil.copy(original_img_path, save_dir)

    image = Image.open(original_img_path)
    rotated_img = image.rotate(15, expand=False, resample=Image.BICUBIC)
    rotated_filename = f"{os.path.splitext(filename)[0]}_rotation15.jpg"
    rotated_img.save(os.path.join(save_dir_rotation, rotated_filename))


    # Apply horizontal flip augmentation
    i = 0
    for batch in datagen_horizontal_flip.flow(x, batch_size=1,
                                              save_to_dir=save_dir_hflip,
                                              save_prefix=f"{os.path.splitext(filename)[0]}_horizontal_flip",
                                              save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one horizontally flipped image
            break

    # Apply vertical flip augmentation
    i = 0
    for batch in datagen_vertical_flip.flow(x, batch_size=1,
                                            save_to_dir=save_dir_vflip,
                                            save_prefix=f"{os.path.splitext(filename)[0]}_vertical_flip",
                                            save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one vertically flipped image
            break



original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2"
save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (rotation)"
save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (vflip)"
save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (hflip)"


# Initialising the ImageDataGenerator classes
datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)

# Loop through all images in the original image folder
for filename in os.listdir(original_img_folder):
    # Construct the full file path
    original_img_path = os.path.join(original_img_folder, filename)

    # Load the image
    img = tf.keras.utils.load_img(original_img_path)

    # Convert the image to an array
    x = tf.keras.utils.img_to_array(img)

    # Reshape the input image for the generator
    x = x.reshape((1,) + x.shape)

    # Copy the original image to the save directory
    # shutil.copy(original_img_path, save_dir)

    image = Image.open(original_img_path)
    rotated_img = image.rotate(15, expand=False, resample=Image.BICUBIC)
    rotated_filename = f"{os.path.splitext(filename)[0]}_rotation15.jpg"
    rotated_img.save(os.path.join(save_dir_rotation, rotated_filename))


    # Apply horizontal flip augmentation
    i = 0
    for batch in datagen_horizontal_flip.flow(x, batch_size=1,
                                              save_to_dir=save_dir_hflip,
                                              save_prefix=f"{os.path.splitext(filename)[0]}_horizontal_flip",
                                              save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one horizontally flipped image
            break

    # Apply vertical flip augmentation
    i = 0
    for batch in datagen_vertical_flip.flow(x, batch_size=1,
                                            save_to_dir=save_dir_vflip,
                                            save_prefix=f"{os.path.splitext(filename)[0]}_vertical_flip",
                                            save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one vertically flipped image
            break




original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1"
save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotation)"
save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (vflip)"
save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (hflip)"


# Initialising the ImageDataGenerator classes
datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)

# Loop through all images in the original image folder
for filename in os.listdir(original_img_folder):
    # Construct the full file path
    original_img_path = os.path.join(original_img_folder, filename)

    # Load the image
    img = tf.keras.utils.load_img(original_img_path)

    # Convert the image to an array
    x = tf.keras.utils.img_to_array(img)

    # Reshape the input image for the generator
    x = x.reshape((1,) + x.shape)

    # Copy the original image to the save directory
    # shutil.copy(original_img_path, save_dir)

    image = Image.open(original_img_path)
    rotated_img = image.rotate(15, expand=False, resample=Image.BICUBIC)
    rotated_filename = f"{os.path.splitext(filename)[0]}_rotation15.jpg"
    rotated_img.save(os.path.join(save_dir_rotation, rotated_filename))


    # Apply horizontal flip augmentation
    i = 0
    for batch in datagen_horizontal_flip.flow(x, batch_size=1,
                                              save_to_dir=save_dir_hflip,
                                              save_prefix=f"{os.path.splitext(filename)[0]}_horizontal_flip",
                                              save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one horizontally flipped image
            break

    # Apply vertical flip augmentation
    i = 0
    for batch in datagen_vertical_flip.flow(x, batch_size=1,
                                            save_to_dir=save_dir_vflip,
                                            save_prefix=f"{os.path.splitext(filename)[0]}_vertical_flip",
                                            save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one vertically flipped image
            break



original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive"
save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (rotation)"
save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (vflip)"
save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (hflip)"


# Initialising the ImageDataGenerator classes
datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)

# Loop through all images in the original image folder
for filename in os.listdir(original_img_folder):
    # Construct the full file path
    original_img_path = os.path.join(original_img_folder, filename)

    # Load the image
    img = tf.keras.utils.load_img(original_img_path)

    # Convert the image to an array
    x = tf.keras.utils.img_to_array(img)

    # Reshape the input image for the generator
    x = x.reshape((1,) + x.shape)

    # Copy the original image to the save directory
    # shutil.copy(original_img_path, save_dir)

    image = Image.open(original_img_path)
    rotated_img = image.rotate(15, expand=False, resample=Image.BICUBIC)
    rotated_filename = f"{os.path.splitext(filename)[0]}_rotation15.jpg"
    rotated_img.save(os.path.join(save_dir_rotation, rotated_filename))


    # Apply horizontal flip augmentation
    i = 0
    for batch in datagen_horizontal_flip.flow(x, batch_size=1,
                                              save_to_dir=save_dir_hflip,
                                              save_prefix=f"{os.path.splitext(filename)[0]}_horizontal_flip",
                                              save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one horizontally flipped image
            break

    # Apply vertical flip augmentation
    i = 0
    for batch in datagen_vertical_flip.flow(x, batch_size=1,
                                            save_to_dir=save_dir_vflip,
                                            save_prefix=f"{os.path.splitext(filename)[0]}_vertical_flip",
                                            save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one vertically flipped image
            break



# Directory paths
# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4"
# save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (rotation)"
# save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (vflip)"
# save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (hflip)"
#
#
# # Initialising the ImageDataGenerator classes
# datagen_rotation = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=45)
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
# # Loop through all images in the original image folder
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     # Skip files that are not images (basic check for .jpg/.jpeg/.png)
#     # if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#     #     continue
#
#     # Load the image
#     img = tf.keras.utils.load_img(original_img_path)
#
#     # Convert the image to an array
#     x = tf.keras.utils.img_to_array(img)
#
#     # Reshape the input image for the generator
#     x = x.reshape((1,) + x.shape)
#
#     # Copy the original image to the save directory
#     # shutil.copy(original_img_path, save_dir)
#
#     # Apply rotation augmentation
#     i = 0
#     for batch in datagen_rotation.flow(x, batch_size=1,
#                                        save_to_dir=save_dir_rotation,
#                                        save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_rotation",
#                                        save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one rotated image
#             break
#
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_horizontal_flip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_vertical_flip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break


# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3"
# save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (rotation)"
# save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (vflip)"
# save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (hflip)"
#
#
# # Initialising the ImageDataGenerator classes
# datagen_rotation = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=45)
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
# # Loop through all images in the original image folder
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     # Skip files that are not images (basic check for .jpg/.jpeg/.png)
#     # if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#     #     continue
#
#     # Load the image
#     img = tf.keras.utils.load_img(original_img_path)
#
#     # Convert the image to an array
#     x = tf.keras.utils.img_to_array(img)
#
#     # Reshape the input image for the generator
#     x = x.reshape((1,) + x.shape)
#
#     # Copy the original image to the save directory
#     # shutil.copy(original_img_path, save_dir)
#
#     # Apply rotation augmentation
#     i = 0
#     for batch in datagen_rotation.flow(x, batch_size=1,
#                                        save_to_dir=save_dir_rotation,
#                                        save_prefix=f"{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}_rotation",
#                                        save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one rotated image
#             break
#
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}_horizontal_flip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}_vertical_flip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break




# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2"
# save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (rotation)"
# save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (vflip)"
# save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (hflip)"
#
#
# # Initialising the ImageDataGenerator classes
# datagen_rotation = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=45)
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
# # Loop through all images in the original image folder
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     # Skip files that are not images (basic check for .jpg/.jpeg/.png)
#     # if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#     #     continue
#
#     # Load the image
#     img = tf.keras.utils.load_img(original_img_path)
#
#     # Convert the image to an array
#     x = tf.keras.utils.img_to_array(img)
#
#     # Reshape the input image for the generator
#     x = x.reshape((1,) + x.shape)
#
#     # Copy the original image to the save directory
#     # shutil.copy(original_img_path, save_dir)
#
#     # Apply rotation augmentation
#     i = 0
#     for batch in datagen_rotation.flow(x, batch_size=1,
#                                        save_to_dir=save_dir_rotation,
#                                        save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_rotation",
#                                        save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one rotated image
#             break
#
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_horizontal_flip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_vertical_flip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
#
#
#
#
# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1"
# save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotation)"
# save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (vflip)"
# save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (hflip)"
#
#
# # Initialising the ImageDataGenerator classes
# datagen_rotation = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=45)
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
# # Loop through all images in the original image folder
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     # Skip files that are not images (basic check for .jpg/.jpeg/.png)
#     # if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#     #     continue
#
#     # Load the image
#     img = tf.keras.utils.load_img(original_img_path)
#
#     # Convert the image to an array
#     x = tf.keras.utils.img_to_array(img)
#
#     # Reshape the input image for the generator
#     x = x.reshape((1,) + x.shape)
#
#     # Copy the original image to the save directory
#     # shutil.copy(original_img_path, save_dir)
#
#     # Apply rotation augmentation
#     i = 0
#     for batch in datagen_rotation.flow(x, batch_size=1,
#                                        save_to_dir=save_dir_rotation,
#                                        save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_rotation",
#                                        save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one rotated image
#             break
#
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_horizontal_flip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_vertical_flip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break

#
#
#
#
# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive"
# save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (rotation)"
# save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (vflip)"
# save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (hflip)"
#
#
# # Initialising the ImageDataGenerator classes
# datagen_rotation = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=45)
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
# # Loop through all images in the original image folder
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     # Skip files that are not images (basic check for .jpg/.jpeg/.png)
#     # if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#     #     continue
#
#     # Load the image
#     img = tf.keras.utils.load_img(original_img_path)
#
#     # Convert the image to an array
#     x = tf.keras.utils.img_to_array(img)
#
#     # Reshape the input image for the generator
#     x = x.reshape((1,) + x.shape)
#
#     # Copy the original image to the save directory
#     # shutil.copy(original_img_path, save_dir)
#
#     # Apply rotation augmentation
#     i = 0
#     for batch in datagen_rotation.flow(x, batch_size=1,
#                                        save_to_dir=save_dir_rotation,
#                                        save_prefix=f"{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}_rotation",
#                                        save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one rotated image
#             break
#
#         print("rotation complete")
#
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}_horizontal_flip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}_vertical_flip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break





# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1"
# save_dir_rotation = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotation)"
# save_dir_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (vflip)"
# save_dir_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (hflip)"
#
#
# # Initialising the ImageDataGenerator classes
# datagen_rotation = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=45)
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
# # Loop through all images in the original image folder
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     # Skip files that are not images (basic check for .jpg/.jpeg/.png)
#     # if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#     #     continue
#
#     # Load the image
#     img = tf.keras.utils.load_img(original_img_path)
#
#     # Convert the image to an array
#     x = tf.keras.utils.img_to_array(img)
#
#     # Reshape the input image for the generator
#     x = x.reshape((1,) + x.shape)
#
#     # Copy the original image to the save directory
#     # shutil.copy(original_img_path, save_dir)
#
#     # Apply rotation augmentation
#     i = 0
#     for batch in datagen_rotation.flow(x, batch_size=1,
#                                        save_to_dir=save_dir_rotation,
#                                        save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_rotation",
#                                        save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one rotated image
#             break
#
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_horizontal_flip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}.{os.path.splitext(filename)[1]}_vertical_flip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break