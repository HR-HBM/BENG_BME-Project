import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

TRAIN_DIR = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/train"
TEST_DIR = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/test"
VAL_DIR = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/validate"

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory(TRAIN_DIR, target_size=(512,512), batch_size=32, class_mode="binary")

val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

val_set = val_datagen.flow_from_directory(VAL_DIR, target_size=(512, 512), batch_size=32, class_mode="binary")

IMG_SHAPE = (512,512,3)
base_model = tf.keras.applications.EfficientNetB1(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')
for layer in base_model.layers:
    layer.trainable = False
for layer in base_model.layers[-5:]:
    layer.trainable = True

print("Number of layers in the base model: ", len(base_model.layers))

# Fine tune from this layer onwards
# fine_tune_at = 100

# Freeze all the layers before the `fine_tune_at` layer
# for layer in base_model.layers[:fine_tune_at]:
#   layer.trainable =  False

model = tf.keras.Sequential([
  base_model,
  # tf.keras.layers.Conv2D(128, 3, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

print(model.summary())

batch_size = 32
epochs = 10

model.compile(loss='binary_crossentropy',
              optimizer = tf.keras.optimizers.Adam(1e-4),
              metrics=['accuracy'])

history = model.fit(x=train_set, validation_data=val_set, epochs=epochs)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

print(acc)
print(val_acc)

epochs_range = range(len(acc))
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))

plt.subplot(1,2,1)
plt.plot(epochs_range, acc, label="Training accuracy")
plt.plot(epochs_range, val_acc, label="Validation accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy After Finetuning")

plt.subplot(1,2,2)
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss After Finetuning")

plt.show()

model.save("C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/MaculaEdema(finetuned).h5")

# evaluation for model without CLAHE preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt




model_path = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/MaculaEdema(finetuned).h5"
model = tf.keras.models.load_model(model_path)


test_dir = "C:/Users/HR/Downloads/mbrset-a-mobile-brazilian-retinal-dataset-1.0/mbrset-a-mobile-brazilian-retinal-dataset-1.0/MaculaEdema/test"

# Define ImageDataGenerator without augmentation (only rescaling)
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

# Load images from test directory
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(512, 512),  # Match the size used in training
    batch_size=32,
    class_mode='binary',  # or 'binary' if you have 2 classes
    shuffle=False  # Don't shuffle so predictions align with file order
)

# Assuming you have the test_generator from flow_from_directory
class_indices = test_generator.class_indices

# To check class indices (it returns a dictionary)
print("Class Indices:", class_indices)

# Get the predicted probabilities (using sigmoid for binary classification)
y_pred_probs = model.predict(test_generator)

# Map the probabilities to class labels
y_pred = (y_pred_probs > 0.5).astype(int)  # Get binary predictions (0 or 1)

# Print the predicted classes with their probabilities
for i, prob in enumerate(y_pred_probs):
    print(f"Image {i+1}: Predicted Probability = {prob[0]}, Predicted Class = {list(class_indices.keys())[y_pred[i]]}")



# Get true labels
y_true = test_generator.classes

y_pred_probs = model.predict(test_generator)
y_pred = (y_pred_probs > 0.5).astype(int)  # Convert probabilities to binary class labels


# # Get predicted probabilities
# y_pred_probs = model.predict(test_generator)
#
# # Convert probabilities to class labels
# y_pred = np.argmax(y_pred_probs, axis=1)

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Print classification report
print("\nClassification Report:\n", classification_report(y_true, y_pred))

labels = list(test_generator.class_indices.keys())

# Plot confusion matrix
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=labels, yticklabels=labels)

plt.xlabel("Predicted")

plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()



