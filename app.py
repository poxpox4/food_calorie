
# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# import difflib
# from tensorflow.keras.models import load_model
# from PIL import Image

# st.set_page_config(
#     page_title="Food Calorie AI",
#     page_icon="🍽️",
#     layout="wide"
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600&display=swap');

# html, body, [class*="css"] {
#     font-family: 'DM Sans', sans-serif;
# }

# /* Background */
# .stApp {
#     background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #16213e 100%);
#     color: #f0ece2;
# }

# /* Hide default streamlit elements */
# #MainMenu, footer, header {visibility: hidden;}
# .block-container {padding-top: 2rem; padding-bottom: 2rem;}

# /* Hero Title */
# .hero-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 3.2rem;
#     font-weight: 700;
#     background: linear-gradient(90deg, #f9c74f, #f3722c, #f94144);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     text-align: center;
#     margin-bottom: 0.2rem;
#     line-height: 1.2;
# }

# .hero-subtitle {
#     text-align: center;
#     color: #9e9e9e;
#     font-size: 1rem;
#     letter-spacing: 0.15em;
#     text-transform: uppercase;
#     margin-bottom: 2.5rem;
# }

# /* Nav buttons container */
# .nav-container {
#     display: flex;
#     justify-content: center;
#     gap: 12px;
#     flex-wrap: wrap;
#     margin-bottom: 2.5rem;
# }

# /* Nav button base */
# .nav-btn {
#     padding: 10px 22px;
#     border-radius: 50px;
#     border: 1.5px solid rgba(255,255,255,0.15);
#     background: rgba(255,255,255,0.05);
#     color: #ccc;
#     font-family: 'DM Sans', sans-serif;
#     font-size: 0.88rem;
#     font-weight: 500;
#     cursor: pointer;
#     transition: all 0.2s ease;
#     white-space: nowrap;
# }

# /* Active nav button */
# .nav-btn-active {
#     background: linear-gradient(135deg, #f9c74f, #f3722c);
#     border-color: transparent;
#     color: #0f0f0f;
#     font-weight: 600;
#     box-shadow: 0 4px 20px rgba(249,199,79,0.35);
# }

# /* Section card */
# .section-card {
#     background: rgba(255,255,255,0.04);
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 16px;
#     padding: 1.8rem 2rem;
#     margin-bottom: 1.2rem;
# }

# .section-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 1.15rem;
#     color: #f9c74f;
#     margin-bottom: 0.8rem;
#     display: flex;
#     align-items: center;
#     gap: 8px;
# }

# /* Metric cards */
# .metric-row {
#     display: flex;
#     gap: 16px;
#     flex-wrap: wrap;
#     margin-top: 0.5rem;
# }

# .metric-card {
#     flex: 1;
#     min-width: 140px;
#     background: linear-gradient(135deg, rgba(249,199,79,0.12), rgba(243,114,44,0.08));
#     border: 1px solid rgba(249,199,79,0.2);
#     border-radius: 12px;
#     padding: 1rem 1.2rem;
#     text-align: center;
# }

# .metric-value {
#     font-size: 2rem;
#     font-weight: 700;
#     color: #f9c74f;
#     line-height: 1;
# }

# .metric-label {
#     font-size: 0.78rem;
#     color: #9e9e9e;
#     margin-top: 4px;
#     text-transform: uppercase;
#     letter-spacing: 0.1em;
# }

# /* Step list */
# .step-item {
#     display: flex;
#     align-items: flex-start;
#     gap: 14px;
#     padding: 10px 0;
#     border-bottom: 1px solid rgba(255,255,255,0.05);
# }
# .step-item:last-child { border-bottom: none; }

# .step-num {
#     width: 28px;
#     height: 28px;
#     min-width: 28px;
#     border-radius: 50%;
#     background: linear-gradient(135deg, #f9c74f, #f3722c);
#     color: #0f0f0f;
#     font-weight: 700;
#     font-size: 0.8rem;
#     display: flex;
#     align-items: center;
#     justify-content: center;
# }

# .step-text { color: #d0cfc8; font-size: 0.92rem; line-height: 1.5; }

# /* Tag badges */
# .tag {
#     display: inline-block;
#     padding: 4px 12px;
#     background: rgba(249,199,79,0.12);
#     border: 1px solid rgba(249,199,79,0.25);
#     border-radius: 20px;
#     color: #f9c74f;
#     font-size: 0.8rem;
#     margin: 3px;
# }

# /* Model badges */
# .model-badge {
#     display: inline-flex;
#     align-items: center;
#     gap: 6px;
#     padding: 6px 14px;
#     border-radius: 8px;
#     background: rgba(255,255,255,0.06);
#     border: 1px solid rgba(255,255,255,0.1);
#     color: #e0ddd5;
#     font-size: 0.85rem;
#     margin: 4px;
# }

# /* Reference links */
# .ref-item {
#     padding: 10px 14px;
#     border-left: 3px solid #f3722c;
#     background: rgba(243,114,44,0.06);
#     border-radius: 0 8px 8px 0;
#     margin-bottom: 8px;
#     font-size: 0.88rem;
#     color: #ccc;
# }

# /* Prediction result */
# .result-low {
#     background: linear-gradient(135deg, rgba(76,175,80,0.2), rgba(76,175,80,0.05));
#     border: 1px solid rgba(76,175,80,0.4);
#     border-radius: 12px;
#     padding: 1.2rem 1.5rem;
#     text-align: center;
# }
# .result-medium {
#     background: linear-gradient(135deg, rgba(255,193,7,0.2), rgba(255,193,7,0.05));
#     border: 1px solid rgba(255,193,7,0.4);
#     border-radius: 12px;
#     padding: 1.2rem 1.5rem;
#     text-align: center;
# }
# .result-high {
#     background: linear-gradient(135deg, rgba(244,67,54,0.2), rgba(244,67,54,0.05));
#     border: 1px solid rgba(244,67,54,0.4);
#     border-radius: 12px;
#     padding: 1.2rem 1.5rem;
#     text-align: center;
# }
# .result-label { font-size: 0.8rem; color: #9e9e9e; text-transform: uppercase; letter-spacing: 0.1em; }
# .result-value { font-size: 2rem; font-weight: 700; margin-top: 4px; }

# /* Streamlit widget overrides */
# .stSelectbox > div > div {
#     background: rgba(255,255,255,0.07) !important;
#     border: 1px solid rgba(255,255,255,0.15) !important;
#     border-radius: 10px !important;
#     color: #f0ece2 !important;
# }
# .stButton > button {
#     background: linear-gradient(135deg, #f9c74f, #f3722c) !important;
#     color: #0f0f0f !important;
#     border: none !important;
#     border-radius: 50px !important;
#     font-weight: 600 !important;
#     padding: 0.6rem 2rem !important;
#     font-size: 0.95rem !important;
#     width: 100% !important;
#     transition: all 0.2s ease !important;
#     box-shadow: 0 4px 20px rgba(249,199,79,0.3) !important;
# }
# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 6px 25px rgba(249,199,79,0.45) !important;
# }
# .stFileUploader > div {
#     background: rgba(255,255,255,0.04) !important;
#     border: 2px dashed rgba(249,199,79,0.3) !important;
#     border-radius: 12px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---- Hero Header ----
# st.markdown('<div class="hero-title">🍽️ Food Calorie AI System</div>', unsafe_allow_html=True)
# st.markdown('<div class="hero-subtitle">Machine Learning & Neural Network · Calorie Intelligence</div>', unsafe_allow_html=True)

# # ---- Navigation ----
# if "page" not in st.session_state:
#     st.session_state.page = "ML Explanation"

# pages = ["ML Explanation", "NN Explanation", "ML Prediction", "NN Prediction"]
# icons = ["🤖", "🧠", "🔍", "📷"]

# cols = st.columns(len(pages))
# for i, (p, icon) in enumerate(zip(pages, icons)):
#     with cols[i]:
#         is_active = st.session_state.page == p
#         if st.button(f"{icon} {p}", key=f"nav_{p}", use_container_width=True):
#             st.session_state.page = p
#             st.rerun()

# page = st.session_state.page

# st.markdown("---")

# # ----------------------------
# # Load Models (cache)
# # ----------------------------

# @st.cache_resource
# def load_models():

#     ensemble = joblib.load("models/ensemble_model.pkl")
#     cnn_model = load_model("models/cnn_model.h5")
#     food_df = joblib.load("models/food_full_data.pkl")

#     ml_metrics = joblib.load("models/ml_metrics.pkl")
#     cnn_metrics = joblib.load("models/cnn_metrics.pkl")

#     class_names = joblib.load("models/cnn_class_names.pkl")
#     feature_columns = joblib.load("models/feature_columns.pkl")

#     return ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns


# ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns = load_models()

# # ----------------------------
# # Helper Function
# # ----------------------------

# # def predict_calorie_level(food_name, grams):

# #     input_data = pd.DataFrame(columns=feature_columns)
# #     input_data.loc[0] = 0

# #     if "Grams" in input_data.columns:
# #         input_data["Grams"] = grams

# #     food_column = f"Food_{food_name}"

# #     if food_column in input_data.columns:
# #         input_data[food_column] = 1

# #     prediction = ensemble.predict(input_data)

# #     return prediction[0]
# def predict_calorie_level(food_name, grams):

#     input_data = pd.DataFrame(columns=feature_columns)
#     input_data.loc[0] = 0

#     if "Grams" in input_data.columns:
#         input_data["Grams"] = grams

#     food_column = f"Food_{food_name}"

#     if food_column in input_data.columns:
#         input_data[food_column] = 1

#     pred = ensemble.predict(input_data)[0]

#     label_map = {
#         0: "Low",
#         1: "Medium",
#         2: "High"
#     }

#     return label_map.get(pred, "Unknown")


# # ------------------ ML Explanation ------------------

# # if page == "ML Explanation":

# #     st.header("Machine Learning - Calorie Level Classification")

# #     st.write("""
# #     Model pipeline:

# #     1. Data Cleaning
# #     2. One-Hot Encoding
# #     3. Random Forest
# #     4. Gradient Boosting
# #     5. Soft Voting Ensemble
# #     """)

# #     st.subheader("Model Performance")

# #     # st.write(f"Accuracy: {ml_metrics['Accuracy']:.2f}")
# #     st.write(f"ML Accuracy: {ml_metrics['Accuracy']*100:.2f}%")
# if page == "ML Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🤖 Machine Learning — Calorie Level Classification</div>
#         <p style="color:#c8c4bc; line-height:1.7;">
#         ระบบ Machine Learning นี้ถูกพัฒนาขึ้นเพื่อทำนาย <b style="color:#f9c74f;">ระดับพลังงาน (Calorie Level)</b> ของอาหาร
#          ซึ่งรวมโมเดลหลายตัวเข้าด้วยกันเพื่อเพิ่มความแม่นยำ
#         </p>
#         <p style="color:#c8c4bc; line-height:1.7;">โมเดลจะทำการจำแนกระดับพลังงานออกเป็น 3 ระดับ</p>
#         <div style="margin-top:12px;">
#             <span class="tag">🟢 Low</span>
#             <span class="tag">🟡 Medium</span>
#             <span class="tag">🔴 High</span>
#         </div>
#         <p style="color:#c8c4bc; line-height:1.7;">ระบบนี้ถูกสร้างขึ้นโดยใช้เทคนิค <b style="color:#f9c74f;">Ensemble Learning</b> ซึ่งเป็นการรวมโมเดลหลายตัวเข้าด้วยกัน 
#          เพื่อเพิ่มความแม่นยำของการทำนาย</p>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <p style="color:#9e9e9e; font-size:0.85rem; margin-bottom:10px;">ข้อมูลจาก 2 ไฟล์ที่รวมกัน</p>
#             <div class="model-badge">📄 calorie_infos.csv</div>
#             <div class="model-badge">📄 Food and Calories - Sheet1.csv</div>
#             <p style="color:#c8c4bc; font-size:0.88rem; margin-top:12px; line-height:1.6;">
#             Features: <span style="color:#f9c74f;">Food Name</span> · <span style="color:#f9c74f;">Serving Size</span> · <span style="color:#f9c74f;">Calories</span>
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">⚙️ Feature Engineering</div>
#             <p style="color:#c8c4bc; font-size:0.88rem; line-height:1.7;">
#             Feature หลักที่ใช้ในการฝึกโมเดล ได้แก่ <b style="color:#f9c74f;">Food Name</b> และ <b style="color:#f9c74f;">Serving Size (Grams)</b><br><br>
#             เนื่องจาก Food Name เป็นข้อมูลประเภทข้อความ จึงใช้เทคนิค
#             <span style="color:#f9c74f;">One-Hot Encoding</span> เพื่อแปลงให้เป็นตัวเลข
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🧹 Data Preprocessing</div>
#         """, unsafe_allow_html=True)
#         steps = [
#             "รวม Dataset จากหลายไฟล์",
#             "ลบข้อมูลที่มีค่า Missing",
#             "แปลง Serving Size ให้เป็นหน่วยกรัม",
#             "แปลงค่า Calories ให้อยู่ในรูปตัวเลข",
#             "ลบข้อมูลซ้ำ (Drop Duplicates)",
#         ]
#         steps_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(steps)])
#         st.markdown(steps_html + "</div>", unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🧩 Machine Learning Models</div>
#             <p style="color:#c8c4bc; font-size:0.85rem; margin-top:12px; line-height:1.6;">โมเดล Machine Learning ที่ใช้ประกอบด้วย</p>
#             <div class="model-badge">🌲 Random Forest Classifier</div>
#             <div class="model-badge">📈 Gradient Boosting Classifier</div>
#             <div class="model-badge">📐 Logistic Regression</div>
#             <p style="color:#c8c4bc; font-size:0.85rem; margin-top:12px; line-height:1.6;">
#             รวมด้วยเทคนิค <b style="color:#f9c74f;">Soft Voting Ensemble</b> —
#             จะคำนวณค่า Probability จากทุกโมเดล จากนั้นเลือกคลาสที่มีค่า Probability สูงที่สุดเป็นผลลัพธ์สุดท้าย
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{ml_metrics['Accuracy']*100:.1f}%</div>
#                 <div class="metric-label">Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <div class="ref-item">📊 <b>Dataset 1:</b> Calories in Food Items — <a href="https://www.kaggle.com/datasets/syedjaferk/calories-in-food-items-per-100gm-ounce-serving" target="_blank" style="color:#f9c74f;">Kaggle · syedjaferk</a></div>
#         <div class="ref-item">📊 <b>Dataset 2:</b> Food and Their Calories — <a href="https://www.kaggle.com/datasets/vaishnavivenkatesan/food-and-their-calories" target="_blank" style="color:#f9c74f;">Kaggle · vaishnavivenkatesan</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Scikit-learn — <a href="https://scikit-learn.org" target="_blank" style="color:#f9c74f;">scikit-learn.org</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Pandas — <a href="https://pandas.pydata.org" target="_blank" style="color:#f9c74f;">pandas.pydata.org</a> &nbsp;|&nbsp; NumPy — <a href="https://numpy.org" target="_blank" style="color:#f9c74f;">numpy.org</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ NN Explanation ------------------

# # elif page == "NN Explanation":

# #     st.header("Neural Network - CNN Food Classification")

# #     st.write("""
# #     CNN Architecture:

# #     • Image Resize (160x160)  
# #     • Data Augmentation  
# #     • 3 Convolution Layers  
# #     • MaxPooling  
# #     • Dropout Regularization  
# #     • Softmax Output Layer
# #     """)

# #     st.subheader("Model Performance")

# #     # st.write(f"Accuracy: {cnn_metrics['Accuracy']:.2f}")
# #     st.write(f"NN Accuracy: {cnn_metrics['Accuracy']*100:.2f}%")
# elif page == "NN Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🧠 Neural Network — Food Image Classification</div>
#         <p style="color:#c8c4bc; line-height:1.7;">
#         โมเดล Neural Network ถูกพัฒนาขึ้นเพื่อ <b style="color:#f9c74f;">จำแนกประเภทของอาหารจากรูปภาพ</b>
#         โดยใช้เทคนิค <b style="color:#f9c74f;">Convolutional Neural Network (CNN)</b>
#         ซึ่งเหมาะสำหรับงาน Computer Vision และการจำแนกรูปภาพโดยเฉพาะ
#         </p>
#         <div style="margin-top:12px;">
#             <span class="tag">🍕 Pizza</span>
#             <span class="tag">🍔 Burger</span>
#             <span class="tag">🥗 Salad</span>
#             <span class="tag">🍜 Noodles</span>
#             <span class="tag">🍚 Fried Rice</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <div class="model-badge">🖼️ Food Image Classification Dataset</div>
#             <p style="color:#c8c4bc; font-size:0.88rem; margin-top:10px; line-height:1.6;">
#             รูปภาพอาหารหลายประเภทจาก Kaggle ใช้สำหรับฝึกโมเดลให้จำแนกประเภทอาหารจากภาพได้
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🖼️ Image Preprocessing</div>
#         """, unsafe_allow_html=True)
#         pre_steps = [
#             "Resize ภาพให้เป็นขนาด 160×160 pixels",
#             "Normalize ค่า Pixel ให้อยู่ในช่วง 0–1",
#             "Data Augmentation: Rotation, Flip, Zoom, Brightness",
#         ]
#         pre_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pre_steps)])
#         st.markdown(pre_html + "</div>", unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🏗️ CNN Architecture</div>
#         """, unsafe_allow_html=True)
#         arch_steps = [
#             "Convolution Layer — สกัด Feature จากภาพ",
#             "ReLU Activation — เพิ่ม Non-linearity",
#             "MaxPooling Layer — ลด Dimension",
#             "Dropout Layer — ป้องกัน Overfitting",
#             "Fully Connected Layer — รวมข้อมูล",
#             "Softmax Output — จำแนกประเภทอาหาร",
#         ]
#         arch_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(arch_steps)])
#         st.markdown(arch_html + "</div>", unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">⚡ Prediction Process</div>
#         """, unsafe_allow_html=True)
#         pred_steps = [
#             "Upload รูปอาหาร",
#             "Resize & Normalize ภาพ",
#             "CNN ทำนายประเภทอาหาร",
#             "ค้นหาชื่ออาหารใน Dataset",
#             "ML ทำนายระดับแคลอรี่",
#         ]
#         pred_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pred_steps)])
#         st.markdown(pred_html + '<p style="color:#9e9e9e;font-size:0.82rem;margin-top:10px;">🔀 Hybrid AI System — NN + ML ทำงานร่วมกัน</p></div>', unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{cnn_metrics['Accuracy']*100:.1f}%</div>
#                 <div class="metric-label">Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <div class="ref-item">🖼️ <b>Dataset:</b> Food Image Classification Dataset — <a href="https://www.kaggle.com/datasets/harishkumardatalab/food-image-classification-dataset" target="_blank" style="color:#f9c74f;">Kaggle · harishkumardatalab</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> TensorFlow / Keras — <a href="https://www.tensorflow.org" target="_blank" style="color:#f9c74f;">tensorflow.org</a></div>
#         <div class="ref-item">📚 <b>Algorithm:</b> Convolutional Neural Network — LeCun et al., 1998</div>
#         <div class="ref-item">🔧 <b>Augmentation:</b> Keras ImageDataGenerator — <a href="https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator" target="_blank" style="color:#f9c74f;">TF Docs</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ ML Prediction ------------------

# elif page == "ML Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔍 Calorie Level Prediction</div>
#         <p style="color:#9e9e9e; font-size:0.88rem;">เลือกชื่ออาหารเพื่อทำนายระดับแคลอรี่ด้วย ML Ensemble Model</p>
#     </div>
#     """, unsafe_allow_html=True)

#     food_list = sorted(food_df["Food"].unique())
#     food_name = st.selectbox("🍽️ Select Food", food_list)

#     if st.button("✨ Predict Calorie Level"):

#         row = food_df[food_df["Food"] == food_name]

#         if len(row) > 0:
#             grams = row["Grams"].values[0]
#             actual_cal = row["Calories"].values[0]
#             predicted_level = predict_calorie_level(food_name, grams)

#             level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#             color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))

#             st.markdown(f"""
#             <div style="background:rgba({','.join(str(int(color.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.15);
#                         border:1px solid {color}66; border-radius:16px; padding:1.5rem 2rem;
#                         text-align:center; margin: 1rem 0;">
#                 <div style="font-size:0.8rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Predicted Calorie Level</div>
#                 <div style="font-size:3rem; margin: 0.3rem 0;">{emoji}</div>
#                 <div style="font-size:2.2rem; font-weight:700; color:{color};">{predicted_level}</div>
#             </div>
#             """, unsafe_allow_html=True)

#             c1, c2, c3 = st.columns(3)
#             with c1:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(actual_cal)}</div><div class="metric-label">Actual kcal</div></div>""", unsafe_allow_html=True)
#             with c2:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(grams)}g</div><div class="metric-label">Serving Size</div></div>""", unsafe_allow_html=True)
#             with c3:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{ml_metrics['Accuracy']*100:.1f}%</div><div class="metric-label">ML Accuracy</div></div>""", unsafe_allow_html=True)

#         else:
#             st.warning("Food not found in dataset")


# # ------------------ NN Prediction ------------------

# elif page == "NN Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">📷 Food Image Classification</div>
#         <p style="color:#9e9e9e; font-size:0.88rem;">อัปโหลดรูปภาพอาหาร — CNN จะจำแนกประเภท แล้ว ML จะทำนายระดับแคลอรี่</p>
#     </div>
#     """, unsafe_allow_html=True)

#     uploaded = st.file_uploader("📁 Upload Food Image (JPG / PNG)", type=["jpg", "jpeg", "png"])

#     if uploaded:

#         col1, col2 = st.columns([1, 1.5])

#         with col1:
#             img_display = Image.open(uploaded).convert("RGB")
#             st.image(img_display, caption="Uploaded Image", use_container_width=True)

#         with col2:
#             IMG_SIZE = 160
#             img = img_display.resize((IMG_SIZE, IMG_SIZE))
#             img_array = np.array(img) / 255.0
#             img_array = np.expand_dims(img_array, axis=0)

#             prediction = cnn_model.predict(img_array)
#             predicted_index = np.argmax(prediction)
#             confidence = np.max(prediction)
#             predicted_food = class_names[predicted_index]

#             st.markdown(f"""
#             <div class="section-card" style="margin-top:0;">
#                 <div class="section-title">🍽️ Predicted Food</div>
#                 <div style="font-size:1.8rem; font-weight:700; color:#f9c74f; margin: 8px 0;">{predicted_food}</div>
#                 <div style="color:#9e9e9e; font-size:0.85rem;">Confidence: <b style="color:#f3722c;">{confidence*100:.1f}%</b></div>
#             </div>
#             """, unsafe_allow_html=True)

#             row = pd.DataFrame()
#             food_list = food_df["Food"].tolist()
#             match = difflib.get_close_matches(predicted_food, food_list, n=1, cutoff=0.5)

#             if match:
#                 matched_food = match[0]
#                 row = food_df[food_df["Food"] == matched_food]

#             if len(row) > 0:
#                 grams = row["Grams"].values[0]
#                 predicted_level = predict_calorie_level(row["Food"].values[0], grams)

#                 level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#                 color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))

#                 st.markdown(f"""
#                 <div style="background:rgba({','.join(str(int(color.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.15);
#                             border:1px solid {color}66; border-radius:12px; padding:1.2rem;
#                             text-align:center; margin-top: 0.8rem;">
#                     <div style="font-size:0.75rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Calorie Level</div>
#                     <div style="font-size:1.8rem; margin:4px 0;">{emoji}</div>
#                     <div style="font-size:1.8rem; font-weight:700; color:{color};">{predicted_level}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#             else:
#                 st.warning("Food not found in ML database")

#             st.markdown(f"""
#             <div class="metric-card" style="margin-top:12px; text-align:left;">
#                 <span style="color:#9e9e9e; font-size:0.8rem;">NN Accuracy: </span>
#                 <b style="color:#f9c74f;">{cnn_metrics['Accuracy']*100:.1f}%</b>
#             </div>
#             """, unsafe_allow_html=True)

# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# import difflib
# from tensorflow.keras.models import load_model
# from PIL import Image

# st.set_page_config(
#     page_title="Food Calorie AI",
#     page_icon="🍽️",
#     layout="wide"
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600&display=swap');

# html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

# .stApp {
#     background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #16213e 100%);
#     color: #f0ece2;
# }

# #MainMenu, footer, header {visibility: hidden;}
# .block-container {padding-top: 2rem; padding-bottom: 2rem;}

# .hero-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 3.2rem;
#     font-weight: 700;
#     background: linear-gradient(90deg, #f9c74f, #f3722c, #f94144);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     text-align: center;
#     margin-bottom: 0.2rem;
#     line-height: 1.2;
# }

# .hero-subtitle {
#     text-align: center;
#     color: #9e9e9e;
#     font-size: 1rem;
#     letter-spacing: 0.15em;
#     text-transform: uppercase;
#     margin-bottom: 2.5rem;
# }

# .section-card {
#     background: rgba(255,255,255,0.04);
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 16px;
#     padding: 1.8rem 2rem;
#     margin-bottom: 1.2rem;
# }

# .section-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 1.15rem;
#     color: #f9c74f;
#     margin-bottom: 0.8rem;
#     display: flex;
#     align-items: center;
#     gap: 8px;
# }

# .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 0.5rem; }

# .metric-card {
#     flex: 1;
#     min-width: 140px;
#     background: linear-gradient(135deg, rgba(249,199,79,0.12), rgba(243,114,44,0.08));
#     border: 1px solid rgba(249,199,79,0.2);
#     border-radius: 12px;
#     padding: 1rem 1.2rem;
#     text-align: center;
# }

# .metric-value { font-size: 2rem; font-weight: 700; color: #f9c74f; line-height: 1; }
# .metric-label { font-size: 0.78rem; color: #9e9e9e; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.1em; }

# .step-item {
#     display: flex;
#     align-items: flex-start;
#     gap: 14px;
#     padding: 10px 0;
#     border-bottom: 1px solid rgba(255,255,255,0.05);
# }
# .step-item:last-child { border-bottom: none; }

# .step-num {
#     width: 28px; height: 28px; min-width: 28px;
#     border-radius: 50%;
#     background: linear-gradient(135deg, #f9c74f, #f3722c);
#     color: #0f0f0f;
#     font-weight: 700; font-size: 0.8rem;
#     display: flex; align-items: center; justify-content: center;
# }

# .step-text { color: #d0cfc8; font-size: 0.92rem; line-height: 1.5; }

# .tag {
#     display: inline-block;
#     padding: 4px 12px;
#     background: rgba(249,199,79,0.12);
#     border: 1px solid rgba(249,199,79,0.25);
#     border-radius: 20px;
#     color: #f9c74f;
#     font-size: 0.8rem;
#     margin: 3px;
# }

# .model-badge {
#     display: inline-flex;
#     align-items: center;
#     gap: 6px;
#     padding: 6px 14px;
#     border-radius: 8px;
#     background: rgba(255,255,255,0.06);
#     border: 1px solid rgba(255,255,255,0.1);
#     color: #e0ddd5;
#     font-size: 0.85rem;
#     margin: 4px;
# }

# .ref-item {
#     padding: 10px 14px;
#     border-left: 3px solid #f3722c;
#     background: rgba(243,114,44,0.06);
#     border-radius: 0 8px 8px 0;
#     margin-bottom: 8px;
#     font-size: 0.88rem;
#     color: #ccc;
# }

# .stSelectbox > div > div {
#     background: rgba(255,255,255,0.07) !important;
#     border: 1px solid rgba(255,255,255,0.15) !important;
#     border-radius: 10px !important;
#     color: #f0ece2 !important;
# }

# .stButton > button {
#     background: linear-gradient(135deg, #f9c74f, #f3722c) !important;
#     color: #0f0f0f !important;
#     border: none !important;
#     border-radius: 50px !important;
#     font-weight: 600 !important;
#     padding: 0.6rem 2rem !important;
#     font-size: 0.95rem !important;
#     width: 100% !important;
#     box-shadow: 0 4px 20px rgba(249,199,79,0.3) !important;
# }

# .stFileUploader > div {
#     background: rgba(255,255,255,0.04) !important;
#     border: 2px dashed rgba(249,199,79,0.3) !important;
#     border-radius: 12px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---- Hero Header ----
# st.markdown('<div class="hero-title">🍽️ Food Calorie AI System</div>', unsafe_allow_html=True)
# st.markdown('<div class="hero-subtitle">Machine Learning & Neural Network · Calorie Intelligence</div>', unsafe_allow_html=True)

# # ---- Navigation ----
# if "page" not in st.session_state:
#     st.session_state.page = "ML Explanation"

# pages = ["ML Explanation", "NN Explanation", "ML Prediction", "NN Prediction"]
# icons = ["🤖", "🧠", "🔍", "📷"]

# cols = st.columns(len(pages))
# for i, (p, icon) in enumerate(zip(pages, icons)):
#     with cols[i]:
#         if st.button(f"{icon} {p}", key=f"nav_{p}", use_container_width=True):
#             st.session_state.page = p
#             st.rerun()

# page = st.session_state.page

# st.markdown("---")

# # ----------------------------
# # Load Models (cache)
# # ----------------------------

# @st.cache_resource
# def load_models():

#     ensemble = joblib.load("models/ensemble_model.pkl")
#     cnn_model = load_model("models/cnn_model.h5")
#     food_df = joblib.load("models/food_full_data.pkl")

#     ml_metrics = joblib.load("models/ml_metrics.pkl")
#     cnn_metrics = joblib.load("models/cnn_metrics.pkl")

#     class_names = joblib.load("models/cnn_class_names.pkl")
#     feature_columns = joblib.load("models/feature_columns.pkl")

#     return ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns


# ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns = load_models()

# # ----------------------------
# # Helper Function
# # ----------------------------

# # def predict_calorie_level(food_name, grams):

# #     input_data = pd.DataFrame(columns=feature_columns)
# #     input_data.loc[0] = 0

# #     if "Grams" in input_data.columns:
# #         input_data["Grams"] = grams

# #     food_column = f"Food_{food_name}"

# #     if food_column in input_data.columns:
# #         input_data[food_column] = 1

# #     prediction = ensemble.predict(input_data)

# #     return prediction[0]
# def predict_calorie_level(food_name, grams):

#     input_data = pd.DataFrame(columns=feature_columns)
#     input_data.loc[0] = 0

#     if "Grams" in input_data.columns:
#         input_data["Grams"] = grams

#     food_column = f"Food_{food_name}"

#     if food_column in input_data.columns:
#         input_data[food_column] = 1

#     pred = ensemble.predict(input_data)[0]

#     label_map = {
#         0: "Low",
#         1: "Medium",
#         2: "High"
#     }

#     return label_map.get(pred, "Unknown")


# # ------------------ ML Explanation ------------------

# # if page == "ML Explanation":

# #     st.header("Machine Learning - Calorie Level Classification")

# #     st.write("""
# #     Model pipeline:

# #     1. Data Cleaning
# #     2. One-Hot Encoding
# #     3. Random Forest
# #     4. Gradient Boosting
# #     5. Soft Voting Ensemble
# #     """)

# #     st.subheader("Model Performance")

# #     # st.write(f"Accuracy: {ml_metrics['Accuracy']:.2f}")
# #     st.write(f"ML Accuracy: {ml_metrics['Accuracy']*100:.2f}%")
# if page == "ML Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🤖 Machine Learning — Calorie Level Classification</div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         ระบบ Machine Learning นี้ถูกพัฒนาขึ้นเพื่อทำนาย <b style="color:#f9c74f;">ระดับพลังงาน (Calorie Level)</b> ของอาหาร
#         โดยใช้ข้อมูลจาก Dataset อาหารและแคลอรี่
#         </p>
#         <p style="color:#c8c4bc; line-height:1.8;">โมเดลจะทำการจำแนกระดับพลังงานออกเป็น 3 ระดับ ได้แก่</p>
#         <div style="margin: 10px 0 14px 0;">
#             <span class="tag">🟢 Low — แคลอรี่ต่ำ</span>
#             <span class="tag">🟡 Medium — แคลอรี่ปานกลาง</span>
#             <span class="tag">🔴 High — แคลอรี่สูง</span>
#         </div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         ระบบนี้ถูกสร้างขึ้นโดยใช้เทคนิค <b style="color:#f9c74f;">Ensemble Learning</b>
#         ซึ่งเป็นการรวมโมเดลหลายตัวเข้าด้วยกัน เพื่อเพิ่มความแม่นยำของการทำนาย
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8;">
#             Dataset ที่ใช้ประกอบด้วยข้อมูลอาหารจาก 2 ไฟล์ ได้แก่
#             </p>
#             <div class="model-badge">📄 calorie_infos.csv</div>
#             <div class="model-badge">📄 Food and Calories - Sheet1.csv</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:12px;">
#             ข้อมูลใน Dataset ประกอบด้วย<br>
#             • <span style="color:#f9c74f;">Food Name</span> — ชื่ออาหาร<br>
#             • <span style="color:#f9c74f;">Serving Size / Grams</span> — ปริมาณต่อหนึ่งหน่วยบริโภค<br>
#             • <span style="color:#f9c74f;">Calories</span> — จำนวนพลังงาน<br><br>
#             หลังจากนั้นทำการรวม Dataset ทั้งสองเข้าด้วยกัน เพื่อเพิ่มจำนวนข้อมูลสำหรับการฝึกโมเดล
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">⚙️ Feature Engineering</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8;">
#             Feature ที่ใช้ในการฝึกโมเดล ได้แก่<br>
#             • <b style="color:#f9c74f;">Food Name</b><br>
#             • <b style="color:#f9c74f;">Serving Size (Grams)</b><br><br>
#             เนื่องจาก Food Name เป็นข้อมูลประเภทข้อความ
#             จึงต้องใช้เทคนิค <span style="color:#f9c74f;">One-Hot Encoding</span>
#             เพื่อแปลงเป็นตัวเลขก่อนนำไปใช้กับ Machine Learning Model
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🧹 Data Preprocessing</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ก่อนนำข้อมูลไปฝึกโมเดล จำเป็นต้องทำ Data Preprocessing เพื่อทำความสะอาดข้อมูล
#             ขั้นตอนประกอบด้วย
#             </p>
#         """, unsafe_allow_html=True)
#         steps = [
#             "รวม Dataset จากหลายไฟล์",
#             "ลบข้อมูลที่มีค่า Missing",
#             "แปลง Serving Size ให้เป็นหน่วยกรัม (Grams)",
#             "แปลงค่า Calories ให้อยู่ในรูปตัวเลข",
#             "ลบข้อมูลซ้ำ (Drop Duplicates)",
#         ]
#         steps_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(steps)])
#         st.markdown(steps_html + "</div>", unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🧩 Machine Learning Models</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:10px;">
#             โมเดล Machine Learning ที่ใช้ประกอบด้วย
#             </p>
#             <div class="model-badge">🌲 Random Forest Classifier</div>
#             <div class="model-badge">📈 Gradient Boosting Classifier</div>
#             <div class="model-badge">📐 Logistic Regression</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:14px;">
#             โมเดลทั้งสามถูกนำมารวมกันด้วยเทคนิค <b style="color:#f9c74f;">Soft Voting Ensemble</b><br><br>
#             Soft Voting จะคำนวณค่า Probability จากทุกโมเดล
#             จากนั้นเลือกคลาสที่มีค่า Probability สูงที่สุดเป็นผลลัพธ์สุดท้าย
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{ml_metrics['Accuracy']*100:.2f}%</div>
#                 <div class="metric-label">ML Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <p style="color:#9e9e9e; font-size:0.85rem; margin-bottom:12px;">แหล่งข้อมูลที่ใช้ในการพัฒนาโมเดล Machine Learning</p>
#         <div class="ref-item">📊 <b>Dataset 1:</b> Calories in Food Items per 100gm/Ounce/Serving — <a href="https://www.kaggle.com/datasets/syedjaferk/calories-in-food-items-per-100gm-ounce-serving" target="_blank" style="color:#f9c74f;">Kaggle · syedjaferk</a></div>
#         <div class="ref-item">📊 <b>Dataset 2:</b> Food and Their Calories — <a href="https://www.kaggle.com/datasets/vaishnavivenkatesan/food-and-their-calories" target="_blank" style="color:#f9c74f;">Kaggle · vaishnavivenkatesan</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Scikit-learn: Random Forest, Gradient Boosting, Logistic Regression, VotingClassifier — <a href="https://scikit-learn.org" target="_blank" style="color:#f9c74f;">scikit-learn.org</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Pandas — <a href="https://pandas.pydata.org" target="_blank" style="color:#f9c74f;">pandas.pydata.org</a> &nbsp;|&nbsp; NumPy — <a href="https://numpy.org" target="_blank" style="color:#f9c74f;">numpy.org</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ NN Explanation ------------------

# # elif page == "NN Explanation":

# #     st.header("Neural Network - CNN Food Classification")

# #     st.write("""
# #     CNN Architecture:

# #     • Image Resize (160x160)  
# #     • Data Augmentation  
# #     • 3 Convolution Layers  
# #     • MaxPooling  
# #     • Dropout Regularization  
# #     • Softmax Output Layer
# #     """)

# #     st.subheader("Model Performance")

# #     # st.write(f"Accuracy: {cnn_metrics['Accuracy']:.2f}")
# #     st.write(f"NN Accuracy: {cnn_metrics['Accuracy']*100:.2f}%")
# elif page == "NN Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🧠 Neural Network — Food Image Classification</div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         โมเดล Neural Network ถูกพัฒนาขึ้นเพื่อ <b style="color:#f9c74f;">จำแนกประเภทของอาหารจากรูปภาพ</b>
#         โดยใช้เทคนิค <b style="color:#f9c74f;">Convolutional Neural Network (CNN)</b>
#         ซึ่งเป็นโมเดลที่เหมาะสำหรับงานด้าน Computer Vision เช่น การจำแนกรูปภาพ
#         </p>
#         <div style="margin-top:12px;">
#             <span class="tag">🍕 Pizza</span>
#             <span class="tag">🍔 Burger</span>
#             <span class="tag">🥗 Salad</span>
#             <span class="tag">🍜 Noodles</span>
#             <span class="tag">🍚 Fried Rice</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <div class="model-badge">🖼️ Food Image Classification Dataset</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:12px;">
#             Dataset สำหรับ Neural Network ประกอบด้วยรูปภาพอาหารหลายประเภท เช่น
#             Pizza, Burger, Salad, Noodles, Fried Rice<br><br>
#             ภาพเหล่านี้ถูกใช้เพื่อฝึกโมเดลให้สามารถ <b style="color:#f9c74f;">จำแนกประเภทอาหารจากรูปภาพ</b> ได้
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🖼️ Image Preprocessing</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ก่อนนำภาพเข้าสู่โมเดล CNN มีการเตรียมข้อมูลดังนี้
#             </p>
#         """, unsafe_allow_html=True)
#         pre_steps = [
#             "Resize ภาพให้เป็นขนาด 160×160 pixels",
#             "Normalize ค่า Pixel ให้อยู่ในช่วง 0–1",
#             "ใช้ Data Augmentation เพื่อเพิ่มความหลากหลายของข้อมูล ได้แก่ Rotation · Horizontal Flip · Zoom · Brightness Adjustment",
#         ]
#         pre_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pre_steps)])
#         st.markdown(pre_html + "</div>", unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🏗️ CNN Architecture</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             โครงสร้างของโมเดล CNN ประกอบด้วย Layer หลักดังนี้
#             </p>
#         """, unsafe_allow_html=True)
#         arch_steps = [
#             "Convolution Layer — สกัดคุณลักษณะสำคัญของภาพ เช่น รูปร่าง ขอบ และพื้นผิวของอาหาร",
#             "ReLU Activation — เพิ่ม Non-linearity ให้โมเดล",
#             "MaxPooling Layer — ลด Dimension ของข้อมูล",
#             "Dropout Layer — ป้องกัน Overfitting",
#             "Fully Connected Layer — รวมข้อมูลเพื่อการตัดสินใจ",
#             "Softmax Output Layer — จำแนกประเภทอาหาร",
#         ]
#         arch_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(arch_steps)])
#         st.markdown(arch_html + "</div>", unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">⚡ Prediction Process</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ขั้นตอนการทำนายของระบบ
#             </p>
#         """, unsafe_allow_html=True)
#         pred_steps = [
#             "ผู้ใช้ Upload รูปอาหาร",
#             "ระบบ Resize และ Normalize รูปภาพ",
#             "CNN Model ทำนายประเภทอาหาร",
#             "ระบบนำชื่ออาหารไปค้นหาใน Dataset",
#             "ML Model ทำนายระดับแคลอรี่ของอาหาร",
#         ]
#         pred_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pred_steps)])
#         st.markdown(pred_html + '<p style="color:#9e9e9e;font-size:0.85rem;margin-top:12px;line-height:1.6;">🔀 ดังนั้นระบบนี้จึงเป็น <b style="color:#f9c74f;">Hybrid AI System</b> ที่ใช้ทั้ง Neural Network และ Machine Learning ร่วมกัน</p></div>', unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{cnn_metrics['Accuracy']*100:.2f}%</div>
#                 <div class="metric-label">NN Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <p style="color:#9e9e9e; font-size:0.85rem; margin-bottom:12px;">แหล่งข้อมูลที่ใช้ในการพัฒนาโมเดล Neural Network</p>
#         <div class="ref-item">🖼️ <b>Dataset:</b> Food Image Classification Dataset — <a href="https://www.kaggle.com/datasets/harishkumardatalab/food-image-classification-dataset" target="_blank" style="color:#f9c74f;">Kaggle · harishkumardatalab</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> TensorFlow / Keras — <a href="https://www.tensorflow.org" target="_blank" style="color:#f9c74f;">tensorflow.org</a></div>
#         <div class="ref-item">📚 <b>Algorithm:</b> Convolutional Neural Network — LeCun et al., 1998</div>
#         <div class="ref-item">🔧 <b>Augmentation:</b> Keras ImageDataGenerator — <a href="https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator" target="_blank" style="color:#f9c74f;">TF Docs</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ ML Prediction ------------------

# elif page == "ML Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔍 Calorie Level Prediction</div>
#         <p style="color:#9e9e9e; font-size:0.9rem; line-height:1.7;">เลือกชื่ออาหารเพื่อทำนายระดับแคลอรี่ด้วย ML Ensemble Model</p>
#     </div>
#     """, unsafe_allow_html=True)

#     food_list = sorted(food_df["Food"].unique())
#     food_name = st.selectbox("🍽️ Select Food", food_list)

#     if st.button("✨ Predict Calorie Level"):

#         row = food_df[food_df["Food"] == food_name]

#         if len(row) > 0:
#             grams = row["Grams"].values[0]
#             actual_cal = row["Calories"].values[0]
#             predicted_level = predict_calorie_level(food_name, grams)

#             level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#             color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))
#             r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

#             st.markdown(f"""
#             <div style="background:rgba({r},{g},{b},0.15); border:1px solid {color}66;
#                         border-radius:16px; padding:1.5rem 2rem; text-align:center; margin: 1rem 0;">
#                 <div style="font-size:0.8rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Predicted Calorie Level</div>
#                 <div style="font-size:3rem; margin: 0.3rem 0;">{emoji}</div>
#                 <div style="font-size:2.2rem; font-weight:700; color:{color};">{predicted_level}</div>
#             </div>
#             """, unsafe_allow_html=True)

#             c1, c2, c3 = st.columns(3)
#             with c1:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(actual_cal)}</div><div class="metric-label">Actual kcal</div></div>""", unsafe_allow_html=True)
#             with c2:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(grams)}g</div><div class="metric-label">Serving Size</div></div>""", unsafe_allow_html=True)
#             with c3:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{ml_metrics['Accuracy']*100:.2f}%</div><div class="metric-label">ML Accuracy</div></div>""", unsafe_allow_html=True)

#         else:
#             st.warning("Food not found in dataset")


# # ------------------ NN Prediction ------------------

# elif page == "NN Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">📷 Food Image Classification</div>
#         <p style="color:#9e9e9e; font-size:0.9rem; line-height:1.7;">อัปโหลดรูปภาพอาหาร — CNN จะจำแนกประเภท แล้ว ML จะทำนายระดับแคลอรี่</p>
#     </div>
#     """, unsafe_allow_html=True)

#     uploaded = st.file_uploader("📁 Upload Food Image (JPG / PNG)", type=["jpg", "jpeg", "png"])

#     if uploaded:

#         col1, col2 = st.columns([1, 1.5])

#         with col1:
#             img_display = Image.open(uploaded).convert("RGB")
#             st.image(img_display, caption="Uploaded Image", use_container_width=True)

#         with col2:
#             IMG_SIZE = 160
#             img = img_display.resize((IMG_SIZE, IMG_SIZE))
#             img_array = np.array(img) / 255.0
#             img_array = np.expand_dims(img_array, axis=0)

#             prediction = cnn_model.predict(img_array)
#             predicted_index = np.argmax(prediction)
#             confidence = np.max(prediction)
#             predicted_food = class_names[predicted_index]

#             st.markdown(f"""
#             <div class="section-card" style="margin-top:0;">
#                 <div class="section-title">🍽️ Predicted Food</div>
#                 <div style="font-size:1.8rem; font-weight:700; color:#f9c74f; margin: 8px 0;">{predicted_food}</div>
#                 <div style="color:#9e9e9e; font-size:0.88rem;">Confidence: <b style="color:#f3722c;">{confidence*100:.2f}%</b></div>
#             </div>
#             """, unsafe_allow_html=True)

#             row = pd.DataFrame()
#             food_list = food_df["Food"].tolist()
#             match = difflib.get_close_matches(predicted_food, food_list, n=1, cutoff=0.5)

#             if match:
#                 matched_food = match[0]
#                 row = food_df[food_df["Food"] == matched_food]

#             if len(row) > 0:
#                 grams = row["Grams"].values[0]
#                 predicted_level = predict_calorie_level(row["Food"].values[0], grams)

#                 level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#                 color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))
#                 r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

#                 st.markdown(f"""
#                 <div style="background:rgba({r},{g},{b},0.15); border:1px solid {color}66;
#                             border-radius:12px; padding:1.2rem; text-align:center; margin-top:0.8rem;">
#                     <div style="font-size:0.75rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Calorie Level</div>
#                     <div style="font-size:1.8rem; margin:4px 0;">{emoji}</div>
#                     <div style="font-size:1.8rem; font-weight:700; color:{color};">{predicted_level}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#             else:
#                 st.warning("Food not found in ML database")

#             st.markdown(f"""
#             <div class="metric-card" style="margin-top:12px; text-align:left;">
#                 <span style="color:#9e9e9e; font-size:0.8rem;">NN Accuracy: </span>
#                 <b style="color:#f9c74f;">{cnn_metrics['Accuracy']*100:.2f}%</b>
#             </div>
#             """, unsafe_allow_html=True)

# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# import difflib
# from tensorflow.keras.models import load_model
# from PIL import Image

# st.set_page_config(
#     page_title="Food Calorie AI",
#     page_icon="🍽️",
#     layout="wide"
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600&display=swap');

# html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

# .stApp {
#     background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #16213e 100%);
#     color: #f0ece2;
# }

# #MainMenu, footer, header {visibility: hidden;}
# .block-container {padding-top: 2rem; padding-bottom: 2rem;}

# .hero-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 3.2rem;
#     font-weight: 700;
#     background: linear-gradient(90deg, #f9c74f, #f3722c, #f94144);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     text-align: center;
#     margin-bottom: 0.2rem;
#     line-height: 1.2;
# }

# .hero-subtitle {
#     text-align: center;
#     color: #9e9e9e;
#     font-size: 1rem;
#     letter-spacing: 0.15em;
#     text-transform: uppercase;
#     margin-bottom: 2.5rem;
# }

# .section-card {
#     background: rgba(255,255,255,0.04);
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 16px;
#     padding: 1.8rem 2rem;
#     margin-bottom: 1.2rem;
# }

# .section-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 1.15rem;
#     color: #f9c74f;
#     margin-bottom: 0.8rem;
#     display: flex;
#     align-items: center;
#     gap: 8px;
# }

# .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 0.5rem; }

# .metric-card {
#     flex: 1;
#     min-width: 140px;
#     background: linear-gradient(135deg, rgba(249,199,79,0.12), rgba(243,114,44,0.08));
#     border: 1px solid rgba(249,199,79,0.2);
#     border-radius: 12px;
#     padding: 1rem 1.2rem;
#     text-align: center;
# }

# .metric-value { font-size: 2rem; font-weight: 700; color: #f9c74f; line-height: 1; }
# .metric-label { font-size: 0.78rem; color: #9e9e9e; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.1em; }

# .step-item {
#     display: flex;
#     align-items: flex-start;
#     gap: 14px;
#     padding: 10px 0;
#     border-bottom: 1px solid rgba(255,255,255,0.05);
# }
# .step-item:last-child { border-bottom: none; }

# .step-num {
#     width: 28px; height: 28px; min-width: 28px;
#     border-radius: 50%;
#     background: linear-gradient(135deg, #f9c74f, #f3722c);
#     color: #0f0f0f;
#     font-weight: 700; font-size: 0.8rem;
#     display: flex; align-items: center; justify-content: center;
# }

# .step-text { color: #d0cfc8; font-size: 0.92rem; line-height: 1.5; }

# .tag {
#     display: inline-block;
#     padding: 4px 12px;
#     background: rgba(249,199,79,0.12);
#     border: 1px solid rgba(249,199,79,0.25);
#     border-radius: 20px;
#     color: #f9c74f;
#     font-size: 0.8rem;
#     margin: 3px;
# }

# .model-badge {
#     display: inline-flex;
#     align-items: center;
#     gap: 6px;
#     padding: 6px 14px;
#     border-radius: 8px;
#     background: rgba(255,255,255,0.06);
#     border: 1px solid rgba(255,255,255,0.1);
#     color: #e0ddd5;
#     font-size: 0.85rem;
#     margin: 4px;
# }

# .ref-item {
#     padding: 10px 14px;
#     border-left: 3px solid #f3722c;
#     background: rgba(243,114,44,0.06);
#     border-radius: 0 8px 8px 0;
#     margin-bottom: 8px;
#     font-size: 0.88rem;
#     color: #ccc;
# }

# /* ---- Selectbox: input box stays dark, dropdown popup stays readable ---- */
# div[data-baseweb="select"] > div {
#     background: rgba(255,255,255,0.07) !important;
#     border: 1px solid rgba(255,255,255,0.2) !important;
#     border-radius: 10px !important;
# }

# /* selected value text inside input — force white so it's visible on dark bg */
# div[data-baseweb="select"] span,
# div[data-baseweb="select"] input,
# div[data-baseweb="select"] [class*="singleValue"],
# div[data-baseweb="select"] [class*="placeholder"],
# div[data-baseweb="select"] * {
#     color: #f0ece2 !important;
# }

# /* dropdown option list popup - white bg needs dark text */
# ul[data-baseweb="menu"] li,
# ul[role="listbox"] li,
# [role="option"] {
#     color: #1a1a1a !important;
#     background: #ffffff !important;
# }
# [role="option"]:hover,
# [role="option"][aria-selected="true"] {
#     background: #f0ede6 !important;
#     color: #1a1a1a !important;
# }

# /* label above selectbox */
# .stSelectbox label, .stSelectbox p {
#     color: #f0ece2 !important;
# }

# /* ---- Buttons ---- */
# .stButton > button {
#     background: linear-gradient(135deg, #f9c74f, #f3722c) !important;
#     color: #0f0f0f !important;
#     border: none !important;
#     border-radius: 50px !important;
#     font-weight: 600 !important;
#     padding: 0.6rem 2rem !important;
#     font-size: 0.95rem !important;
#     width: 100% !important;
#     box-shadow: 0 4px 20px rgba(249,199,79,0.3) !important;
# }

# /* ---- File Uploader: white box needs dark text ---- */
# [data-testid="stFileUploaderDropzone"] {
#     background: #ffffff !important;
#     border: 2px dashed #f3722c !important;
#     border-radius: 12px !important;
# }

# [data-testid="stFileUploaderDropzone"] p,
# [data-testid="stFileUploaderDropzone"] span,
# [data-testid="stFileUploaderDropzone"] small {
#     color: #1a1a1a !important;
# }

# [data-testid="stFileUploaderDropzone"] button {
#     color: #f3722c !important;
#     border: 1px solid #f3722c !important;
#     background: transparent !important;
#     border-radius: 6px !important;
# }

# /* file uploader label above the box */
# .stFileUploader label, .stFileUploader p {
#     color: #f0ece2 !important;
# }

# /* uploaded file name row below the dropzone */
# [data-testid="stFileUploaderFile"],
# [data-testid="stFileUploaderFileName"],
# [data-testid="stFileUploaderFile"] span,
# [data-testid="stFileUploaderFile"] small,
# [data-testid="stFileUploaderFile"] p {
#     color: #f0ece2 !important;
# }

# /* X delete button for uploaded file */
# [data-testid="stFileUploaderDeleteBtn"] button {
#     color: #f0ece2 !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---- Hero Header ----
# st.markdown('<div class="hero-title">🍽️ Food Calorie AI System</div>', unsafe_allow_html=True)
# st.markdown('<div class="hero-subtitle">Machine Learning & Neural Network · Calorie Intelligence</div>', unsafe_allow_html=True)

# # ---- Navigation ----
# if "page" not in st.session_state:
#     st.session_state.page = "ML Explanation"

# pages = ["ML Explanation", "NN Explanation", "ML Prediction", "NN Prediction"]
# icons = ["🤖", "🧠", "🔍", "📷"]

# cols = st.columns(len(pages))
# for i, (p, icon) in enumerate(zip(pages, icons)):
#     with cols[i]:
#         if st.button(f"{icon} {p}", key=f"nav_{p}", use_container_width=True):
#             st.session_state.page = p
#             st.rerun()

# page = st.session_state.page

# st.markdown("---")

# # ----------------------------
# # Load Models (cache)
# # ----------------------------

# @st.cache_resource
# def load_models():
#     ensemble = joblib.load("models/ensemble_model.pkl")
#     cnn_model = load_model("models/cnn_model.h5")
#     food_df = joblib.load("models/food_full_data.pkl")
#     ml_metrics = joblib.load("models/ml_metrics.pkl")
#     cnn_metrics = joblib.load("models/cnn_metrics.pkl")
#     class_names = joblib.load("models/cnn_class_names.pkl")
#     feature_columns = joblib.load("models/feature_columns.pkl")
#     return ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns


# ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns = load_models()

# # ----------------------------
# # Helper Function
# # ----------------------------

# def predict_calorie_level(food_name, grams):
#     input_data = pd.DataFrame(columns=feature_columns)
#     input_data.loc[0] = 0
#     if "Grams" in input_data.columns:
#         input_data["Grams"] = grams
#     food_column = f"Food_{food_name}"
#     if food_column in input_data.columns:
#         input_data[food_column] = 1
#     pred = ensemble.predict(input_data)[0]
#     label_map = {0: "Low", 1: "Medium", 2: "High"}
#     return label_map.get(pred, "Unknown")


# # ------------------ ML Explanation ------------------

# if page == "ML Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🤖 Machine Learning — Calorie Level Classification</div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         ระบบ Machine Learning นี้ถูกพัฒนาขึ้นเพื่อทำนาย <b style="color:#f9c74f;">ระดับพลังงาน (Calorie Level)</b> ของอาหาร
#         โดยใช้ข้อมูลจาก Dataset อาหารและแคลอรี่
#         </p>
#         <p style="color:#c8c4bc; line-height:1.8;">โมเดลจะทำการจำแนกระดับพลังงานออกเป็น 3 ระดับ ได้แก่</p>
#         <div style="margin: 10px 0 14px 0;">
#             <span class="tag">🟢 Low — แคลอรี่ต่ำ</span>
#             <span class="tag">🟡 Medium — แคลอรี่ปานกลาง</span>
#             <span class="tag">🔴 High — แคลอรี่สูง</span>
#         </div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         ระบบนี้ถูกสร้างขึ้นโดยใช้เทคนิค <b style="color:#f9c74f;">Ensemble Learning</b>
#         ซึ่งเป็นการรวมโมเดลหลายตัวเข้าด้วยกัน เพื่อเพิ่มความแม่นยำของการทำนาย
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8;">
#             Dataset ที่ใช้ประกอบด้วยข้อมูลอาหารจาก 2 ไฟล์ ได้แก่
#             </p>
#             <div class="model-badge">📄 calorie_infos.csv</div>
#             <div class="model-badge">📄 Food and Calories - Sheet1.csv</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:12px;">
#             ข้อมูลใน Dataset ประกอบด้วย<br>
#             • <span style="color:#f9c74f;">Food Name</span> — ชื่ออาหาร<br>
#             • <span style="color:#f9c74f;">Serving Size / Grams</span> — ปริมาณต่อหนึ่งหน่วยบริโภค<br>
#             • <span style="color:#f9c74f;">Calories</span> — จำนวนพลังงาน<br><br>
#             หลังจากนั้นทำการรวม Dataset ทั้งสองเข้าด้วยกัน เพื่อเพิ่มจำนวนข้อมูลสำหรับการฝึกโมเดล
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">⚙️ Feature Engineering</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8;">
#             Feature ที่ใช้ในการฝึกโมเดล ได้แก่<br>
#             • <b style="color:#f9c74f;">Food Name</b><br>
#             • <b style="color:#f9c74f;">Serving Size (Grams)</b><br><br>
#             เนื่องจาก Food Name เป็นข้อมูลประเภทข้อความ
#             จึงต้องใช้เทคนิค <span style="color:#f9c74f;">One-Hot Encoding</span>
#             เพื่อแปลงเป็นตัวเลขก่อนนำไปใช้กับ Machine Learning Model
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🧹 Data Preprocessing</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ก่อนนำข้อมูลไปฝึกโมเดล จำเป็นต้องทำ Data Preprocessing เพื่อทำความสะอาดข้อมูล
#             ขั้นตอนประกอบด้วย
#             </p>
#         </div>     
#         """, unsafe_allow_html=True)
#         steps = [
#             "รวม Dataset จากหลายไฟล์",
#             "ลบข้อมูลที่มีค่า Missing",
#             "แปลง Serving Size ให้เป็นหน่วยกรัม (Grams)",
#             "แปลงค่า Calories ให้อยู่ในรูปตัวเลข",
#             "ลบข้อมูลซ้ำ (Drop Duplicates)",
#         ]
#         steps_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(steps)])
#         st.markdown(steps_html + "</div>", unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🧩 Machine Learning Models</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:10px;">
#             โมเดล Machine Learning ที่ใช้ประกอบด้วย
#             </p>
#             <div class="model-badge">🌲 Random Forest Classifier</div>
#             <div class="model-badge">📈 Gradient Boosting Classifier</div>
#             <div class="model-badge">📐 Logistic Regression</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:14px;">
#             โมเดลทั้งสามถูกนำมารวมกันด้วยเทคนิค <b style="color:#f9c74f;">Soft Voting Ensemble</b><br><br>
#             Soft Voting จะคำนวณค่า Probability จากทุกโมเดล
#             จากนั้นเลือกคลาสที่มีค่า Probability สูงที่สุดเป็นผลลัพธ์สุดท้าย
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{ml_metrics['Accuracy']*100:.2f}%</div>
#                 <div class="metric-label">ML Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <p style="color:#9e9e9e; font-size:0.85rem; margin-bottom:12px;">แหล่งข้อมูลที่ใช้ในการพัฒนาโมเดล Machine Learning</p>
#         <div class="ref-item">📊 <b>Dataset 1:</b> Calories in Food Items per 100gm/Ounce/Serving — <a href="https://www.kaggle.com/datasets/syedjaferk/calories-in-food-items-per-100gm-ounce-serving" target="_blank" style="color:#f9c74f;">Kaggle · syedjaferk</a></div>
#         <div class="ref-item">📊 <b>Dataset 2:</b> Food and Their Calories — <a href="https://www.kaggle.com/datasets/vaishnavivenkatesan/food-and-their-calories" target="_blank" style="color:#f9c74f;">Kaggle · vaishnavivenkatesan</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Scikit-learn: Random Forest, Gradient Boosting, Logistic Regression, VotingClassifier — <a href="https://scikit-learn.org" target="_blank" style="color:#f9c74f;">scikit-learn.org</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Pandas — <a href="https://pandas.pydata.org" target="_blank" style="color:#f9c74f;">pandas.pydata.org</a> &nbsp;|&nbsp; NumPy — <a href="https://numpy.org" target="_blank" style="color:#f9c74f;">numpy.org</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ NN Explanation ------------------

# elif page == "NN Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🧠 Neural Network — Food Image Classification</div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         โมเดล Neural Network ถูกพัฒนาขึ้นเพื่อ <b style="color:#f9c74f;">จำแนกประเภทของอาหารจากรูปภาพ</b>
#         โดยใช้เทคนิค <b style="color:#f9c74f;">Convolutional Neural Network (CNN)</b>
#         ซึ่งเป็นโมเดลที่เหมาะสำหรับงานด้าน Computer Vision เช่น การจำแนกรูปภาพ
#         </p>
#         <div style="margin-top:12px;">
#             <span class="tag">🍕 Pizza</span>
#             <span class="tag">🍔 Burger</span>
#             <span class="tag">🥗 Salad</span>
#             <span class="tag">🍜 Noodles</span>
#             <span class="tag">🍚 Fried Rice</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <div class="model-badge">🖼️ Food Image Classification Dataset</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:12px;">
#             Dataset สำหรับ Neural Network ประกอบด้วยรูปภาพอาหารหลายประเภท เช่น
#             Pizza, Burger, Salad, Noodles, Fried Rice<br><br>
#             ภาพเหล่านี้ถูกใช้เพื่อฝึกโมเดลให้สามารถ <b style="color:#f9c74f;">จำแนกประเภทอาหารจากรูปภาพ</b> ได้
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🖼️ Image Preprocessing</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ก่อนนำภาพเข้าสู่โมเดล CNN มีการเตรียมข้อมูลดังนี้
#             </p>
#         """, unsafe_allow_html=True)
#         pre_steps = [
#             "Resize ภาพให้เป็นขนาด 160×160 pixels",
#             "Normalize ค่า Pixel ให้อยู่ในช่วง 0–1",
#             "ใช้ Data Augmentation เพื่อเพิ่มความหลากหลายของข้อมูล ได้แก่ Rotation · Horizontal Flip · Zoom · Brightness Adjustment",
#         ]
#         pre_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pre_steps)])
#         st.markdown(pre_html + "</div>", unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🏗️ CNN Architecture</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             โครงสร้างของโมเดล CNN ประกอบด้วย Layer หลักดังนี้
#             </p>
#         """, unsafe_allow_html=True)
#         arch_steps = [
#             "Convolution Layer — สกัดคุณลักษณะสำคัญของภาพ เช่น รูปร่าง ขอบ และพื้นผิวของอาหาร",
#             "ReLU Activation — เพิ่ม Non-linearity ให้โมเดล",
#             "MaxPooling Layer — ลด Dimension ของข้อมูล",
#             "Dropout Layer — ป้องกัน Overfitting",
#             "Fully Connected Layer — รวมข้อมูลเพื่อการตัดสินใจ",
#             "Softmax Output Layer — จำแนกประเภทอาหาร",
#         ]
#         arch_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(arch_steps)])
#         st.markdown(arch_html + "</div>", unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">⚡ Prediction Process</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ขั้นตอนการทำนายของระบบ
#             </p>
#         """, unsafe_allow_html=True)
#         pred_steps = [
#             "ผู้ใช้ Upload รูปอาหาร",
#             "ระบบ Resize และ Normalize รูปภาพ",
#             "CNN Model ทำนายประเภทอาหาร",
#             "ระบบนำชื่ออาหารไปค้นหาใน Dataset",
#             "ML Model ทำนายระดับแคลอรี่ของอาหาร",
#         ]
#         pred_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pred_steps)])
#         st.markdown(pred_html + '<p style="color:#9e9e9e;font-size:0.85rem;margin-top:12px;line-height:1.6;">🔀 ดังนั้นระบบนี้จึงเป็น <b style="color:#f9c74f;">Hybrid AI System</b> ที่ใช้ทั้ง Neural Network และ Machine Learning ร่วมกัน</p></div>', unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{cnn_metrics['Accuracy']*100:.2f}%</div>
#                 <div class="metric-label">NN Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <p style="color:#9e9e9e; font-size:0.85rem; margin-bottom:12px;">แหล่งข้อมูลที่ใช้ในการพัฒนาโมเดล Neural Network</p>
#         <div class="ref-item">🖼️ <b>Dataset:</b> Food Image Classification Dataset — <a href="https://www.kaggle.com/datasets/harishkumardatalab/food-image-classification-dataset" target="_blank" style="color:#f9c74f;">Kaggle · harishkumardatalab</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> TensorFlow / Keras — <a href="https://www.tensorflow.org" target="_blank" style="color:#f9c74f;">tensorflow.org</a></div>
#         <div class="ref-item">📚 <b>Algorithm:</b> Convolutional Neural Network — LeCun et al., 1998</div>
#         <div class="ref-item">🔧 <b>Augmentation:</b> Keras ImageDataGenerator — <a href="https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator" target="_blank" style="color:#f9c74f;">TF Docs</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ ML Prediction ------------------

# elif page == "ML Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔍 Calorie Level Prediction</div>
#         <p style="color:#9e9e9e; font-size:0.9rem; line-height:1.7;">เลือกชื่ออาหารเพื่อทำนายระดับแคลอรี่ด้วย ML Ensemble Model</p>
#     </div>
#     """, unsafe_allow_html=True)

#     food_list = sorted(food_df["Food"].unique())
#     food_name = st.selectbox("🍽️ Select Food", food_list)

#     if st.button("✨ Predict Calorie Level"):

#         row = food_df[food_df["Food"] == food_name]

#         if len(row) > 0:
#             grams = row["Grams"].values[0]
#             actual_cal = row["Calories"].values[0]
#             predicted_level = predict_calorie_level(food_name, grams)

#             level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#             color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))
#             r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

#             st.markdown(f"""
#             <div style="background:rgba({r},{g},{b},0.15); border:1px solid {color}66;
#                         border-radius:16px; padding:1.5rem 2rem; text-align:center; margin: 1rem 0;">
#                 <div style="font-size:0.8rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Predicted Calorie Level</div>
#                 <div style="font-size:3rem; margin: 0.3rem 0;">{emoji}</div>
#                 <div style="font-size:2.2rem; font-weight:700; color:{color};">{predicted_level}</div>
#             </div>
#             """, unsafe_allow_html=True)

#             c1, c2, c3 = st.columns(3)
#             with c1:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(actual_cal)}</div><div class="metric-label">Actual kcal</div></div>""", unsafe_allow_html=True)
#             with c2:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(grams)}g</div><div class="metric-label">Serving Size</div></div>""", unsafe_allow_html=True)
#             with c3:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{ml_metrics['Accuracy']*100:.2f}%</div><div class="metric-label">ML Accuracy</div></div>""", unsafe_allow_html=True)

#         else:
#             st.warning("Food not found in dataset")


# # ------------------ NN Prediction ------------------

# elif page == "NN Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">📷 Food Image Classification</div>
#         <p style="color:#9e9e9e; font-size:0.9rem; line-height:1.7;">อัปโหลดรูปภาพอาหาร — CNN จะจำแนกประเภท แล้ว ML จะทำนายระดับแคลอรี่</p>
#     </div>
#     """, unsafe_allow_html=True)

#     uploaded = st.file_uploader("📁 Upload Food Image (JPG / PNG)", type=["jpg", "jpeg", "png"])

#     if uploaded:

#         col1, col2 = st.columns([1, 1.5])

#         with col1:
#             img_display = Image.open(uploaded).convert("RGB")
#             st.image(img_display, caption="Uploaded Image", use_container_width=True)

#         with col2:
#             IMG_SIZE = 160
#             img = img_display.resize((IMG_SIZE, IMG_SIZE))
#             img_array = np.array(img) / 255.0
#             img_array = np.expand_dims(img_array, axis=0)

#             prediction = cnn_model.predict(img_array)
#             predicted_index = np.argmax(prediction)
#             confidence = np.max(prediction)
#             predicted_food = class_names[predicted_index]

#             st.markdown(f"""
#             <div class="section-card" style="margin-top:0;">
#                 <div class="section-title">🍽️ Predicted Food</div>
#                 <div style="font-size:1.8rem; font-weight:700; color:#f9c74f; margin: 8px 0;">{predicted_food}</div>
#                 <div style="color:#9e9e9e; font-size:0.88rem;">Confidence: <b style="color:#f3722c;">{confidence*100:.2f}%</b></div>
#             </div>
#             """, unsafe_allow_html=True)

#             row = pd.DataFrame()
#             food_list = food_df["Food"].tolist()
#             match = difflib.get_close_matches(predicted_food, food_list, n=1, cutoff=0.5)

#             if match:
#                 matched_food = match[0]
#                 row = food_df[food_df["Food"] == matched_food]

#             if len(row) > 0:
#                 grams = row["Grams"].values[0]
#                 predicted_level = predict_calorie_level(row["Food"].values[0], grams)

#                 level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#                 color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))
#                 r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

#                 st.markdown(f"""
#                 <div style="background:rgba({r},{g},{b},0.15); border:1px solid {color}66;
#                             border-radius:12px; padding:1.2rem; text-align:center; margin-top:0.8rem;">
#                     <div style="font-size:0.75rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Calorie Level</div>
#                     <div style="font-size:1.8rem; margin:4px 0;">{emoji}</div>
#                     <div style="font-size:1.8rem; font-weight:700; color:{color};">{predicted_level}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#             else:
#                 st.warning("Food not found in ML database")

#             st.markdown(f"""
#             <div class="metric-card" style="margin-top:12px; text-align:left;">
#                 <span style="color:#9e9e9e; font-size:0.8rem;">NN Accuracy: </span>
#                 <b style="color:#f9c74f;">{cnn_metrics['Accuracy']*100:.2f}%</b>
#             </div>
#             """, unsafe_allow_html=True)

# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# import difflib
# from tensorflow.keras.models import load_model
# from PIL import Image

# st.set_page_config(
#     page_title="Food Calorie AI",
#     page_icon="🍽️",
#     layout="wide"
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600&display=swap');

# html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

# .stApp {
#     background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #16213e 100%);
#     color: #f0ece2;
# }

# #MainMenu, footer, header {visibility: hidden;}
# .block-container {padding-top: 2rem; padding-bottom: 2rem;}

# .hero-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 3.2rem;
#     font-weight: 700;
#     background: linear-gradient(90deg, #f9c74f, #f3722c, #f94144);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     text-align: center;
#     margin-bottom: 0.2rem;
#     line-height: 1.2;
# }

# .hero-subtitle {
#     text-align: center;
#     color: #9e9e9e;
#     font-size: 1rem;
#     letter-spacing: 0.15em;
#     text-transform: uppercase;
#     margin-bottom: 2.5rem;
# }

# .section-card {
#     background: rgba(255,255,255,0.04);
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 16px;
#     padding: 1.8rem 2rem;
#     margin-bottom: 1.2rem;
# }

# .section-title {
#     font-family: 'Playfair Display', serif;
#     font-size: 1.15rem;
#     color: #f9c74f;
#     margin-bottom: 0.8rem;
#     display: flex;
#     align-items: center;
#     gap: 8px;
# }

# .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 0.5rem; }

# .metric-card {
#     flex: 1;
#     min-width: 140px;
#     background: linear-gradient(135deg, rgba(249,199,79,0.12), rgba(243,114,44,0.08));
#     border: 1px solid rgba(249,199,79,0.2);
#     border-radius: 12px;
#     padding: 1rem 1.2rem;
#     text-align: center;
# }

# .metric-value { font-size: 2rem; font-weight: 700; color: #f9c74f; line-height: 1; }
# .metric-label { font-size: 0.78rem; color: #9e9e9e; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.1em; }

# .step-item {
#     display: flex;
#     align-items: flex-start;
#     gap: 14px;
#     padding: 10px 0;
#     border-bottom: 1px solid rgba(255,255,255,0.05);
# }
# .step-item:last-child { border-bottom: none; }

# .step-num {
#     width: 28px; height: 28px; min-width: 28px;
#     border-radius: 50%;
#     background: linear-gradient(135deg, #f9c74f, #f3722c);
#     color: #0f0f0f;
#     font-weight: 700; font-size: 0.8rem;
#     display: flex; align-items: center; justify-content: center;
# }

# .step-text { color: #d0cfc8; font-size: 0.92rem; line-height: 1.5; }

# .tag {
#     display: inline-block;
#     padding: 4px 12px;
#     background: rgba(249,199,79,0.12);
#     border: 1px solid rgba(249,199,79,0.25);
#     border-radius: 20px;
#     color: #f9c74f;
#     font-size: 0.8rem;
#     margin: 3px;
# }

# .model-badge {
#     display: inline-flex;
#     align-items: center;
#     gap: 6px;
#     padding: 6px 14px;
#     border-radius: 8px;
#     background: rgba(255,255,255,0.06);
#     border: 1px solid rgba(255,255,255,0.1);
#     color: #e0ddd5;
#     font-size: 0.85rem;
#     margin: 4px;
# }

# .ref-item {
#     padding: 10px 14px;
#     border-left: 3px solid #f3722c;
#     background: rgba(243,114,44,0.06);
#     border-radius: 0 8px 8px 0;
#     margin-bottom: 8px;
#     font-size: 0.88rem;
#     color: #ccc;
# }

# /* ---- Selectbox: input box stays dark, dropdown popup stays readable ---- */
# div[data-baseweb="select"] > div {
#     background: rgba(255,255,255,0.07) !important;
#     border: 1px solid rgba(255,255,255,0.2) !important;
#     border-radius: 10px !important;
# }

# /* selected value text inside input — force white so it's visible on dark bg */
# div[data-baseweb="select"] span,
# div[data-baseweb="select"] input,
# div[data-baseweb="select"] [class*="singleValue"],
# div[data-baseweb="select"] [class*="placeholder"],
# div[data-baseweb="select"] * {
#     color: #f0ece2 !important;
# }

# /* dropdown option list popup - white bg needs dark text */
# ul[data-baseweb="menu"] li,
# ul[role="listbox"] li,
# [role="option"] {
#     color: #1a1a1a !important;
#     background: #ffffff !important;
# }
# [role="option"]:hover,
# [role="option"][aria-selected="true"] {
#     background: #f0ede6 !important;
#     color: #1a1a1a !important;
# }

# /* label above selectbox */
# .stSelectbox label, .stSelectbox p {
#     color: #f0ece2 !important;
# }

# /* ---- Buttons ---- */
# .stButton > button {
#     background: linear-gradient(135deg, #f9c74f, #f3722c) !important;
#     color: #0f0f0f !important;
#     border: none !important;
#     border-radius: 50px !important;
#     font-weight: 600 !important;
#     padding: 0.6rem 2rem !important;
#     font-size: 0.95rem !important;
#     width: 100% !important;
#     box-shadow: 0 4px 20px rgba(249,199,79,0.3) !important;
# }

# /* ---- File Uploader: white box needs dark text ---- */
# [data-testid="stFileUploaderDropzone"] {
#     background: #ffffff !important;
#     border: 2px dashed #f3722c !important;
#     border-radius: 12px !important;
# }

# [data-testid="stFileUploaderDropzone"] p,
# [data-testid="stFileUploaderDropzone"] span,
# [data-testid="stFileUploaderDropzone"] small {
#     color: #1a1a1a !important;
# }

# [data-testid="stFileUploaderDropzone"] button {
#     color: #f3722c !important;
#     border: 1px solid #f3722c !important;
#     background: transparent !important;
#     border-radius: 6px !important;
# }

# /* file uploader label above the box */
# .stFileUploader label, .stFileUploader p {
#     color: #f0ece2 !important;
# }

# /* uploaded file name row below the dropzone */
# [data-testid="stFileUploaderFile"],
# [data-testid="stFileUploaderFileName"],
# [data-testid="stFileUploaderFile"] span,
# [data-testid="stFileUploaderFile"] small,
# [data-testid="stFileUploaderFile"] p {
#     color: #f0ece2 !important;
# }

# /* X delete button for uploaded file */
# [data-testid="stFileUploaderDeleteBtn"] button {
#     color: #f0ece2 !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---- Hero Header ----
# st.markdown('<div class="hero-title">🍽️ Food Calorie AI System</div>', unsafe_allow_html=True)
# st.markdown('<div class="hero-subtitle">Machine Learning & Neural Network · Calorie Intelligence</div>', unsafe_allow_html=True)

# # ---- Navigation ----
# if "page" not in st.session_state:
#     st.session_state.page = "ML Explanation"

# pages = ["ML Explanation", "NN Explanation", "ML Prediction", "NN Prediction"]
# icons = ["🤖", "🧠", "🔍", "📷"]

# cols = st.columns(len(pages))
# for i, (p, icon) in enumerate(zip(pages, icons)):
#     with cols[i]:
#         if st.button(f"{icon} {p}", key=f"nav_{p}", use_container_width=True):
#             st.session_state.page = p
#             st.rerun()

# page = st.session_state.page

# st.markdown("---")

# # ----------------------------
# # Load Models (cache)
# # ----------------------------

# @st.cache_resource
# def load_models():
#     ensemble = joblib.load("models/ensemble_model.pkl")
#     cnn_model = load_model("models/cnn_model.h5")
#     food_df = joblib.load("models/food_full_data.pkl")
#     ml_metrics = joblib.load("models/ml_metrics.pkl")
#     cnn_metrics = joblib.load("models/cnn_metrics.pkl")
#     class_names = joblib.load("models/cnn_class_names.pkl")
#     feature_columns = joblib.load("models/feature_columns.pkl")
#     return ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns


# ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns = load_models()

# # ----------------------------
# # Helper Function
# # ----------------------------

# def predict_calorie_level(food_name, grams):
#     input_data = pd.DataFrame(columns=feature_columns)
#     input_data.loc[0] = 0
#     if "Grams" in input_data.columns:
#         input_data["Grams"] = grams
#     food_column = f"Food_{food_name}"
#     if food_column in input_data.columns:
#         input_data[food_column] = 1
#     pred = ensemble.predict(input_data)[0]
#     label_map = {0: "Low", 1: "Medium", 2: "High"}
#     return label_map.get(pred, "Unknown")


# # ------------------ ML Explanation ------------------

# if page == "ML Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🤖 Machine Learning — Calorie Level Classification</div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         ระบบ Machine Learning นี้ถูกพัฒนาขึ้นเพื่อทำนาย <b style="color:#f9c74f;">ระดับพลังงาน (Calorie Level)</b> ของอาหาร
#         โดยใช้ข้อมูลจาก Dataset อาหารและแคลอรี่
#         </p>
#         <p style="color:#c8c4bc; line-height:1.8;">โมเดลจะทำการจำแนกระดับพลังงานออกเป็น 3 ระดับ ได้แก่</p>
#         <div style="margin: 10px 0 14px 0;">
#             <span class="tag">🟢 Low — แคลอรี่ต่ำ</span>
#             <span class="tag">🟡 Medium — แคลอรี่ปานกลาง</span>
#             <span class="tag">🔴 High — แคลอรี่สูง</span>
#         </div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         ระบบนี้ถูกสร้างขึ้นโดยใช้เทคนิค <b style="color:#f9c74f;">Ensemble Learning</b>
#         ซึ่งเป็นการรวมโมเดลหลายตัวเข้าด้วยกัน เพื่อเพิ่มความแม่นยำของการทำนาย
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8;">
#             Dataset ที่ใช้ประกอบด้วยข้อมูลอาหารจาก 2 ไฟล์ ได้แก่
#             </p>
#             <div class="model-badge">📄 calorie_infos.csv</div>
#             <div class="model-badge">📄 Food and Calories - Sheet1.csv</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:12px;">
#             ข้อมูลใน Dataset ประกอบด้วย<br>
#             • <span style="color:#f9c74f;">Food Name</span> — ชื่ออาหาร<br>
#             • <span style="color:#f9c74f;">Serving Size / Grams</span> — ปริมาณต่อหนึ่งหน่วยบริโภค<br>
#             • <span style="color:#f9c74f;">Calories</span> — จำนวนพลังงาน<br><br>
#             หลังจากนั้นทำการรวม Dataset ทั้งสองเข้าด้วยกัน เพื่อเพิ่มจำนวนข้อมูลสำหรับการฝึกโมเดล
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">⚙️ Feature Engineering</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8;">
#             Feature ที่ใช้ในการฝึกโมเดล ได้แก่<br>
#             • <b style="color:#f9c74f;">Food Name</b><br>
#             • <b style="color:#f9c74f;">Serving Size (Grams)</b><br><br>
#             เนื่องจาก Food Name เป็นข้อมูลประเภทข้อความ
#             จึงต้องใช้เทคนิค <span style="color:#f9c74f;">One-Hot Encoding</span>
#             เพื่อแปลงเป็นตัวเลขก่อนนำไปใช้กับ Machine Learning Model
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         steps = [
#             "รวม Dataset จากหลายไฟล์",
#             "ลบข้อมูลที่มีค่า Missing",
#             "แปลง Serving Size ให้เป็นหน่วยกรัม (Grams)",
#             "แปลงค่า Calories ให้อยู่ในรูปตัวเลข",
#             "ลบข้อมูลซ้ำ (Drop Duplicates)",
#         ]
#         steps_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(steps)])
#         st.markdown(f"""
#         <div class="section-card">
#             <div class="section-title">🧹 Data Preprocessing</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ก่อนนำข้อมูลไปฝึกโมเดล จำเป็นต้องทำ Data Preprocessing เพื่อทำความสะอาดข้อมูล
#             ขั้นตอนประกอบด้วย
#             </p>
#             {steps_html}
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">🧩 Machine Learning Models</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:10px;">
#             โมเดล Machine Learning ที่ใช้ประกอบด้วย
#             </p>
#             <div class="model-badge">🌲 Random Forest Classifier</div>
#             <div class="model-badge">📈 Gradient Boosting Classifier</div>
#             <div class="model-badge">📐 Logistic Regression</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:14px;">
#             โมเดลทั้งสามถูกนำมารวมกันด้วยเทคนิค <b style="color:#f9c74f;">Soft Voting Ensemble</b><br><br>
#             Soft Voting จะคำนวณค่า Probability จากทุกโมเดล
#             จากนั้นเลือกคลาสที่มีค่า Probability สูงที่สุดเป็นผลลัพธ์สุดท้าย
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{ml_metrics['Accuracy']*100:.2f}%</div>
#                 <div class="metric-label">ML Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <p style="color:#9e9e9e; font-size:0.85rem; margin-bottom:12px;">แหล่งข้อมูลที่ใช้ในการพัฒนาโมเดล Machine Learning</p>
#         <div class="ref-item">📊 <b>Dataset 1:</b> Calories in Food Items per 100gm/Ounce/Serving — <a href="https://www.kaggle.com/datasets/syedjaferk/calories-in-food-items-per-100gm-ounce-serving" target="_blank" style="color:#f9c74f;">Kaggle · syedjaferk</a></div>
#         <div class="ref-item">📊 <b>Dataset 2:</b> Food and Their Calories — <a href="https://www.kaggle.com/datasets/vaishnavivenkatesan/food-and-their-calories" target="_blank" style="color:#f9c74f;">Kaggle · vaishnavivenkatesan</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Scikit-learn: Random Forest, Gradient Boosting, Logistic Regression, VotingClassifier — <a href="https://scikit-learn.org" target="_blank" style="color:#f9c74f;">scikit-learn.org</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> Pandas — <a href="https://pandas.pydata.org" target="_blank" style="color:#f9c74f;">pandas.pydata.org</a> &nbsp;|&nbsp; NumPy — <a href="https://numpy.org" target="_blank" style="color:#f9c74f;">numpy.org</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ NN Explanation ------------------

# elif page == "NN Explanation":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🧠 Neural Network — Food Image Classification</div>
#         <p style="color:#c8c4bc; line-height:1.8;">
#         โมเดล Neural Network ถูกพัฒนาขึ้นเพื่อ <b style="color:#f9c74f;">จำแนกประเภทของอาหารจากรูปภาพ</b>
#         โดยใช้เทคนิค <b style="color:#f9c74f;">Convolutional Neural Network (CNN)</b>
#         ซึ่งเป็นโมเดลที่เหมาะสำหรับงานด้าน Computer Vision เช่น การจำแนกรูปภาพ
#         </p>
#         <div style="margin-top:12px;">
#             <span class="tag">🍕 Pizza</span>
#             <span class="tag">🍔 Burger</span>
#             <span class="tag">🥗 Salad</span>
#             <span class="tag">🍜 Noodles</span>
#             <span class="tag">🍚 Fried Rice</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">📦 Dataset</div>
#             <div class="model-badge">🖼️ Food Image Classification Dataset</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-top:12px;">
#             Dataset สำหรับ Neural Network ประกอบด้วยรูปภาพอาหารหลายประเภท เช่น
#             Pizza, Burger, Salad, Noodles, Fried Rice<br><br>
#             ภาพเหล่านี้ถูกใช้เพื่อฝึกโมเดลให้สามารถ <b style="color:#f9c74f;">จำแนกประเภทอาหารจากรูปภาพ</b> ได้
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         pre_steps = [
#             "Resize ภาพให้เป็นขนาด 160×160 pixels",
#             "Normalize ค่า Pixel ให้อยู่ในช่วง 0–1",
#             "ใช้ Data Augmentation เพื่อเพิ่มความหลากหลายของข้อมูล ได้แก่ Rotation · Horizontal Flip · Zoom · Brightness Adjustment",
#         ]
#         pre_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pre_steps)])
#         st.markdown(f"""
#         <div class="section-card">
#             <div class="section-title">🖼️ Image Preprocessing</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ก่อนนำภาพเข้าสู่โมเดล CNN มีการเตรียมข้อมูลดังนี้
#             </p>
#             {pre_html}
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         arch_steps = [
#             "Convolution Layer — สกัดคุณลักษณะสำคัญของภาพ เช่น รูปร่าง ขอบ และพื้นผิวของอาหาร",
#             "ReLU Activation — เพิ่ม Non-linearity ให้โมเดล",
#             "MaxPooling Layer — ลด Dimension ของข้อมูล",
#             "Dropout Layer — ป้องกัน Overfitting",
#             "Fully Connected Layer — รวมข้อมูลเพื่อการตัดสินใจ",
#             "Softmax Output Layer — จำแนกประเภทอาหาร",
#         ]
#         arch_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(arch_steps)])
#         st.markdown(f"""
#         <div class="section-card">
#             <div class="section-title">🏗️ CNN Architecture</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             โครงสร้างของโมเดล CNN ประกอบด้วย Layer หลักดังนี้
#             </p>
#             {arch_html}
#         </div>
#         """, unsafe_allow_html=True)

#         pred_steps = [
#             "ผู้ใช้ Upload รูปอาหาร",
#             "ระบบ Resize และ Normalize รูปภาพ",
#             "CNN Model ทำนายประเภทอาหาร",
#             "ระบบนำชื่ออาหารไปค้นหาใน Dataset",
#             "ML Model ทำนายระดับแคลอรี่ของอาหาร",
#         ]
#         pred_html = "".join([f'<div class="step-item"><div class="step-num">{i+1}</div><div class="step-text">{s}</div></div>' for i, s in enumerate(pred_steps)])
#         st.markdown(f"""
#         <div class="section-card">
#             <div class="section-title">⚡ Prediction Process</div>
#             <p style="color:#c8c4bc; font-size:0.9rem; line-height:1.8; margin-bottom:12px;">
#             ขั้นตอนการทำนายของระบบ
#             </p>
#             {pred_html}
#             <p style="color:#9e9e9e;font-size:0.85rem;margin-top:12px;line-height:1.6;">🔀 ดังนั้นระบบนี้จึงเป็น <b style="color:#f9c74f;">Hybrid AI System</b> ที่ใช้ทั้ง Neural Network และ Machine Learning ร่วมกัน</p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="section-card">
#         <div class="section-title">📊 Model Performance</div>
#         <div class="metric-row">
#             <div class="metric-card">
#                 <div class="metric-value">{cnn_metrics['Accuracy']*100:.2f}%</div>
#                 <div class="metric-label">NN Accuracy</div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔗 References</div>
#         <p style="color:#9e9e9e; font-size:0.85rem; margin-bottom:12px;">แหล่งข้อมูลที่ใช้ในการพัฒนาโมเดล Neural Network</p>
#         <div class="ref-item">🖼️ <b>Dataset:</b> Food Image Classification Dataset — <a href="https://www.kaggle.com/datasets/harishkumardatalab/food-image-classification-dataset" target="_blank" style="color:#f9c74f;">Kaggle · harishkumardatalab</a></div>
#         <div class="ref-item">🔧 <b>Library:</b> TensorFlow / Keras — <a href="https://www.tensorflow.org" target="_blank" style="color:#f9c74f;">tensorflow.org</a></div>
#         <div class="ref-item">📚 <b>Algorithm:</b> Convolutional Neural Network — LeCun et al., 1998</div>
#         <div class="ref-item">🔧 <b>Augmentation:</b> Keras ImageDataGenerator — <a href="https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator" target="_blank" style="color:#f9c74f;">TF Docs</a></div>
#     </div>
#     """, unsafe_allow_html=True)


# # ------------------ ML Prediction ------------------

# elif page == "ML Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">🔍 Calorie Level Prediction</div>
#         <p style="color:#9e9e9e; font-size:0.9rem; line-height:1.7;">เลือกชื่ออาหารเพื่อทำนายระดับแคลอรี่ด้วย ML Ensemble Model</p>
#     </div>
#     """, unsafe_allow_html=True)

#     food_list = sorted(food_df["Food"].unique())
#     food_name = st.selectbox("🍽️ Select Food", food_list)

#     if st.button("✨ Predict Calorie Level"):

#         row = food_df[food_df["Food"] == food_name]

#         if len(row) > 0:
#             grams = row["Grams"].values[0]
#             actual_cal = row["Calories"].values[0]
#             predicted_level = predict_calorie_level(food_name, grams)

#             level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#             color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))
#             r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

#             st.markdown(f"""
#             <div style="background:rgba({r},{g},{b},0.15); border:1px solid {color}66;
#                         border-radius:16px; padding:1.5rem 2rem; text-align:center; margin: 1rem 0;">
#                 <div style="font-size:0.8rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Predicted Calorie Level</div>
#                 <div style="font-size:3rem; margin: 0.3rem 0;">{emoji}</div>
#                 <div style="font-size:2.2rem; font-weight:700; color:{color};">{predicted_level}</div>
#             </div>
#             """, unsafe_allow_html=True)

#             c1, c2, c3 = st.columns(3)
#             with c1:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(actual_cal)}</div><div class="metric-label">Actual kcal</div></div>""", unsafe_allow_html=True)
#             with c2:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{int(grams)}g</div><div class="metric-label">Serving Size</div></div>""", unsafe_allow_html=True)
#             with c3:
#                 st.markdown(f"""<div class="metric-card"><div class="metric-value" style="font-size:1.6rem;">{ml_metrics['Accuracy']*100:.2f}%</div><div class="metric-label">ML Accuracy</div></div>""", unsafe_allow_html=True)

#         else:
#             st.warning("Food not found in dataset")


# # ------------------ NN Prediction ------------------

# elif page == "NN Prediction":

#     st.markdown("""
#     <div class="section-card">
#         <div class="section-title">📷 Food Image Classification</div>
#         <p style="color:#9e9e9e; font-size:0.9rem; line-height:1.7;">อัปโหลดรูปภาพอาหาร — CNN จะจำแนกประเภท แล้ว ML จะทำนายระดับแคลอรี่</p>
#     </div>
#     """, unsafe_allow_html=True)

#     uploaded = st.file_uploader("📁 Upload Food Image (JPG / PNG)", type=["jpg", "jpeg", "png"])

#     if uploaded:

#         col1, col2 = st.columns([1, 1.5])

#         with col1:
#             img_display = Image.open(uploaded).convert("RGB")
#             st.image(img_display, caption="Uploaded Image", use_container_width=True)

#         with col2:
#             IMG_SIZE = 160
#             img = img_display.resize((IMG_SIZE, IMG_SIZE))
#             img_array = np.array(img) / 255.0
#             img_array = np.expand_dims(img_array, axis=0)

#             prediction = cnn_model.predict(img_array)
#             predicted_index = np.argmax(prediction)
#             confidence = np.max(prediction)
#             predicted_food = class_names[predicted_index]

#             st.markdown(f"""
#             <div class="section-card" style="margin-top:0;">
#                 <div class="section-title">🍽️ Predicted Food</div>
#                 <div style="font-size:1.8rem; font-weight:700; color:#f9c74f; margin: 8px 0;">{predicted_food}</div>
#                 <div style="color:#9e9e9e; font-size:0.88rem;">Confidence: <b style="color:#f3722c;">{confidence*100:.2f}%</b></div>
#             </div>
#             """, unsafe_allow_html=True)

#             row = pd.DataFrame()
#             food_list = food_df["Food"].tolist()
#             match = difflib.get_close_matches(predicted_food, food_list, n=1, cutoff=0.5)

#             if match:
#                 matched_food = match[0]
#                 row = food_df[food_df["Food"] == matched_food]

#             if len(row) > 0:
#                 grams = row["Grams"].values[0]
#                 predicted_level = predict_calorie_level(row["Food"].values[0], grams)

#                 level_colors = {"Low": ("#4caf50", "🟢"), "Medium": ("#ffc107", "🟡"), "High": ("#f44336", "🔴")}
#                 color, emoji = level_colors.get(predicted_level, ("#9e9e9e", "⚪"))
#                 r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

#                 st.markdown(f"""
#                 <div style="background:rgba({r},{g},{b},0.15); border:1px solid {color}66;
#                             border-radius:12px; padding:1.2rem; text-align:center; margin-top:0.8rem;">
#                     <div style="font-size:0.75rem; color:#9e9e9e; text-transform:uppercase; letter-spacing:0.1em;">Calorie Level</div>
#                     <div style="font-size:1.8rem; margin:4px 0;">{emoji}</div>
#                     <div style="font-size:1.8rem; font-weight:700; color:{color};">{predicted_level}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#             else:
#                 st.warning("Food not found in ML database")

#             st.markdown(f"""
#             <div class="metric-card" style="margin-top:12px; text-align:left;">
#                 <span style="color:#9e9e9e; font-size:0.8rem;">NN Accuracy: </span>
#                 <b style="color:#f9c74f;">{cnn_metrics['Accuracy']*100:.2f}%</b>
#             </div>
#             """, unsafe_allow_html=True)

import streamlit as st
import joblib
import numpy as np
import pandas as pd
import difflib
from tensorflow.keras.models import load_model
from PIL import Image

st.set_page_config(
    page_title="Food Calorie AI",
    page_icon="🍽️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=Fraunces:ital,wght@0,700;1,400&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
    -webkit-font-smoothing: antialiased;
}

/* ===================== BACKGROUND ===================== */
.stApp {
    background: #0c0e14;
    color: #e8e4dc;
    min-height: 100vh;
}

/* Subtle grid pattern overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(249,199,79,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(249,199,79,0.03) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    z-index: 0;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 2rem 3rem 4rem;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

/* ===================== HERO ===================== */
.hero-wrap {
    text-align: center;
    padding: 2.5rem 0 1rem;
    position: relative;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(249,199,79,0.1);
    border: 1px solid rgba(249,199,79,0.25);
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #f9c74f;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}

.hero-title {
    font-family: 'Fraunces', serif;
    font-size: clamp(2.4rem, 5vw, 3.6rem);
    font-weight: 700;
    line-height: 1.1;
    color: #f0ece2;
    margin-bottom: 0.6rem;
    letter-spacing: -0.02em;
}

.hero-title span {
    background: linear-gradient(95deg, #f9c74f 0%, #f3722c 55%, #f94144 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-size: 0.9rem;
    color: #6b6b7a;
    letter-spacing: 0.08em;
    font-weight: 400;
    margin-bottom: 2.5rem;
}

/* ===================== NAV ===================== */
.nav-wrap {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-bottom: 2.5rem;
    flex-wrap: wrap;
}

/* Override stButton for nav only */
div[data-testid="stHorizontalBlock"] .stButton > button {
    background: rgba(255,255,255,0.04) !important;
    color: #8a8a9a !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 100px !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    padding: 0.55rem 1.4rem !important;
    transition: all 0.2s ease !important;
    box-shadow: none !important;
    width: auto !important;
    letter-spacing: 0.01em !important;
}

div[data-testid="stHorizontalBlock"] .stButton > button:hover {
    background: rgba(249,199,79,0.08) !important;
    border-color: rgba(249,199,79,0.3) !important;
    color: #f9c74f !important;
}

/* ===================== DIVIDER ===================== */
hr {
    border: none !important;
    border-top: 1px solid rgba(255,255,255,0.06) !important;
    margin: 0 0 2rem !important;
}

/* ===================== CARDS ===================== */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 1.8rem 2rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s;
}

.card:hover { border-color: rgba(249,199,79,0.15); }

.card-hero {
    background: linear-gradient(135deg, rgba(249,199,79,0.07) 0%, rgba(243,114,44,0.04) 100%);
    border: 1px solid rgba(249,199,79,0.12);
    border-radius: 20px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.4rem;
}

.card-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #f9c74f;
    margin-bottom: 0.9rem;
    display: flex;
    align-items: center;
    gap: 6px;
}

.card-label::before {
    content: '';
    width: 18px;
    height: 2px;
    background: linear-gradient(90deg, #f9c74f, #f3722c);
    border-radius: 2px;
}

.card-title {
    font-family: 'Fraunces', serif;
    font-size: 1.25rem;
    color: #f0ece2;
    margin-bottom: 0.7rem;
    font-weight: 700;
    letter-spacing: -0.01em;
}

.card p {
    color: #9a9aaa;
    font-size: 0.88rem;
    line-height: 1.75;
}

/* ===================== TAGS ===================== */
.tags { display: flex; flex-wrap: wrap; gap: 6px; margin: 0.8rem 0; }

.tag {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 12px;
    background: rgba(249,199,79,0.08);
    border: 1px solid rgba(249,199,79,0.18);
    border-radius: 100px;
    color: #f9c74f;
    font-size: 0.76rem;
    font-weight: 500;
}

.tag-neutral {
    background: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.1);
    color: #b0b0c0;
}

/* ===================== STEP LIST ===================== */
.steps { display: flex; flex-direction: column; gap: 2px; margin-top: 0.5rem; }

.step {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.step:last-child { border-bottom: none; }

.step-num {
    width: 24px; height: 24px; min-width: 24px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f9c74f, #f3722c);
    color: #0c0e14;
    font-weight: 700; font-size: 0.72rem;
    display: flex; align-items: center; justify-content: center;
    margin-top: 1px;
}

.step-text {
    color: #b0b0c0;
    font-size: 0.86rem;
    line-height: 1.6;
    padding-top: 2px;
}

/* ===================== BADGES ===================== */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 10px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.09);
    color: #c8c4bc;
    font-size: 0.82rem;
    font-weight: 500;
    margin: 3px;
}

/* ===================== METRICS ===================== */
.metric-grid { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 0.8rem; }

.metric {
    flex: 1;
    min-width: 120px;
    background: rgba(249,199,79,0.06);
    border: 1px solid rgba(249,199,79,0.14);
    border-radius: 14px;
    padding: 1rem 1.2rem;
    text-align: center;
}

.metric-val {
    font-family: 'Fraunces', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #f9c74f;
    line-height: 1;
    margin-bottom: 4px;
}

.metric-lbl {
    font-size: 0.7rem;
    color: #6b6b7a;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* ===================== REFS ===================== */
.ref {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.ref:last-child { border-bottom: none; }

.ref-dot {
    width: 6px; height: 6px; min-width: 6px;
    border-radius: 50%;
    background: #f3722c;
    margin-top: 6px;
}

.ref-text {
    font-size: 0.84rem;
    color: #8a8a9a;
    line-height: 1.6;
}

.ref-text a { color: #f9c74f; text-decoration: none; }
.ref-text a:hover { text-decoration: underline; }

/* ===================== PREDICTION RESULT ===================== */
.result-card {
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    margin: 1.2rem 0;
}

.result-emoji { font-size: 2.8rem; margin-bottom: 0.4rem; }
.result-label-sm { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #6b6b7a; margin-bottom: 0.4rem; }
.result-level { font-family: 'Fraunces', serif; font-size: 2.4rem; font-weight: 700; line-height: 1; }

/* ===================== SELECTBOX ===================== */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] span,
div[data-baseweb="select"] input,
div[data-baseweb="select"] [class*="singleValue"],
div[data-baseweb="select"] [class*="placeholder"],
div[data-baseweb="select"] * {
    color: #e8e4dc !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 0.88rem !important;
}

ul[data-baseweb="menu"] li,
ul[role="listbox"] li,
[role="option"] {
    color: #1a1a1a !important;
    background: #ffffff !important;
    font-size: 0.88rem !important;
}
[role="option"]:hover,
[role="option"][aria-selected="true"] {
    background: #fff8ed !important;
    color: #1a1a1a !important;
}

.stSelectbox label { color: #9a9aaa !important; font-size: 0.82rem !important; font-weight: 500 !important; }

/* ===================== PREDICT BUTTON ===================== */
.stButton > button {
    background: linear-gradient(135deg, #f9c74f 0%, #f3722c 100%) !important;
    color: #0c0e14 !important;
    border: none !important;
    border-radius: 100px !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.7rem 2rem !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 24px rgba(243,114,44,0.3) !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 32px rgba(243,114,44,0.45) !important;
}

/* ===================== FILE UPLOADER ===================== */
[data-testid="stFileUploaderDropzone"] {
    background: rgba(255,255,255,0.03) !important;
    border: 2px dashed rgba(249,199,79,0.25) !important;
    border-radius: 16px !important;
    transition: border-color 0.2s !important;
}

[data-testid="stFileUploaderDropzone"]:hover {
    border-color: rgba(249,199,79,0.5) !important;
}

[data-testid="stFileUploaderDropzone"] p,
[data-testid="stFileUploaderDropzone"] span,
[data-testid="stFileUploaderDropzone"] small {
    color: #6b6b7a !important;
    font-family: 'Sora', sans-serif !important;
}

[data-testid="stFileUploaderDropzone"] button {
    color: #f9c74f !important;
    border: 1px solid rgba(249,199,79,0.3) !important;
    background: transparent !important;
    border-radius: 100px !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 0.8rem !important;
}

.stFileUploader label { color: #9a9aaa !important; font-size: 0.82rem !important; }

[data-testid="stFileUploaderFile"],
[data-testid="stFileUploaderFileName"],
[data-testid="stFileUploaderFile"] span,
[data-testid="stFileUploaderFile"] small,
[data-testid="stFileUploaderFile"] p {
    color: #c8c4bc !important;
}

[data-testid="stFileUploaderDeleteBtn"] button {
    color: #c8c4bc !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* ===================== STREAMLIT OVERRIDES ===================== */
.stWarning, .stSuccess, .stError, .stInfo {
    border-radius: 12px !important;
    font-family: 'Sora', sans-serif !important;
}

/* image caption */
.stImage figcaption {
    color: #6b6b7a !important;
    font-size: 0.78rem !important;
    text-align: center;
    margin-top: 6px;
}
</style>
""", unsafe_allow_html=True)

# ===================== HERO =====================
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">✦ AI-Powered · Thai University Project</div>
    <div class="hero-title">Food Calorie <span>Intelligence</span></div>
    <div class="hero-sub">MACHINE LEARNING & NEURAL NETWORK · CALORIE PREDICTION SYSTEM</div>
</div>
""", unsafe_allow_html=True)

# ===================== NAVIGATION =====================
if "page" not in st.session_state:
    st.session_state.page = "ML Explanation"

pages = ["ML Explanation", "NN Explanation", "ML Prediction", "NN Prediction"]
icons = ["🤖", "🧠", "🔍", "📷"]

cols = st.columns(len(pages))
for i, (p, icon) in enumerate(zip(pages, icons)):
    with cols[i]:
        label = f"{icon}  {p}" if st.session_state.page != p else f"● {icon}  {p}"
        if st.button(label, key=f"nav_{p}", use_container_width=True):
            st.session_state.page = p
            st.rerun()

page = st.session_state.page
st.markdown("---")

# ===================== LOAD MODELS =====================
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

def predict_calorie_level(food_name, grams):
    input_data = pd.DataFrame(columns=feature_columns)
    input_data.loc[0] = 0
    if "Grams" in input_data.columns:
        input_data["Grams"] = grams
    food_column = f"Food_{food_name}"
    if food_column in input_data.columns:
        input_data[food_column] = 1
    pred = ensemble.predict(input_data)[0]
    return {0: "Low", 1: "Medium", 2: "High"}.get(pred, "Unknown")


# ===================== ML EXPLANATION =====================
if page == "ML Explanation":

    st.markdown("""
    <div class="card-hero">
        <div class="card-label">Machine Learning</div>
        <div class="card-title">Calorie Level Classification</div>
        <p>ระบบนี้ถูกพัฒนาขึ้นเพื่อทำนาย <b style="color:#f0ece2;">ระดับพลังงาน (Calorie Level)</b> ของอาหาร
        โดยใช้เทคนิค <b style="color:#f0ece2;">Ensemble Learning</b> — การรวมโมเดลหลายตัวเข้าด้วยกันเพื่อเพิ่มความแม่นยำ</p>
        <div class="tags" style="margin-top:1rem;">
            <span class="tag">🟢 Low — แคลอรี่ต่ำ</span>
            <span class="tag">🟡 Medium — แคลอรี่ปานกลาง</span>
            <span class="tag">🔴 High — แคลอรี่สูง</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Dataset</div>
            <p style="margin-bottom:0.8rem;">ข้อมูลจาก 2 ไฟล์ที่รวมกันเพื่อเพิ่มจำนวนข้อมูลสำหรับการฝึกโมเดล</p>
            <div class="tags">
                <span class="tag-neutral tag">📄 calorie_infos.csv</span>
                <span class="tag-neutral tag">📄 Food and Calories - Sheet1.csv</span>
            </div>
            <p style="margin-top:0.9rem;">
            Features หลักที่ใช้ ได้แก่
            <b style="color:#f9c74f;">Food Name</b> ·
            <b style="color:#f9c74f;">Serving Size (Grams)</b> ·
            <b style="color:#f9c74f;">Calories</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-label">Feature Engineering</div>
            <p>Feature ที่ใช้ฝึกโมเดล ได้แก่ <b style="color:#f0ece2;">Food Name</b> และ <b style="color:#f0ece2;">Serving Size (Grams)</b></p>
            <p style="margin-top:0.6rem;">เนื่องจาก Food Name เป็น categorical data จึงใช้เทคนิค
            <b style="color:#f9c74f;">One-Hot Encoding</b> แปลงเป็นตัวเลขก่อนนำไปใช้กับโมเดล</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-label">ML Models</div>
            <p style="margin-bottom:0.8rem;">โมเดลทั้ง 3 ถูกรวมด้วย <b style="color:#f9c74f;">Soft Voting Ensemble</b></p>
            <div class="tags">
                <span class="badge">🌲 Random Forest</span>
                <span class="badge">📈 Gradient Boosting</span>
                <span class="badge">📐 Logistic Regression</span>
            </div>
            <p style="margin-top:0.8rem;">Soft Voting คำนวณค่า Probability จากทุกโมเดล
            แล้วเลือกคลาสที่มีค่าสูงที่สุดเป็นผลลัพธ์สุดท้าย</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        steps = [
            ("รวม Dataset", "นำข้อมูลจากหลายไฟล์มารวมกัน"),
            ("ลบ Missing Values", "ตรวจสอบและลบข้อมูลที่ขาดหาย"),
            ("แปลง Serving Size", "แปลงหน่วยให้เป็นกรัม (Grams) ทั้งหมด"),
            ("แปลง Calories", "แปลงค่าพลังงานให้อยู่ในรูปตัวเลข"),
            ("Drop Duplicates", "ลบข้อมูลที่ซ้ำกันออก"),
        ]
        steps_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Data Preprocessing</div>
            <p style="margin-bottom:0.8rem;">ขั้นตอนเตรียมข้อมูลก่อนนำไปฝึกโมเดล</p>
            <div class="steps">{steps_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <div class="card-label">Model Performance</div>
        <div class="metric-grid">
            <div class="metric">
                <div class="metric-val">{ml_metrics['Accuracy']*100:.2f}%</div>
                <div class="metric-lbl">Accuracy</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-label">References</div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">Dataset 1</b> — Calories in Food Items per 100gm/Ounce/Serving
            <br><a href="https://www.kaggle.com/datasets/syedjaferk/calories-in-food-items-per-100gm-ounce-serving" target="_blank">Kaggle · syedjaferk ↗</a></div>
        </div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">Dataset 2</b> — Food and Their Calories
            <br><a href="https://www.kaggle.com/datasets/vaishnavivenkatesan/food-and-their-calories" target="_blank">Kaggle · vaishnavivenkatesan ↗</a></div>
        </div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">Scikit-learn</b> — Random Forest, Gradient Boosting, Logistic Regression, VotingClassifier
            <br><a href="https://scikit-learn.org" target="_blank">scikit-learn.org ↗</a></div>
        </div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">Pandas</b> — <a href="https://pandas.pydata.org" target="_blank">pandas.pydata.org ↗</a>
            &nbsp;·&nbsp; <b style="color:#c8c4bc;">NumPy</b> — <a href="https://numpy.org" target="_blank">numpy.org ↗</a></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ===================== NN EXPLANATION =====================
elif page == "NN Explanation":

    st.markdown("""
    <div class="card-hero">
        <div class="card-label">Neural Network</div>
        <div class="card-title">Food Image Classification</div>
        <p>โมเดลถูกพัฒนาเพื่อ <b style="color:#f0ece2;">จำแนกประเภทอาหารจากรูปภาพ</b>
        โดยใช้เทคนิค <b style="color:#f0ece2;">Convolutional Neural Network (CNN)</b>
        ซึ่งเหมาะสำหรับงานด้าน Computer Vision โดยเฉพาะ</p>
        <div class="tags" style="margin-top:1rem;">
            <span class="tag">🍕 Pizza</span>
            <span class="tag">🍔 Burger</span>
            <span class="tag">🥗 Salad</span>
            <span class="tag">🍜 Noodles</span>
            <span class="tag">🍚 Fried Rice</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Dataset</div>
            <div class="tags" style="margin-bottom:0.8rem;">
                <span class="tag-neutral tag">🖼️ Food Image Classification Dataset</span>
            </div>
            <p>รูปภาพอาหารหลายประเภทจาก Kaggle ใช้สำหรับฝึกโมเดลให้
            <b style="color:#f0ece2;">จำแนกประเภทอาหารจากภาพ</b> ได้</p>
        </div>
        """, unsafe_allow_html=True)

        pre_steps = [
            ("Resize", "ปรับขนาดภาพเป็น 160×160 pixels"),
            ("Normalize", "ปรับค่า Pixel ให้อยู่ในช่วง 0–1"),
            ("Data Augmentation", "Rotation · Horizontal Flip · Zoom · Brightness"),
        ]
        pre_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(pre_steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Image Preprocessing</div>
            <p style="margin-bottom:0.8rem;">ขั้นตอนเตรียมภาพก่อนส่งเข้าโมเดล CNN</p>
            <div class="steps">{pre_html}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        arch_steps = [
            ("Convolution Layer", "สกัดคุณลักษณะสำคัญ เช่น รูปร่าง ขอบ และพื้นผิว"),
            ("ReLU Activation", "เพิ่ม Non-linearity ให้โมเดล"),
            ("MaxPooling Layer", "ลด Dimension ของข้อมูล"),
            ("Dropout Layer", "ป้องกัน Overfitting"),
            ("Fully Connected", "รวมข้อมูลเพื่อการตัดสินใจ"),
            ("Softmax Output", "จำแนกประเภทอาหาร"),
        ]
        arch_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(arch_steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">CNN Architecture</div>
            <p style="margin-bottom:0.8rem;">โครงสร้าง Layer หลักของโมเดล</p>
            <div class="steps">{arch_html}</div>
        </div>
        """, unsafe_allow_html=True)

        pred_steps = [
            ("Upload", "ผู้ใช้อัปโหลดรูปอาหาร"),
            ("Preprocess", "Resize & Normalize ภาพ"),
            ("CNN Predict", "จำแนกประเภทอาหาร"),
            ("Dataset Match", "ค้นหาชื่ออาหารใน Dataset"),
            ("ML Predict", "ทำนายระดับแคลอรี่"),
        ]
        pred_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(pred_steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Prediction Process</div>
            <p style="margin-bottom:0.8rem;">ระบบนี้เป็น <b style="color:#f9c74f;">Hybrid AI System</b> — NN + ML ทำงานร่วมกัน</p>
            <div class="steps">{pred_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <div class="card-label">Model Performance</div>
        <div class="metric-grid">
            <div class="metric">
                <div class="metric-val">{cnn_metrics['Accuracy']*100:.2f}%</div>
                <div class="metric-lbl">Accuracy</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-label">References</div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">Dataset</b> — Food Image Classification Dataset
            <br><a href="https://www.kaggle.com/datasets/harishkumardatalab/food-image-classification-dataset" target="_blank">Kaggle · harishkumardatalab ↗</a></div>
        </div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">TensorFlow / Keras</b> — <a href="https://www.tensorflow.org" target="_blank">tensorflow.org ↗</a></div>
        </div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">Convolutional Neural Network</b> — LeCun et al., 1998</div>
        </div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">Keras ImageDataGenerator</b> — <a href="https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator" target="_blank">TF Docs ↗</a></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ===================== ML PREDICTION =====================
elif page == "ML Prediction":

    st.markdown("""
    <div class="card-hero">
        <div class="card-label">ML Prediction</div>
        <div class="card-title">Calorie Level Predictor</div>
        <p>เลือกชื่ออาหารเพื่อทำนายระดับแคลอรี่ด้วย <b style="color:#f0ece2;">ML Ensemble Model</b></p>
    </div>
    """, unsafe_allow_html=True)

    food_list = sorted(food_df["Food"].unique())
    food_name = st.selectbox("เลือกอาหาร / Select Food", food_list)

    col_btn, _ = st.columns([1, 2])
    with col_btn:
        predict_clicked = st.button("✦  Predict Calorie Level")

    if predict_clicked:
        row = food_df[food_df["Food"] == food_name]

        if len(row) > 0:
            grams = row["Grams"].values[0]
            actual_cal = row["Calories"].values[0]
            predicted_level = predict_calorie_level(food_name, grams)

            palette = {
                "Low":    {"color": "#4caf50", "bg": "rgba(76,175,80,0.08)",    "border": "rgba(76,175,80,0.25)",  "emoji": "🟢"},
                "Medium": {"color": "#f9c74f", "bg": "rgba(249,199,79,0.08)",   "border": "rgba(249,199,79,0.25)", "emoji": "🟡"},
                "High":   {"color": "#f44336", "bg": "rgba(244,67,54,0.08)",    "border": "rgba(244,67,54,0.25)",  "emoji": "🔴"},
            }
            p = palette.get(predicted_level, {"color": "#9e9e9e", "bg": "rgba(158,158,158,0.08)", "border": "rgba(158,158,158,0.25)", "emoji": "⚪"})

            st.markdown(f"""
            <div style="background:{p['bg']}; border:1px solid {p['border']};
                        border-radius:20px; padding:2.5rem 2rem; text-align:center; margin:1rem 0;">
                <div class="result-label-sm">Predicted Calorie Level</div>
                <div class="result-emoji">{p['emoji']}</div>
                <div class="result-level" style="color:{p['color']};">{predicted_level}</div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f"""<div class="metric"><div class="metric-val" style="font-size:1.7rem;">{int(actual_cal)}</div><div class="metric-lbl">Actual kcal</div></div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""<div class="metric"><div class="metric-val" style="font-size:1.7rem;">{int(grams)}g</div><div class="metric-lbl">Serving Size</div></div>""", unsafe_allow_html=True)
            with c3:
                st.markdown(f"""<div class="metric"><div class="metric-val" style="font-size:1.7rem;">{ml_metrics['Accuracy']*100:.1f}%</div><div class="metric-lbl">ML Accuracy</div></div>""", unsafe_allow_html=True)

        else:
            st.warning("Food not found in dataset")


# ===================== NN PREDICTION =====================
elif page == "NN Prediction":

    st.markdown("""
    <div class="card-hero">
        <div class="card-label">NN Prediction</div>
        <div class="card-title">Food Image Classifier</div>
        <p>อัปโหลดรูปภาพอาหาร — <b style="color:#f0ece2;">CNN</b> จะจำแนกประเภท
        แล้ว <b style="color:#f0ece2;">ML</b> จะทำนายระดับแคลอรี่</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("อัปโหลดรูปอาหาร (JPG / PNG)", type=["jpg", "jpeg", "png"])

    if uploaded:
        col1, col2 = st.columns([1, 1.4], gap="large")

        with col1:
            img_display = Image.open(uploaded).convert("RGB")
            st.image(img_display, caption="Uploaded Image", use_container_width=True)

        with col2:
            IMG_SIZE = 160
            img_arr = np.array(img_display.resize((IMG_SIZE, IMG_SIZE))) / 255.0
            img_arr = np.expand_dims(img_arr, axis=0)

            prediction = cnn_model.predict(img_arr)
            predicted_index = np.argmax(prediction)
            confidence = np.max(prediction)
            predicted_food = class_names[predicted_index]

            st.markdown(f"""
            <div class="card" style="margin-top:0;">
                <div class="card-label">Predicted Food</div>
                <div style="font-family:'Fraunces',serif; font-size:1.9rem; color:#f0ece2; font-weight:700;
                            margin:0.4rem 0 0.3rem; letter-spacing:-0.01em;">{predicted_food}</div>
                <div style="font-size:0.83rem; color:#6b6b7a;">Confidence — <b style="color:#f3722c;">{confidence*100:.1f}%</b></div>
            </div>
            """, unsafe_allow_html=True)

            # ML calorie match
            row = pd.DataFrame()
            food_list_ml = food_df["Food"].tolist()
            match = difflib.get_close_matches(predicted_food, food_list_ml, n=1, cutoff=0.5)
            if match:
                row = food_df[food_df["Food"] == match[0]]

            if len(row) > 0:
                grams = row["Grams"].values[0]
                predicted_level = predict_calorie_level(row["Food"].values[0], grams)

                palette = {
                    "Low":    {"color": "#4caf50", "bg": "rgba(76,175,80,0.08)",    "border": "rgba(76,175,80,0.25)",  "emoji": "🟢"},
                    "Medium": {"color": "#f9c74f", "bg": "rgba(249,199,79,0.08)",   "border": "rgba(249,199,79,0.25)", "emoji": "🟡"},
                    "High":   {"color": "#f44336", "bg": "rgba(244,67,54,0.08)",    "border": "rgba(244,67,54,0.25)",  "emoji": "🔴"},
                }
                p = palette.get(predicted_level, {"color": "#9e9e9e", "bg": "rgba(158,158,158,0.08)", "border": "rgba(158,158,158,0.25)", "emoji": "⚪"})

                st.markdown(f"""
                <div style="background:{p['bg']}; border:1px solid {p['border']};
                            border-radius:16px; padding:1.5rem; text-align:center; margin-top:0.8rem;">
                    <div class="result-label-sm">Calorie Level</div>
                    <div style="font-size:2rem; margin:4px 0;">{p['emoji']}</div>
                    <div style="font-family:'Fraunces',serif; font-size:1.8rem; font-weight:700; color:{p['color']};">{predicted_level}</div>
                </div>
                """, unsafe_allow_html=True)

            else:
                st.warning("Food not found in ML database")

            st.markdown(f"""
            <div class="metric" style="margin-top:12px; text-align:center;">
                <div class="metric-val" style="font-size:1.4rem;">{cnn_metrics['Accuracy']*100:.1f}%</div>
                <div class="metric-lbl">NN Accuracy</div>
            </div>
            """, unsafe_allow_html=True)