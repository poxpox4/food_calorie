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
import h5py
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import tensorflow as tf

# โหลดข้อมูล
# with h5py.File('data/food_c101_n1000_r384x384x3.h5', 'r') as f:
#     X = np.array(f['images'])
#     y = np.array(f['category'])
with h5py.File('data/food_c101_n1000_r384x384x3.h5', 'r') as f:
    X = np.array(f['images'])
    y = np.array(f['category'])
    class_names = np.array(f['category_names'])

# บันทึกชื่อ class ไว้ใช้ในเว็บ
import joblib
joblib.dump(class_names, "models/cnn_class_names.pkl")

print("Images shape:", X.shape)
print("Labels shape:", y.shape)

# Normalize
X = X / 255.0

num_classes = y.shape[1]  # เพราะมัน one-hot อยู่แล้ว

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ลดขนาดภาพ
# X_train = X_train[:, :128, :128, :]
# X_test = X_test[:, :128, :128, :]
X_train = tf.image.resize(X_train, (128,128)).numpy()
X_test = tf.image.resize(X_test, (128,128)).numpy()

# สร้าง CNN
# model = Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
#     MaxPooling2D(2,2),
#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(2,2),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dense(num_classes, activation='softmax')
# ])
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),
    Dense(256, activation='relu'),
    Dense(num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',  # ใช้ตัวนี้เพราะ y เป็น one-hot
    metrics=['accuracy']
)

# model.fit(X_train, y_train, epochs=10, batch_size=32)
model.fit(X_train, y_train, epochs=25, batch_size=32)

loss, acc = model.evaluate(X_test, y_test)
print("CNN Accuracy:", acc)

model.save("models/cnn_model.h5")

print("CNN Model saved successfully!")