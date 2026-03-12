import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model
import joblib
import os

dataset_dir = "data/Food Classification dataset"

IMG_SIZE = 160
BATCH_SIZE = 32

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train_generator = datagen.flow_from_directory(
    dataset_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    dataset_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

num_classes = len(train_generator.class_indices)

# -------------------------
# โหลด pretrained model
# -------------------------
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

# Phase 1: Freeze ทั้งหมดก่อน
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.4)(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# -------------------------
# Phase 1 Training
# -------------------------
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    train_generator,
    epochs=5,
    validation_data=val_generator,
    steps_per_epoch=150,
    validation_steps=120
)

# -------------------------
# Phase 2: Fine-tune
# -------------------------
base_model.trainable = True

# freeze แค่ layer แรก ๆ
# for layer in base_model.layers[:100]:
#     layer.trainable = False
for layer in base_model.layers[:70]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.00005),  # LR ต่ำมาก
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# model.fit(
#     train_generator,
#     epochs=10,
#     validation_data=val_generator,
#     steps_per_epoch=200,      
#     validation_steps=80,
#     callbacks=[early_stop]
# )
model.fit(
    train_generator,
    epochs=12,
    validation_data=val_generator,
    steps_per_epoch=150,
    validation_steps=80,
    callbacks=[early_stop]
)

# -------------------------
# Evaluate
# -------------------------
# loss, acc = model.evaluate(val_generator)
# print("Final Validation Accuracy:", acc)

# os.makedirs("models", exist_ok=True)
# # model.save("models/cnn_model.h5")


# class_names = list(train_generator.class_indices.keys())
# joblib.dump(class_names, "models/cnn_class_names.pkl")
# joblib.dump({"Accuracy": float(acc)}, "models/cnn_metrics.pkl")

# print("Fine-tuned CNN saved!")

# -------------------------
# Evaluate
# -------------------------
loss, acc = model.evaluate(val_generator)
print("Final Validation Accuracy:", acc)

os.makedirs("models", exist_ok=True)

# ✅ save โมเดลที่เพิ่ง train เสร็จตรงๆ เป็น .keras
# model.save("models/cnn_model.keras")
# print("Done!")
model.save("models/cnn_model.h5")
print("Model saved without optimizer!")

class_names = list(train_generator.class_indices.keys())
joblib.dump(class_names, "models/cnn_class_names.pkl")
joblib.dump({"Accuracy": float(acc)}, "models/cnn_metrics.pkl")

print("Fine-tuned CNN saved!")