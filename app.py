# import streamlit as st
# import joblib
# import numpy as np
# from tensorflow.keras.models import load_model
# from PIL import Image

# st.title("Food Calorie Project")

# page = st.sidebar.selectbox(
#     "Select Page",
#     ["ML Explanation",
#      "NN Explanation",
#      "ML Prediction",
#      "NN Prediction"]
# )

# ml_metrics = joblib.load("models/ml_metrics.pkl")
# cnn_metrics = joblib.load("models/cnn_metrics.pkl")

# # โหลดโมเดล
# ensemble = joblib.load("models/ensemble_model.pkl")
# cnn_model = load_model("models/cnn_model.h5")
# le = joblib.load("models/label_encoder.pkl")

# # ------------------ หน้าอธิบาย ML ------------------
# # if page == "ML Explanation":
# #     st.header("Machine Learning - Ensemble Model")
# #     st.write("""
# #     - ทำ Data Cleaning
# #     - แปลง Calories เป็นตัวเลข
# #     - แบ่ง Low / Medium / High
# #     - ใช้ Random Forest + Gradient Boosting
# #     - ทำ Voting Ensemble
# #     """)
# if page == "ML Explanation":
#     st.header("Machine Learning - Ensemble Model")

#     st.write("""
#     - Data Cleaning
#     - Extract Grams from Serving
#     - Random Forest + Gradient Boosting
#     - Voting Regressor
#     """)

#     st.subheader("Model Performance")
#     st.write(f"MAE: {ml_metrics['MAE']:.2f} kcal")
#     st.write(f"R² Score: {ml_metrics['R2']:.2f}")

# # ------------------ หน้าอธิบาย NN ------------------
# # if page == "NN Explanation":
# #     st.header("Neural Network - CNN Model")
# #     st.write("""
# #     - ใช้ Image Dataset
# #     - Normalize ภาพ
# #     - สร้าง CNN 2 Conv Layers
# #     - Softmax สำหรับ classification
# #     """)
# if page == "NN Explanation":
#     st.header("Neural Network - CNN Model")

#     st.write("""
#     - ImageDataGenerator
#     - 3 Convolution Layers
#     - Softmax Output
#     """)

#     st.subheader("Model Performance")
#     st.write(f"Accuracy: {cnn_metrics['Accuracy']:.2f}")

# # ------------------ หน้า ML ทำนาย ------------------
# # if page == "ML Prediction":
# #     # food_name = st.text_input("Enter Food Name")

# #     food_list = le.classes_
# #     # food_name = st.selectbox("Select Food", food_list)
# #     food_name = st.selectbox(
# #         "Select Food",
# #         food_list,
# #         key="ml_food_select"
# #     )
# #     # if st.button("Predict"):
# #     if st.button("Predict", key="ml_predict_btn"):
# #         encoded = le.transform([food_name])
# #         result = ensemble.predict([[encoded[0]]])
# #         st.success(f"Calorie Level: {result[0]}")
# # food_df = joblib.load("models/food_full_data.pkl")
# # if page == "ML Prediction":
# #     st.header("Calorie Prediction")

# #     food_list = le.classes_
# #     food_name = st.selectbox("Select Food", food_list, key="ml_food")

# #     if st.button("Predict", key="ml_btn"):
# #         encoded = le.transform([food_name])
# #         predicted_cal = ensemble.predict([[encoded[0]]])[0]

# #         st.success(f"Estimated Calories: {int(predicted_cal)} kcal")

# #         if predicted_cal < 150:
# #             st.info("Level: Low")
# #         elif predicted_cal < 300:
# #             st.info("Level: Medium")
# #         else:
# #             st.info("Level: High")
# food_df = joblib.load("models/food_full_data.pkl")

# if page == "ML Prediction":
#     st.header("Calorie Prediction")

#     food_list = le.classes_
#     food_name = st.selectbox("Select Food", food_list, key="ml_food")

#     if st.button("Predict", key="ml_btn"):

#         # -------------------
#         # 🔹 ดึงค่าจริงจาก database
#         # -------------------
#         row = food_df[food_df['Food'] == food_name]

#         if len(row) > 0:

#             actual_cal = row['Calories'].values[0]
#             grams = row['Grams'].values[0]

#             st.success(f"Calories: {int(actual_cal)} kcal")
#             st.write(f"Serving Size: {int(grams)} g")

#             cal_per_100g = (actual_cal / grams) * 100
#             st.write(f"Calories per 100g: {int(cal_per_100g)} kcal")

#             if actual_cal < 150:
#                 st.info("Level: Low")
#             elif actual_cal < 300:
#                 st.info("Level: Medium")
#             else:
#                 st.info("Level: High")

#         else:
#             st.warning("Food not found in database")

# # ------------------ หน้า NN ทำนาย ------------------
# # if page == "NN Prediction":
# #     uploaded = st.file_uploader("Upload Food Image")

# #     if uploaded:
# #         img = Image.open(uploaded).resize((384,384))
# #         img = np.array(img) / 255.0
# #         img = img.reshape(1,384,384,3)

# #         prediction = cnn_model.predict(img)
# #         st.success(f"Predicted Class: {np.argmax(prediction)}")
# # if page == "NN Prediction":
# #     st.header("Upload Food Image")

# #     uploaded = st.file_uploader("Upload Food Image", key="nn_upload")

# #     if uploaded:
# #         img = Image.open(uploaded).resize((128,128))
# #         img_array = np.array(img) / 255.0
# #         img_array = img_array.reshape(1,128,128,3)

# #         prediction = cnn_model.predict(img_array)
# #         predicted_class = np.argmax(prediction)

# #         st.success(f"Predicted Class Index: {predicted_class}")
# # class_names = joblib.load("models/cnn_class_names.pkl")

# # if page == "NN Prediction":
# #     st.header("Upload Food Image")

# #     uploaded = st.file_uploader("Upload Food Image", key="nn_upload")

# #     if uploaded:
# #         img = Image.open(uploaded).resize((128,128))
# #         img_array = np.array(img) / 255.0
# #         img_array = img_array.reshape(1,128,128,3)

# #         prediction = cnn_model.predict(img_array)
# #         # predicted_index = np.argmax(prediction)

# #         # predicted_food = class_names[predicted_index].decode("utf-8")
# #         predicted_index = np.argmax(prediction)
# #         predicted_food = class_names[predicted_index]

# #         st.success(f"Predicted Food: {predicted_food}")

# #         # เอาชื่ออาหารไปทำนายแคล
# #         # if predicted_food in le.classes_:
# #         #     encoded = le.transform([predicted_food])
# #         #     predicted_cal = ensemble.predict([[encoded[0]]])[0]

# #         #     st.success(f"Estimated Calories: {int(predicted_cal)} kcal")
# #         # else:
# #         #     st.warning("Food not found in calorie database")
# #         predicted_food_lower = predicted_food.lower()
# #         food_list_lower = [f.lower() for f in le.classes_]

# #         st.write(le.classes_)

        
# #         if predicted_food_lower in food_list_lower:
# #             match_index = food_list_lower.index(predicted_food_lower)
# #             matched_food = le.classes_[match_index]

# #             encoded = le.transform([matched_food])
# #             predicted_cal = ensemble.predict([[encoded[0]]])[0]

# #             st.success(f"Estimated Calories: {int(predicted_cal)} kcal")

# #             if predicted_cal < 150:
# #                 st.info("Level: Low")
# #             elif predicted_cal < 300:
# #                 st.info("Level: Medium")
# #             else:
# #                 st.info("Level: High")

# #         else:
# #             st.warning("Food not found in calorie database")
# class_names = joblib.load("models/cnn_class_names.pkl")

# if page == "NN Prediction":
#     st.header("Upload Food Image")

#     uploaded = st.file_uploader("Upload Food Image", key="nn_upload")

#     if uploaded:
#         img = Image.open(uploaded).resize((128,128))
#         img_array = np.array(img) / 255.0
#         img_array = img_array.reshape(1,128,128,3)

#         prediction = cnn_model.predict(img_array)
#         predicted_index = np.argmax(prediction)
#         predicted_food = class_names[predicted_index]

#         st.success(f"Predicted Food: {predicted_food}")

#         # -------------------------
#         # 🔎 หาอาหารที่มี keyword ตรงกัน
#         # -------------------------
#         matched_items = []

#         for food in le.classes_:
#             if predicted_food.lower() in food.lower():
#                 matched_items.append(food)

#         if len(matched_items) > 0:

#             # st.write("Matched Items in Database:")
#             # for item in matched_items:
#             #     st.write("-", item)

#             # -------------------------
#             # 🔥 เฉลี่ยแคลอรี่ทั้งหมด
#             # -------------------------
#             calories = []

#             for food in matched_items:
#                 encoded = le.transform([food])
#                 cal = ensemble.predict([[encoded[0]]])[0]
#                 calories.append(cal)

#             predicted_cal = sum(calories) / len(calories)

#             st.success(f"Average Estimated Calories: {int(predicted_cal)} kcal")

#             # แสดงระดับแคล
#             if predicted_cal < 150:
#                 st.info("Level: Low")
#             elif predicted_cal < 300:
#                 st.info("Level: Medium")
#             else:
#                 st.info("Level: High")

#         else:
#             st.warning("Food not found in calorie database")
# import streamlit as st
# import joblib
# import numpy as np
# from tensorflow.keras.models import load_model
# from PIL import Image

# st.title("Food Calorie Project")

# page = st.sidebar.selectbox(
#     "Select Page",
#     ["ML Explanation",
#      "NN Explanation",
#      "ML Prediction",
#      "NN Prediction"]
# )

# # ----------------------------
# # โหลดโมเดลและข้อมูล
# # ----------------------------
# ensemble = joblib.load("models/ensemble_model.pkl")
# cnn_model = load_model("models/cnn_model.h5")
# le = joblib.load("models/label_encoder.pkl")
# food_df = joblib.load("models/food_full_data.pkl")

# ml_metrics = joblib.load("models/ml_metrics.pkl")
# cnn_metrics = joblib.load("models/cnn_metrics.pkl")

# class_names = joblib.load("models/cnn_class_names.pkl")

# # ------------------ ML Explanation ------------------
# if page == "ML Explanation":
#     st.header("Machine Learning - Ensemble Model")
#     st.write("""
#     - Data Cleaning
#     - Extract Grams from Serving
#     - Random Forest + Gradient Boosting
#     - Voting Regressor
#     """)

#     st.subheader("Model Performance")
#     st.write(f"MAE: {ml_metrics['MAE']:.2f} kcal")
#     st.write(f"R² Score: {ml_metrics['R2']:.2f}")

# # ------------------ NN Explanation ------------------
# if page == "NN Explanation":
#     st.header("Neural Network - CNN Model")
#     st.write("""
#     - ImageDataGenerator
#     - 3 Convolution Layers
#     - Softmax Classification
#     """)

#     st.subheader("Model Performance")
#     st.write(f"Accuracy: {cnn_metrics['Accuracy']:.2f}")

# # ------------------ ML Prediction ------------------
# if page == "ML Prediction":
#     st.header("Calorie Prediction")

#     food_list = le.classes_
#     food_name = st.selectbox("Select Food", food_list)

#     if st.button("Predict"):

#         row = food_df[food_df['Food'] == food_name]

#         if len(row) > 0:

#             actual_cal = row['Calories'].values[0]
#             grams = row['Grams'].values[0]

#             st.success(f"Calories: {int(actual_cal)} kcal")
#             st.write(f"Serving Size: {int(grams)} g")

#             cal_per_100g = (actual_cal / grams) * 100
#             st.write(f"Calories per 100g: {int(cal_per_100g)} kcal")

#             if actual_cal < 150:
#                 st.info("Level: Low")
#             elif actual_cal < 300:
#                 st.info("Level: Medium")
#             else:
#                 st.info("Level: High")

#             # แสดง Model Performance
#             st.divider()
#             st.subheader("Model Performance")
#             st.write(f"ML MAE: {ml_metrics['MAE']:.2f} kcal")
#             st.write(f"ML R² Score: {ml_metrics['R2']:.2f}")

#         else:
#             st.warning("Food not found in database")

# # ------------------ NN Prediction ------------------
# if page == "NN Prediction":
#     st.header("Upload Food Image")

#     uploaded = st.file_uploader("Upload Food Image")

#     if uploaded:
#         img = Image.open(uploaded).resize((128,128))
#         img_array = np.array(img) / 255.0
#         img_array = img_array.reshape(1,128,128,3)

#         prediction = cnn_model.predict(img_array)
#         predicted_index = np.argmax(prediction)
#         confidence = np.max(prediction)

#         predicted_food = class_names[predicted_index]

#         st.success(f"Predicted Food: {predicted_food}")
#         st.write(f"Prediction Confidence: {confidence*100:.2f}%")

#         # -------------------------
#         # หาอาหารที่ตรง keyword
#         # -------------------------
#         matched_items = []

#         for food in le.classes_:
#             if predicted_food.lower() in food.lower():
#                 matched_items.append(food)

#         if len(matched_items) > 0:

#             calories = []

#             for food in matched_items:
#                 encoded = le.transform([food])
#                 cal = ensemble.predict([[encoded[0]]])[0]
#                 calories.append(cal)

#             predicted_cal = sum(calories) / len(calories)

#             st.success(f"Average Estimated Calories: {int(predicted_cal)} kcal")

#             if predicted_cal < 150:
#                 st.info("Level: Low")
#             elif predicted_cal < 300:
#                 st.info("Level: Medium")
#             else:
#                 st.info("Level: High")

#         else:
#             st.warning("Food not found in calorie database")

#         # แสดง Model Performance
#         st.divider()
#         st.subheader("Model Performance")
#         st.write(f"CNN Accuracy: {cnn_metrics['Accuracy']:.2f}")
#         st.write(f"ML R² Score: {ml_metrics['R2']:.2f}")
# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# from tensorflow.keras.models import load_model
# from PIL import Image

# st.title("Food Calorie Project")

# page = st.sidebar.selectbox(
#     "Select Page",
#     ["ML Explanation",
#      "NN Explanation",
#      "ML Prediction",
#      "NN Prediction"]
# )

# # ----------------------------
# # โหลดโมเดล
# # ----------------------------
# ensemble = joblib.load("models/ensemble_model.pkl")
# cnn_model = load_model("models/cnn_model.h5")
# food_df = joblib.load("models/food_full_data.pkl")
# ml_metrics = joblib.load("models/ml_metrics.pkl")
# cnn_metrics = joblib.load("models/cnn_metrics.pkl")
# class_names = joblib.load("models/cnn_class_names.pkl")
# feature_columns = joblib.load("models/feature_columns.pkl")

# # ------------------ ML Explanation ------------------
# if page == "ML Explanation":
#     st.header("Machine Learning - Calorie Level Classification")

#     st.write("""
#     - Data Cleaning
#     - Extract Grams from Serving
#     - One-Hot Encoding Food Name
#     - Random Forest + Gradient Boosting
#     - Soft Voting Ensemble
#     """)

#     st.subheader("Model Performance")
#     st.write(f"Accuracy: {ml_metrics['Accuracy']:.2f}")

# # ------------------ NN Explanation ------------------
# if page == "NN Explanation":
#     st.header("Neural Network - CNN Model")

#     st.write("""
#     - ImageDataGenerator
#     - 3 Convolution Layers
#     - Softmax Classification
#     """)

#     st.subheader("Model Performance")
#     st.write(f"Accuracy: {cnn_metrics['Accuracy']:.2f}")

# # ------------------ ML Prediction ------------------
# if page == "ML Prediction":
#     st.header("Calorie Level Prediction")

#     food_list = food_df['Food'].unique()
#     food_name = st.selectbox("Select Food", food_list)

#     if st.button("Predict"):

#         row = food_df[food_df['Food'] == food_name]

#         if len(row) > 0:

#             grams = row['Grams'].values[0]
#             actual_cal = row['Calories'].values[0]

#             # สร้าง input vector สำหรับโมเดล
#             input_data = pd.DataFrame(columns=feature_columns)
#             input_data.loc[0] = 0

#             input_data['Grams'] = grams

#             food_column = f"Food_{food_name}"
#             if food_column in input_data.columns:
#                 input_data[food_column] = 1

#             predicted_level = ensemble.predict(input_data)[0]

#             st.success(f"Predicted Calorie Level: {predicted_level}")

#             st.write(f"Actual Calories: {int(actual_cal)} kcal")
#             st.write(f"Serving Size: {int(grams)} g")

#             # แสดง Accuracy
#             st.divider()
#             st.subheader("Model Performance")
#             st.write(f"ML Accuracy: {ml_metrics['Accuracy']:.2f}")

#         else:
#             st.warning("Food not found")

# # ------------------ NN Prediction ------------------
# if page == "NN Prediction":
#     st.header("Upload Food Image")

#     uploaded = st.file_uploader("Upload Food Image")

#     if uploaded:
#         img = Image.open(uploaded).resize((128,128))
#         img_array = np.array(img) / 255.0
#         img_array = img_array.reshape(1,128,128,3)

#         prediction = cnn_model.predict(img_array)
#         predicted_index = np.argmax(prediction)
#         confidence = np.max(prediction)

#         predicted_food = class_names[predicted_index]

#         st.success(f"Predicted Food: {predicted_food}")
#         st.write(f"Prediction Confidence: {confidence*100:.2f}%")

#         # -------------------------
#         # ส่งชื่ออาหารเข้า ML Classification
#         # -------------------------
#         row = food_df[food_df['Food'].str.lower() == predicted_food.lower()]

#         if len(row) > 0:

#             grams = row['Grams'].values[0]

#             input_data = pd.DataFrame(columns=feature_columns)
#             input_data.loc[0] = 0

#             input_data['Grams'] = grams

#             food_column = f"Food_{row['Food'].values[0]}"
#             if food_column in input_data.columns:
#                 input_data[food_column] = 1

#             predicted_level = ensemble.predict(input_data)[0]

#             st.success(f"Predicted Calorie Level: {predicted_level}")

#         else:
#             st.warning("Food not found in ML database")

#         # แสดง Performance
#         st.divider()
#         st.subheader("Model Performance")
#         st.write(f"CNN Accuracy: {cnn_metrics['Accuracy']:.2f}")
#         st.write(f"ML Accuracy: {ml_metrics['Accuracy']:.2f}")
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.callbacks import EarlyStopping
# import joblib
# import os

# dataset_dir = "data/Food Classification dataset"

# # ----------------------------
# # Data Augmentation
# # ----------------------------
# datagen = ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2,
#     rotation_range=20,
#     zoom_range=0.2,
#     horizontal_flip=True
# )

# train_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(128,128),
#     batch_size=32,
#     class_mode='categorical',
#     subset='training'
# )

# val_generator = datagen.flow_from_directory(
#     dataset_dir,
#     target_size=(128,128),
#     batch_size=32,
#     class_mode='categorical',
#     subset='validation'
# )

# num_classes = len(train_generator.class_indices)

# # ----------------------------
# # CNN Model
# # ----------------------------
# model = Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
#     MaxPooling2D(2,2),

#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(2,2),

#     Conv2D(128, (3,3), activation='relu'),
#     MaxPooling2D(2,2),

#     Flatten(),
#     Dense(256, activation='relu'),
#     Dropout(0.5),
#     Dense(num_classes, activation='softmax')
# ])

# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# # ----------------------------
# # Early Stopping
# # ----------------------------
# early_stop = EarlyStopping(
#     monitor='val_loss',
#     patience=3,
#     restore_best_weights=True
# )

# # ----------------------------
# # Train
# # ----------------------------
# model.fit(
#     train_generator,
#     epochs=20,
#     validation_data=val_generator,
#     callbacks=[early_stop]
# )

# # ----------------------------
# # Evaluate
# # ----------------------------
# loss, acc = model.evaluate(val_generator)
# print("Validation Accuracy:", acc)

# # ----------------------------
# # Save Model
# # ----------------------------
# os.makedirs("models", exist_ok=True)

# model.save("models/cnn_model.h5")

# class_names = list(train_generator.class_indices.keys())
# joblib.dump(class_names, "models/cnn_class_names.pkl")

# cnn_metrics = {
#     "Accuracy": float(acc)
# }
# joblib.dump(cnn_metrics, "models/cnn_metrics.pkl")

# print("CNN Model saved successfully!")
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import difflib
from tensorflow.keras.models import load_model
from PIL import Image


st.title("Food Calorie AI System")

page = st.sidebar.selectbox(
    "Select Page",
    ["ML Explanation",
     "NN Explanation",
     "ML Prediction",
     "NN Prediction"]
)

# ----------------------------
# Load Models (cache)
# ----------------------------
@st.cache_resource
def load_models():
    ensemble = joblib.load("models/ensemble_model.pkl")
    cnn_model = load_model("models/cnn_model.h5")
    food_df = joblib.load("models/food_full_data.pkl")
    ml_metrics = joblib.load("models/ml_metrics.pkl")
    cnn_metrics = joblib.load("models/cnn_metrics.pkl")
    class_names = joblib.load("models/cnn_class_names.pkl")
    feature_columns = joblib.load("models/feature_columns.pkl")

    return ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns

ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns = load_models()

# ----------------------------
# Helper Function
# ----------------------------
def predict_calorie_level(food_name, grams):
    input_data = pd.DataFrame(columns=feature_columns)
    input_data.loc[0] = 0

    if 'Grams' in input_data.columns:
        input_data['Grams'] = grams

    food_column = f"Food_{food_name}"
    if food_column in input_data.columns:
        input_data[food_column] = 1

    return ensemble.predict(input_data)[0]

# ------------------ ML Explanation ------------------
if page == "ML Explanation":
    st.header("Machine Learning - Calorie Level Classification")

    st.write("""
    - Data Cleaning
    - One-Hot Encoding
    - Random Forest + Gradient Boosting
    - Soft Voting Ensemble
    """)

    st.subheader("Model Performance")
    st.write(f"Accuracy: {ml_metrics['Accuracy']:.2f}")

# ------------------ NN Explanation ------------------
if page == "NN Explanation":
    st.header("Neural Network - CNN Food Classification")

    st.write("""
    - Data Augmentation
    - 3 Convolution Layers
    - Dropout Regularization
    - Softmax Output
    """)

    st.subheader("Model Performance")
    st.write(f"Accuracy: {cnn_metrics['Accuracy']:.2f}")

# ------------------ ML Prediction ------------------
if page == "ML Prediction":
    st.header("Calorie Level Prediction")

    food_list = sorted(food_df['Food'].unique())
    food_name = st.selectbox("Select Food", food_list)

    if st.button("Predict"):

        row = food_df[food_df['Food'] == food_name]

        if len(row) > 0:
            grams = row['Grams'].values[0]
            actual_cal = row['Calories'].values[0]

            predicted_level = predict_calorie_level(food_name, grams)

            st.success(f"Predicted Calorie Level: {predicted_level}")
            st.write(f"Actual Calories: {int(actual_cal)} kcal")
            st.write(f"Serving Size: {int(grams)} g")

            st.divider()
            st.write(f"ML Accuracy: {ml_metrics['Accuracy']:.2f}")

# ------------------ NN Prediction ------------------
if page == "NN Prediction":
    st.header("Upload Food Image")

    uploaded = st.file_uploader("Upload Food Image")

    if uploaded:
        # img = Image.open(uploaded).resize((128,128))
        # img_array = np.array(img) / 255.0
        # img_array = img_array.reshape(1,128,128,3)
        IMG_SIZE = 160   # ต้องตรงกับตอนเทรน

        img = Image.open(uploaded).resize((IMG_SIZE, IMG_SIZE))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = cnn_model.predict(img_array)
        predicted_index = np.argmax(prediction)
        confidence = np.max(prediction)

        predicted_food = class_names[predicted_index]

        st.success(f"Predicted Food: {predicted_food}")
        st.write(f"Confidence: {confidence*100:.2f}%")

        # row = food_df[food_df['Food'].str.lower() == predicted_food.lower()]
        food_list = food_df['Food'].tolist()
        match = difflib.get_close_matches(predicted_food, food_list, n=1, cutoff=0.5)

        if match:
            matched_food = match[0]
            row = food_df[food_df['Food'] == matched_food]

        if len(row) > 0:
            grams = row['Grams'].values[0]
            predicted_level = predict_calorie_level(row['Food'].values[0], grams)

            st.success(f"Predicted Calorie Level: {predicted_level}")
        else:
            st.warning("Food not found in ML database")

        st.divider()
        st.write(f"CNN Accuracy: {cnn_metrics['Accuracy']:.2f}")
        st.write(f"ML Accuracy: {ml_metrics['Accuracy']:.2f}")