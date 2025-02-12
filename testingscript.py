import os
import shutil
import tensorflow as tf
from PIL import Image


# -------------------
# for Macula positive
# -------------------

# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (rotation)"
# save_dir_rotation30 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (rotation30)"
# save_dir_rotation_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/Macula Positive (rotation_hflip)"


# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)


# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     image = Image.open(original_img_path)
#
#
#     rotated_img = image.rotate(30, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation30.jpg"
#     rotated_img.save(os.path.join(save_dir_rotation30, rotated_filename))
#
#     # Load the image
#     # img = tf.keras.utils.load_img(original_img_path)
#     #
#     # # Convert the image to an array
#     # x = tf.keras.utils.img_to_array(img)
#     #
#     # # Reshape the input image for the generator
#     # x = x.reshape((1,) + x.shape)
#
#     # Apply horizontal flip augmentation
#     # i = 0
#     # for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#     #                                           save_to_dir=save_dir_rotation_hflip,
#     #                                           save_prefix=f"{os.path.splitext(filename)[0]}_rotation_hflip",
#     #                                           save_format='jpg'):
#     #     i += 1
#     #     if i >= 1:  # Only generate one horizontally flipped image
#     #         break
#
#     # # Apply vertical flip augmentation
#     # i = 0
#     # for batch in datagen_vertical_flip.flow(x, batch_size=1,
#     #                                         save_to_dir=save_dir_hflip_vflip,
#     #                                         save_prefix=f"{os.path.splitext(filename)[0]}_hflip_vflip",
#     #                                         save_format='jpg'):
#     #     i += 1
#     #     if i >= 1:  # Only generate one vertically flipped image
#     #         break




# -----------------
# for ICDR level 01
# -----------------

# # original_img_folder_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (vflip)"
# original_img_folder_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (hflip)"
# original_img_folder_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotation)"
#
# save_dir_rotation15_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate15_hflip)"
# save_dir_rotation15_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate15_vflip)"
# save_dir_hflip_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (hflip_vflip)"
#
#
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
#
# for filename in os.listdir(original_img_folder_rotate):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_rotate, filename)
#
#     # image = Image.open(original_img_path)
#
#
#     # rotated_img = image.rotate(30, expand=False, resample=Image.BICUBIC)
#     # rotated_filename = f"{os.path.splitext(filename)[0]}_rotation30.jpg"
#     # rotated_img.save(os.path.join(save_dir_rotation30, rotated_filename))
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
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_rotation15_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}_rotation15_hflip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotation15_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_rotation15_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
#
# for filename in os.listdir(original_img_folder_hflip):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_hflip, filename)
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
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_hflip_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_hflip_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
#
# original_img_folder_rotate15_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate15_hflip)"
# save_dir_rotation15_hflip_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate15_hflip_vflip)"
#
#
# for filename in os.listdir(original_img_folder_rotate15_hflip):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_rotate15_hflip, filename)
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
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotation15_hflip_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_rotation15_hflip_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
#
# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1"
# save_dir_rotation30 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate30)"
#
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     image = Image.open(original_img_path)
#
#
#     rotated_img = image.rotate(30, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation30.jpg"
#     rotated_img.save(os.path.join(save_dir_rotation30, rotated_filename))
#
#
#
# # original_img_folder_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (hflip)"
# original_img_folder_rotate30 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate30)"
#
# save_dir_rotation30_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate30_hflip)"
# save_dir_rotation30_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate30_vflip)"
#
# for filename in os.listdir(original_img_folder_rotate30):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_rotate30, filename)
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
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_rotation30_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}_rotation30_hflip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotation30_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_rotation30_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
# original_img_folder_rotate30_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate30_hflip)"
# save_dir_rotation30_hflip_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate30_hflip_vflip)"
#
# for filename in os.listdir(original_img_folder_rotate30_hflip):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_rotate30_hflip, filename)
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
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotation30_hflip_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_rotation30_hflip_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break



# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1"
# save_dir_rotation40 = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (rotate40)"
#
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     image = Image.open(original_img_path)
#
#
#     rotated_img = image.rotate(40, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation40.jpg"
#     rotated_img.save(os.path.join(save_dir_rotation40, rotated_filename))

#
# # -----------------
# # FOR IDCR LEVEL 02
# # -----------------

# # original_img_folder_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 1 (vflip)"
# original_img_folder_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (hflip)"
# original_img_folder_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (rotation)"
#
# save_dir_rotation15_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (rotation_hflip)"
# save_dir_rotation15_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (rotation_vflip)"
# save_dir_hflip_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 2 (hflip_vflip)"
#
#
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
#
# for filename in os.listdir(original_img_folder_rotate):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_rotate, filename)
#
#     # image = Image.open(original_img_path)
#
#
#     # rotated_img = image.rotate(30, expand=False, resample=Image.BICUBIC)
#     # rotated_filename = f"{os.path.splitext(filename)[0]}_rotation30.jpg"
#     # rotated_img.save(os.path.join(save_dir_rotation30, rotated_filename))
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
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_rotation15_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}_rotation15_hflip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotation15_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_rotation15_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
#
# for filename in os.listdir(original_img_folder_hflip):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_hflip, filename)
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
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_hflip_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_hflip_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#

# # -----------------
# # FOR IDCR LEVEL 03
# # -----------------

# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3"
# save_dir_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (rotation)"
#
#
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
#
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     image = Image.open(original_img_path)
#
#     rotated_img = image.rotate(30, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation30.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(45, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation45.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(60, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation60.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(75, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation75.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(90, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation90.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(50, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation50.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(110, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation110.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(80, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation80.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(20, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation20.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#
#
# original_img_folder_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (rotation)"
# original_img_folder_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (hflip)"
# save_dir_rotate_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (hflip)"
# save_dir_rotate_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (vflip)"
# save_dir_rotate_hflip_flip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 3 (hflip_vflip)"
#
#
#
# for filename in os.listdir(original_img_folder_rotate):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_rotate, filename)
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
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_rotate_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}_hflip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotate_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
#
# for filename in os.listdir(original_img_folder_hflip):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_hflip, filename)
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
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotate_hflip_flip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_rotation_hflip_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#



# # -----------------
# # FOR IDCR LEVEL 04
# # -----------------



# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4"
# save_dir_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (rotation)"
#
#
# datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
# datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)
#
#
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     image = Image.open(original_img_path)
#
#     rotated_img = image.rotate(30, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation30.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(45, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation45.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#
#
# original_img_folder_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (rotation)"
# original_img_folder_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (hflip)"
# save_dir_rotate_hflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (hflip)"
# save_dir_rotate_vflip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (vflip)"
# save_dir_rotate_hflip_flip = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (hflip_vflip)"
#
#
#
# for filename in os.listdir(original_img_folder_rotate):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_rotate, filename)
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
#     # Apply horizontal flip augmentation
#     i = 0
#     for batch in datagen_horizontal_flip.flow(x, batch_size=1,
#                                               save_to_dir=save_dir_rotate_hflip,
#                                               save_prefix=f"{os.path.splitext(filename)[0]}_hflip",
#                                               save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one horizontally flipped image
#             break
#
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotate_vflip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break
#
#
# for filename in os.listdir(original_img_folder_hflip):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder_hflip, filename)
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
#     # Apply vertical flip augmentation
#     i = 0
#     for batch in datagen_vertical_flip.flow(x, batch_size=1,
#                                             save_to_dir=save_dir_rotate_hflip_flip,
#                                             save_prefix=f"{os.path.splitext(filename)[0]}_rotation_hflip_vflip",
#                                             save_format='jpg'):
#         i += 1
#         if i >= 1:  # Only generate one vertically flipped image
#             break

#
#
# original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4"
# save_dir_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/train/DR Severity 4 (rotation)"
#
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     image = Image.open(original_img_path)
#
#     rotated_img = image.rotate(60, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation60.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))



original_img_folder = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/validate/MaculaPositive"
save_dir_rotate = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/validate/new"



datagen_horizontal_flip = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True)
datagen_vertical_flip = tf.keras.preprocessing.image.ImageDataGenerator(vertical_flip=True)


for filename in os.listdir(original_img_folder):
    # Construct the full file path
    original_img_path = os.path.join(original_img_folder, filename)

    # Load the image
    img = tf.keras.utils.load_img(original_img_path)

    # Convert the image to an array
    x = tf.keras.utils.img_to_array(img)

    # Reshape the input image for the generator
    x = x.reshape((1,) + x.shape)

    # Apply vertical flip augmentation
    i = 0
    for batch in datagen_vertical_flip.flow(x, batch_size=1,
                                            save_to_dir=save_dir_rotate,
                                            save_prefix=f"{os.path.splitext(filename)[0]}_rotation_vflip",
                                            save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one vertically flipped image
            break

    # Apply horizontal flip augmentation
    i = 0
    for batch in datagen_horizontal_flip.flow(x, batch_size=1,
                                              save_to_dir=save_dir_rotate,
                                              save_prefix=f"{os.path.splitext(filename)[0]}rotation_hflip",
                                              save_format='jpg'):
        i += 1
        if i >= 1:  # Only generate one horizontally flipped image
            break

#
#
# for filename in os.listdir(original_img_folder):
#     # Construct the full file path
#     original_img_path = os.path.join(original_img_folder, filename)
#
#     image = Image.open(original_img_path)
#
#     rotated_img = image.rotate(45, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation45.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
#
#     rotated_img = image.rotate(60, expand=False, resample=Image.BICUBIC)
#     rotated_filename = f"{os.path.splitext(filename)[0]}_rotation60.jpg"
#     rotated_img.save(os.path.join(save_dir_rotate, rotated_filename))
