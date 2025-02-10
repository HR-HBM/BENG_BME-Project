import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

TRAIN_DIR = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/train"
TEST_DIR = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/test"
VAL_DIR = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/validate"

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator()

train_set = train_datagen.flow_from_directory(TRAIN_DIR, target_size=(224,224), batch_size=32, class_mode="categorical")

val_datagen = tf.keras.preprocessing.image.ImageDataGenerator()

val_set = train_datagen.flow_from_directory(VAL_DIR, target_size=(224, 224), batch_size=32, class_mode="categorical")

IMG_SHAPE = (224,224,3)
base_model = tf.keras.applications.EfficientNetB1(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')
base_model.trainable = False

model = tf.keras.Sequential([
  base_model,
  tf.keras.layers.Rescaling(1./255, input_shape=IMG_SHAPE),  # Normalize the image within the model
  tf.keras.layers.Conv2D(128, 3, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(2, activation='softmax')
])

print(model.summary())

batch_size = 32
epochs = 50

model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.0001), #Adam(),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x=train_set, validation_data=val_set, batch_size=batch_size, epochs=epochs)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

print(acc)
print(val_acc)

epochs_range = range(len(acc))
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))

plt.subplot(1,2,1)
plt.plot(epochs_range, acc, label="Training accuracy")
plt.plot(epochs_range, val_acc, label="Validation accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1,2,2)
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")

plt.show()

model.save("C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/MaculaEdemaV2.h5")
