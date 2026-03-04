# import h5py
# import numpy as np
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from tensorflow.keras.utils import to_categorical

# # โหลดข้อมูล
# with h5py.File('data/food_c101_n1000_r384x384x3.h5', 'r') as f:
#     X = np.array(f['images'])
#     y = np.array(f['labels'])

# # Normalize
# X = X / 255.0

# # แปลง label เป็น categorical
# num_classes = len(np.unique(y))
# y = to_categorical(y, num_classes)

# # แบ่งข้อมูล
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # สร้าง CNN
# model = Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(384,384,3)),
#     MaxPooling2D(2,2),
#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(2,2),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dense(num_classes, activation='softmax')
# ])

# # Compile
# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# # Train
# model.fit(X_train, y_train, epochs=5, batch_size=32)

# # Evaluate
# loss, acc = model.evaluate(X_test, y_test)
# print("CNN Accuracy:", acc)

# # Save
# model.save("models/cnn_model.h5")

# print("CNN Model saved successfully!")
# import h5py
# import numpy as np
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from tensorflow.keras.utils import to_categorical

# # โหลดข้อมูล
# with h5py.File('data/food_c101_n1000_r384x384x3.h5', 'r') as f:
#     X = np.array(f['images'])
#     y = np.array(f['category'])
#     category_names = np.array(f['category_names'])

# print("Images shape:", X.shape)
# print("Labels shape:", y.shape)

# # Normalize
# X = X / 255.0

# # แปลง label เป็น categorical
# num_classes = len(np.unique(y))
# y = to_categorical(y, num_classes)

# # แบ่งข้อมูล
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # 🔥 ลดขนาดภาพให้เทรนเร็วขึ้น (สำคัญมาก)
# X_train = X_train[:, :128, :128, :]
# X_test = X_test[:, :128, :128, :]

# # สร้าง CNN
# model = Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
#     MaxPooling2D(2,2),
#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(2,2),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dense(num_classes, activation='softmax')
# ])

# # Compile
# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# # Train
# model.fit(X_train, y_train, epochs=3, batch_size=32)

# # Evaluate
# loss, acc = model.evaluate(X_test, y_test)
# print("CNN Accuracy:", acc)

# # Save
# model.save("models/cnn_model.h5")

# print("CNN Model saved successfully!")
# import h5py
# import numpy as np
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# import tensorflow as tf

# # โหลดข้อมูล
# # with h5py.File('data/food_c101_n1000_r384x384x3.h5', 'r') as f:
# #     X = np.array(f['images'])
# #     y = np.array(f['category'])
# with h5py.File('data/food_c101_n1000_r384x384x3.h5', 'r') as f:
#     X = np.array(f['images'])
#     y = np.array(f['category'])
#     class_names = np.array(f['category_names'])

# # บันทึกชื่อ class ไว้ใช้ในเว็บ
# import joblib
# joblib.dump(class_names, "models/cnn_class_names.pkl")

# print("Images shape:", X.shape)
# print("Labels shape:", y.shape)

# # Normalize
# X = X / 255.0

# num_classes = y.shape[1]  # เพราะมัน one-hot อยู่แล้ว

# # แบ่งข้อมูล
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # ลดขนาดภาพ
# # X_train = X_train[:, :128, :128, :]
# # X_test = X_test[:, :128, :128, :]
# X_train = tf.image.resize(X_train, (128,128)).numpy()
# X_test = tf.image.resize(X_test, (128,128)).numpy()

# # สร้าง CNN
# # model = Sequential([
# #     Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
# #     MaxPooling2D(2,2),
# #     Conv2D(64, (3,3), activation='relu'),
# #     MaxPooling2D(2,2),
# #     Flatten(),
# #     Dense(128, activation='relu'),
# #     Dense(num_classes, activation='softmax')
# # ])
# model = Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
#     MaxPooling2D(2,2),

#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(2,2),

#     Conv2D(128, (3,3), activation='relu'),
#     MaxPooling2D(2,2),

#     Flatten(),
#     Dense(256, activation='relu'),
#     Dense(num_classes, activation='softmax')
# ])

# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',  # ใช้ตัวนี้เพราะ y เป็น one-hot
#     metrics=['accuracy']
# )

# # model.fit(X_train, y_train, epochs=10, batch_size=32)
# model.fit(X_train, y_train, epochs=25, batch_size=32)

# loss, acc = model.evaluate(X_test, y_test)
# print("CNN Accuracy:", acc)

# model.save("models/cnn_model.h5")

# print("CNN Model saved successfully!")
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# import joblib

# dataset_dir = "data/Food Classification dataset"

# datagen = ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2
# )

# train_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(128,128),
#     batch_size=32,
#     class_mode='categorical',
#     subset='training'
# )

# test_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(128,128),
#     batch_size=32,
#     class_mode='categorical',
#     subset='validation'
# )

# num_classes = len(train_generator.class_indices)

# model = Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
#     MaxPooling2D(2,2),

#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(2,2),

#     Conv2D(128, (3,3), activation='relu'),
#     MaxPooling2D(2,2),

#     Flatten(),
#     Dense(256, activation='relu'),
#     Dense(num_classes, activation='softmax')
# ])

# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# model.fit(train_generator, epochs=10)

# loss, acc = model.evaluate(test_generator)
# print("Accuracy:", acc)

# model.save("models/cnn_model.h5")

# class_names = list(train_generator.class_indices.keys())
# joblib.dump(class_names, "models/cnn_class_names.pkl")

# print("New CNN Model saved successfully!")

# loss, acc = model.evaluate(test_generator)
# print("Accuracy:", acc)

# # บันทึก accuracy
# cnn_metrics = {
#     "Accuracy": acc
# }

# joblib.dump(cnn_metrics, "models/cnn_metrics.pkl")
# import tensorflow as tf
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.applications import MobileNetV2
# from tensorflow.keras.callbacks import EarlyStopping
# import joblib
# import os

# dataset_dir = "data/Food Classification dataset"

# datagen = ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2,
#     rotation_range=20,
#     zoom_range=0.2,
#     horizontal_flip=True
# )

# train_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(224,224),
#     batch_size=32,
#     class_mode='categorical',
#     subset='training'
# )

# val_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(224,224),
#     batch_size=32,
#     class_mode='categorical',
#     subset='validation'
# )

# num_classes = len(train_generator.class_indices)

# # โหลด pretrained model
# base_model = MobileNetV2(
#     weights='imagenet',
#     include_top=False,
#     input_shape=(224,224,3)
# )

# base_model.trainable = False  # freeze layer

# x = base_model.output
# x = GlobalAveragePooling2D()(x)
# x = Dropout(0.5)(x)
# predictions = Dense(num_classes, activation='softmax')(x)

# model = Model(inputs=base_model.input, outputs=predictions)

# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# early_stop = EarlyStopping(patience=3, restore_best_weights=True)

# model.fit(
#     train_generator,
#     epochs=15,
#     validation_data=val_generator,
#     callbacks=[early_stop]
# )

# loss, acc = model.evaluate(val_generator)
# print("Validation Accuracy:", acc)

# os.makedirs("models", exist_ok=True)
# model.save("models/cnn_model.h5")

# class_names = list(train_generator.class_indices.keys())
# joblib.dump(class_names, "models/cnn_class_names.pkl")

# joblib.dump({"Accuracy": float(acc)}, "models/cnn_metrics.pkl")

# print("New Transfer Learning CNN saved!")

# import tensorflow as tf
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.applications import MobileNetV2
# from tensorflow.keras.callbacks import EarlyStopping
# import joblib
# import os

# dataset_dir = "data/Food Classification dataset"

# IMG_SIZE = 160
# BATCH_SIZE = 32

# datagen = ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2
# )

# train_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='training'
# )

# val_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='validation'
# )

# num_classes = len(train_generator.class_indices)

# # โหลด pretrained model
# base_model = MobileNetV2(
#     weights='imagenet',
#     include_top=False,
#     input_shape=(IMG_SIZE, IMG_SIZE, 3)
# )

# base_model.trainable = False

# x = base_model.output
# x = GlobalAveragePooling2D()(x)
# x = Dropout(0.3)(x)
# predictions = Dense(num_classes, activation='softmax')(x)

# model = Model(inputs=base_model.input, outputs=predictions)

# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# early_stop = EarlyStopping(
#     monitor='val_loss',
#     patience=2,
#     restore_best_weights=True
# )

# # จำกัดจำนวน step ต่อ epoch (ลดเวลาครึ่งหนึ่ง)
# model.fit(
#     train_generator,
#     epochs=8,
#     validation_data=val_generator,
#     steps_per_epoch=200,          # <<< ลดตรงนี้
#     validation_steps=100,
#     callbacks=[early_stop]
# )

# loss, acc = model.evaluate(val_generator)
# print("Validation Accuracy:", acc)

# os.makedirs("models", exist_ok=True)
# model.save("models/cnn_model.h5")

# class_names = list(train_generator.class_indices.keys())
# joblib.dump(class_names, "models/cnn_class_names.pkl")

# joblib.dump({"Accuracy": float(acc)}, "models/cnn_metrics.pkl")

# print("Fast CNN saved!")

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import EarlyStopping
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
    steps_per_epoch=250,
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
    steps_per_epoch=200,
    validation_steps=80,
    callbacks=[early_stop]
)

# -------------------------
# Evaluate
# -------------------------
loss, acc = model.evaluate(val_generator)
print("Final Validation Accuracy:", acc)

os.makedirs("models", exist_ok=True)
model.save("models/cnn_model.h5")

class_names = list(train_generator.class_indices.keys())
joblib.dump(class_names, "models/cnn_class_names.pkl")
joblib.dump({"Accuracy": float(acc)}, "models/cnn_metrics.pkl")

print("Fine-tuned CNN saved!")