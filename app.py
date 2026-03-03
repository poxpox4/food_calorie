import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

st.title("Food Calorie Project")

page = st.sidebar.selectbox(
    "Select Page",
    ["ML Explanation",
     "NN Explanation",
     "ML Prediction",
     "NN Prediction"]
)

# โหลดโมเดล
ensemble = joblib.load("models/ensemble_model.pkl")
cnn_model = load_model("models/cnn_model.h5")
le = joblib.load("models/label_encoder.pkl")

# ------------------ หน้าอธิบาย ML ------------------
if page == "ML Explanation":
    st.header("Machine Learning - Ensemble Model")
    st.write("""
    - ทำ Data Cleaning
    - แปลง Calories เป็นตัวเลข
    - แบ่ง Low / Medium / High
    - ใช้ Random Forest + Gradient Boosting
    - ทำ Voting Ensemble
    """)

# ------------------ หน้าอธิบาย NN ------------------
if page == "NN Explanation":
    st.header("Neural Network - CNN Model")
    st.write("""
    - ใช้ Image Dataset
    - Normalize ภาพ
    - สร้าง CNN 2 Conv Layers
    - Softmax สำหรับ classification
    """)

# ------------------ หน้า ML ทำนาย ------------------
# if page == "ML Prediction":
#     # food_name = st.text_input("Enter Food Name")

#     food_list = le.classes_
#     # food_name = st.selectbox("Select Food", food_list)
#     food_name = st.selectbox(
#         "Select Food",
#         food_list,
#         key="ml_food_select"
#     )
#     # if st.button("Predict"):
#     if st.button("Predict", key="ml_predict_btn"):
#         encoded = le.transform([food_name])
#         result = ensemble.predict([[encoded[0]]])
#         st.success(f"Calorie Level: {result[0]}")
if page == "ML Prediction":
    st.header("Calorie Prediction")

    food_list = le.classes_
    food_name = st.selectbox("Select Food", food_list, key="ml_food")

    if st.button("Predict", key="ml_btn"):
        encoded = le.transform([food_name])
        predicted_cal = ensemble.predict([[encoded[0]]])[0]

        st.success(f"Estimated Calories: {int(predicted_cal)} kcal")

        if predicted_cal < 150:
            st.info("Level: Low")
        elif predicted_cal < 300:
            st.info("Level: Medium")
        else:
            st.info("Level: High")

# ------------------ หน้า NN ทำนาย ------------------
# if page == "NN Prediction":
#     uploaded = st.file_uploader("Upload Food Image")

#     if uploaded:
#         img = Image.open(uploaded).resize((384,384))
#         img = np.array(img) / 255.0
#         img = img.reshape(1,384,384,3)

#         prediction = cnn_model.predict(img)
#         st.success(f"Predicted Class: {np.argmax(prediction)}")
# if page == "NN Prediction":
#     st.header("Upload Food Image")

#     uploaded = st.file_uploader("Upload Food Image", key="nn_upload")

#     if uploaded:
#         img = Image.open(uploaded).resize((128,128))
#         img_array = np.array(img) / 255.0
#         img_array = img_array.reshape(1,128,128,3)

#         prediction = cnn_model.predict(img_array)
#         predicted_class = np.argmax(prediction)

#         st.success(f"Predicted Class Index: {predicted_class}")
class_names = joblib.load("models/cnn_class_names.pkl")

if page == "NN Prediction":
    st.header("Upload Food Image")

    uploaded = st.file_uploader("Upload Food Image", key="nn_upload")

    if uploaded:
        img = Image.open(uploaded).resize((128,128))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1,128,128,3)

        prediction = cnn_model.predict(img_array)
        predicted_index = np.argmax(prediction)

        predicted_food = class_names[predicted_index].decode("utf-8")

        st.success(f"Predicted Food: {predicted_food}")

        # เอาชื่ออาหารไปทำนายแคล
        if predicted_food in le.classes_:
            encoded = le.transform([predicted_food])
            predicted_cal = ensemble.predict([[encoded[0]]])[0]

            st.success(f"Estimated Calories: {int(predicted_cal)} kcal")
        else:
            st.warning("Food not found in calorie database")