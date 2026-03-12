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
    <div class="hero-badge">✦ Calorie AI · Intelligent Systems Project</div>
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
        if st.button(f"{icon}  {p}", key=f"nav_{p}", use_container_width=True):
            st.session_state.page = p
            st.rerun()

active_index = pages.index(st.session_state.page) + 1
st.markdown(f"""
<style>
div[data-testid="stHorizontalBlock"] > div:nth-child({active_index}) .stButton > button {{
    background: linear-gradient(135deg, #f9c74f 0%, #f3722c 100%) !important;
    color: #0c0e14 !important;
    border-color: transparent !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 20px rgba(243,114,44,0.4) !important;
}}
</style>
""", unsafe_allow_html=True)

page = st.session_state.page
st.markdown("---")

# ===================== LOAD MODELS =====================
# @st.cache_resource
# def load_models():
#     ensemble = joblib.load("models/ensemble_model.pkl")
#     cnn_model = load_model("models/cnn_model.h5",compile=False)
#     food_df = joblib.load("models/food_full_data.pkl")
#     ml_metrics = joblib.load("models/ml_metrics.pkl")
#     cnn_metrics = joblib.load("models/cnn_metrics.pkl")
#     class_names = joblib.load("models/cnn_class_names.pkl")
#     feature_columns = joblib.load("models/feature_columns.pkl")
#     return ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns
# @st.cache_resource
# def load_models():
#     try:
#         ensemble = joblib.load("models/ensemble_model.pkl")
#         # cnn_model = load_model("models/cnn_model.h5", compile=False)
#         cnn_model = load_model("models/cnn_model.keras", compile=False)
#         food_df = joblib.load("models/food_full_data.pkl")
#         ml_metrics = joblib.load("models/ml_metrics.pkl")
#         cnn_metrics = joblib.load("models/cnn_metrics.pkl")
#         class_names = joblib.load("models/cnn_class_names.pkl")
#         feature_columns = joblib.load("models/feature_columns.pkl")

#         return ensemble, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns

#     except Exception as e:
#         st.error(f"Model loading error: {e}")
#         st.stop()
# @st.cache_resource
# def load_models():
#     try:
#         ml_model = joblib.load("models/food_calorie_model.pkl")
#         cnn_model = load_model("models/cnn_model.h5", compile=False)

#         ml_metrics = joblib.load("models/ml_metrics.pkl")
#         cnn_metrics = joblib.load("models/cnn_metrics.pkl")

#         class_names = joblib.load("models/cnn_class_names.pkl")

#         return ml_model, cnn_model, ml_metrics, cnn_metrics, class_names

#     except Exception as e:
#         st.error(f"Model loading error: {e}")
#         st.stop()
@st.cache_resource
def load_models():
    try:
        ml_model = joblib.load("models/ml_model.pkl")
        cnn_model = load_model("models/cnn_model.h5", compile=False)

        food_df = joblib.load("models/food_full_data.pkl")
        food_category_encoder = joblib.load("models/food_category_encoder.pkl")
        ml_metrics = joblib.load("models/ml_metrics.pkl")
        cnn_metrics = joblib.load("models/cnn_metrics.pkl")

        class_names = joblib.load("models/cnn_class_names.pkl")

        feature_columns = joblib.load("models/feature_columns.pkl")

        # return ml_model, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns
        return ml_model, cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns, food_category_encoder

    except Exception as e:
        st.error(f"Model loading error: {e}")
        st.stop()

# ml_model , cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns = load_models()
# ml_model , cnn_model, ml_metrics, cnn_metrics, class_names = load_models()
# ml_model , cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns = load_models()
ml_model , cnn_model, food_df, ml_metrics, cnn_metrics, class_names, feature_columns, food_category_encoder = load_models()

# def predict_calorie_level(food_name, grams):
#     input_data = pd.DataFrame(columns=feature_columns)
#     input_data.loc[0] = 0
#     if "Grams" in input_data.columns:
#         input_data["Grams"] = grams
#     food_column = f"Food_{food_name}"
#     if food_column in input_data.columns:
#         input_data[food_column] = 1
#     pred = ml_model.predict(input_data)[0]
#     return {0: "Low", 1: "Medium", 2: "High"}.get(pred, "Unknown")
# def predict_calorie_level(food_name, grams):

#     # สร้าง dataframe เต็มด้วย 0
#     input_data = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)
#     st.write(input_data)
#     # ใส่ grams
#     if "Grams" in input_data.columns:
#         input_data.loc[0, "Grams"] = grams

#     # one-hot food
#     food_column = f"Food_{food_name}"
#     if food_column in input_data.columns:
#         input_data.loc[0, food_column] = 1

#     # predict
#     # pred = ml_model.predict(input_data)[0]
#     # pred = int(pred)

#     # return {0: "Low", 1: "Medium", 2: "High"}.get(pred, "Unknown")
#     pred = ml_model.predict(input_data)[0]
#     return pred
def predict_calorie_level(food_name, grams, calories, category_encoded):

    input_data = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

    input_data.loc[0,"serving_value"] = grams
    input_data.loc[0,"cal_per_gram"] = calories / grams
    input_data.loc[0,"food_category"] = category_encoded

    pred = ml_model.predict(input_data)[0]

    return pred


# ===================== ML EXPLANATION =====================
if page == "ML Explanation":

    st.markdown("""
    <div class="card-hero">
        <div class="card-label">Machine Learning</div>
        <div class="card-title">Calorie Level Classification</div>
        <p>ระบบนี้ถูกพัฒนาขึ้นเพื่อทำนาย <b style="color:#f0ece2;">ระดับพลังงาน (Calorie Level)</b> ของอาหาร
        โดยใช้เทคนิค <b style="color:#f0ece2;">Ensemble Learning</b> — การรวมโมเดลหลายตัวเข้าด้วยกันเพื่อเพิ่มความแม่นยำในการจำแนกประเภท
        โดยแบ่งระดับแคลอรี่ออกเป็น 3 กลุ่มตามปริมาณพลังงานของอาหารต่อ serving</p>
        <div class="tags" style="margin-top:1rem;">
            <span class="tag">🟢 Low — น้อยกว่า 200 kcal</span>
            <span class="tag">🟡 Medium — 200–400 kcal</span>
            <span class="tag">🔴 High — มากกว่า 400 kcal</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Dataset</div>
            <p style="margin-bottom:0.8rem;">รวบรวมข้อมูลจาก <b style="color:#f0ece2;">2 แหล่ง</b> บน Kaggle เพื่อให้ครอบคลุมรายการอาหารหลากหลายมากขึ้น
            และเพิ่มความหลากหลายของข้อมูลก่อนนำไปฝึกโมเดล</p>
            <div class="tags">
                <span class="tag-neutral tag">📄 calorie_infos.csv</span>
                <span class="tag-neutral tag">📄 Food and Calories - Sheet1.csv</span>
            </div>
            <p style="margin-top:0.9rem;">
            Features หลักที่ใช้ในการฝึกโมเดล ได้แก่
            <b style="color:#f9c74f;">Food Name</b> (ชื่ออาหาร) ·
            <b style="color:#f9c74f;">Serving Size (Grams)</b> (น้ำหนักต่อครั้ง) ·
            <b style="color:#f9c74f;">Calories</b> (พลังงานที่ใช้สร้าง Label)
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-label">Feature Engineering</div>
            <p>Feature ที่ใช้ฝึกโมเดล ได้แก่ <b style="color:#f0ece2;">Food Name</b> และ <b style="color:#f0ece2;">Serving Size (Grams)</b>
            โดยตัด Calories ออกจาก input เพื่อให้โมเดลเรียนรู้จากชื่ออาหารและขนาด serving แทน</p>
            <p style="margin-top:0.6rem;">เนื่องจาก Food Name เป็น <b style="color:#f0ece2;">Categorical Data</b> จึงใช้เทคนิค
            <b style="color:#f9c74f;">One-Hot Encoding</b> แปลงชื่ออาหารแต่ละรายการให้เป็นคอลัมน์ตัวเลข 0/1
            ก่อนนำไปใช้กับโมเดล ML</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-label">ML Models</div>
            <p style="margin-bottom:0.8rem;">ใช้โมเดล 3 ตัวรวมกันด้วยเทคนิค <b style="color:#f9c74f;">Soft Voting Ensemble</b>
            เพื่อให้ผลลัพธ์มีความเสถียรและแม่นยำกว่าการใช้โมเดลเดียว</p>
            <div class="tags" style="margin-bottom:0.8rem;">
                <span class="badge">🌲 Random Forest</span>
                <span class="badge">📈 Gradient Boosting</span>
                <span class="badge">📐 Logistic Regression</span>
            </div>
            <p><b style="color:#f0ece2;">Random Forest</b> — สร้าง Decision Tree จำนวนมากแล้ว vote ผลลัพธ์</p>
            <p style="margin-top:0.4rem;"><b style="color:#f0ece2;">Gradient Boosting</b> — สร้างโมเดลสะสมแบบต่อเนื่อง แก้ข้อผิดพลาดของโมเดลก่อนหน้า</p>
            <p style="margin-top:0.4rem;"><b style="color:#f0ece2;">Logistic Regression</b> — โมเดล Linear ที่คำนวณ Probability ของแต่ละ Class</p>
            <p style="margin-top:0.6rem;">Soft Voting รวม Probability จากทุกโมเดล แล้วเลือก Class ที่มีค่าเฉลี่ยสูงที่สุดเป็นคำตอบสุดท้าย</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        steps = [
            ("รวม Dataset", "นำ CSV ทั้ง 2 ไฟล์มา concat และ reset index"),
            ("ลบ Missing Values", "ตรวจสอบและ dropna() ข้อมูลที่ขาดหาย"),
            ("แปลง Serving Size", "แปลงหน่วยต่างๆ เช่น oz, cup ให้เป็นกรัม (Grams)"),
            ("แปลง Calories", "แปลงค่าพลังงานให้อยู่ในรูปตัวเลข float"),
            ("Drop Duplicates", "ลบข้อมูลที่ซ้ำกันออกด้วย drop_duplicates()"),
            ("สร้าง Label", "แบ่ง Calories เป็น Low / Medium / High ด้วย pd.cut()"),
            ("One-Hot Encoding", "แปลง Food Name เป็น binary columns ด้วย pd.get_dummies()"),
            ("Train/Test Split", "แบ่งข้อมูล 80% train, 20% test"),
        ]
        steps_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Data Preprocessing</div>
            <p style="margin-bottom:0.8rem;">ขั้นตอนเตรียมข้อมูลทั้งหมดก่อนนำไปฝึกโมเดล</p>
            <div class="steps">{steps_html}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-label">Why Ensemble?</div>
            <p>การใช้ <b style="color:#f9c74f;">Ensemble Learning</b> ช่วยลด Variance และ Bias
            เมื่อเทียบกับการใช้โมเดลเดี่ยว เนื่องจากโมเดลแต่ละตัวมีจุดแข็งต่างกัน
            การรวมกันจึงช่วยชดเชยจุดอ่อนของแต่ละโมเดลได้</p>
            <p style="margin-top:0.6rem;">ตัวอย่างเช่น Random Forest เก่งเรื่อง Non-linear patterns
            ส่วน Logistic Regression เก่งเรื่อง Linear boundaries
            การรวมกันทำให้โมเดลครอบคลุม pattern ได้กว้างขึ้น</p>
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
        โดยใช้เทคนิค <b style="color:#f0ece2;">Transfer Learning</b> บน
        <b style="color:#f0ece2;">MobileNetV2</b> — โมเดลที่ผ่านการฝึกจากภาพ ImageNet กว่า 14 ล้านรูป
        นำมา Fine-tune ให้จำแนกประเภทอาหารได้โดยเฉพาะ</p>
        <div class="tags" style="margin-top:1rem;">
            <span class="tag">🍕 Pizza</span>
            <span class="tag">🍔 Burger</span>
            <span class="tag">🥗 Salad</span>
            <span class="tag">🍜 Noodles</span>
            <span class="tag">🍚 Fried Rice</span>
            <span class="tag">🍰 Dessert</span>
            <span class="tag">+ อื่นๆ</span>
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
            <p>รูปภาพอาหารหลายประเภทจาก Kaggle แต่ละ Class จะมีภาพอาหารในมุมมองและแสงที่หลากหลาย
            เพื่อให้โมเดลสามารถ <b style="color:#f0ece2;">Generalize</b> ได้ดีในสภาวะจริง</p>
            <p style="margin-top:0.6rem;">ข้อมูลถูกแบ่งเป็น <b style="color:#f9c74f;">80% Training</b>
            และ <b style="color:#f9c74f;">20% Validation</b> โดยอัตโนมัติผ่าน ImageDataGenerator</p>
        </div>
        """, unsafe_allow_html=True)

        pre_steps = [
            ("Resize", "ปรับขนาดภาพเป็น 160×160 pixels เพื่อให้ตรงกับ input ของ MobileNetV2"),
            ("Normalize", "หาร pixel ด้วย 255.0 เพื่อให้ค่าอยู่ในช่วง 0.0–1.0"),
            ("Rotation", "หมุนภาพแบบสุ่ม ±20° เพื่อเพิ่มความหลากหลาย"),
            ("Horizontal Flip", "พลิกภาพซ้าย-ขวาแบบสุ่ม"),
            ("Zoom", "ซูมเข้า-ออกแบบสุ่ม ±20%"),
        ]
        pre_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(pre_steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Image Preprocessing & Augmentation</div>
            <p style="margin-bottom:0.8rem;">เตรียมภาพและเพิ่มข้อมูลเทียม (Data Augmentation) เพื่อป้องกัน Overfitting</p>
            <div class="steps">{pre_html}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-label">Why MobileNetV2?</div>
            <p><b style="color:#f9c74f;">MobileNetV2</b> เป็น Lightweight CNN ที่ออกแบบมาสำหรับ
            งานที่ต้องการ <b style="color:#f0ece2;">ความเร็วสูงและขนาดโมเดลเล็ก</b>
            เหมาะสำหรับ deployment บน web application</p>
            <p style="margin-top:0.6rem;">ใช้เทคนิค <b style="color:#f9c74f;">Depthwise Separable Convolution</b>
            ที่ลด computation ได้มากกว่า Standard CNN แต่ยังรักษาความแม่นยำไว้ได้ดี</p>
            <p style="margin-top:0.6rem;">การใช้ <b style="color:#f9c74f;">Transfer Learning</b>
            ช่วยให้ไม่ต้องเทรนโมเดลจากศูนย์ ประหยัดเวลาและทรัพยากรได้มาก</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        arch_steps = [
            ("MobileNetV2 Base", "โหลด pretrained weights จาก ImageNet — freeze layer แรกๆ ไว้"),
            ("GlobalAveragePooling2D", "บีบอัด Feature Map ให้เหลือ 1D vector"),
            ("Dropout (0.4)", "ปิด neuron สุ่ม 40% ระหว่าง training ป้องกัน Overfitting"),
            ("Dense + Softmax", "Fully Connected layer สุดท้าย output ความน่าจะเป็นของแต่ละ Class"),
        ]
        arch_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(arch_steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Model Architecture</div>
            <p style="margin-bottom:0.8rem;">โครงสร้างโมเดลแบบ <b style="color:#f9c74f;">Transfer Learning</b> — ต่อยอดจาก MobileNetV2</p>
            <div class="steps">{arch_html}</div>
        </div>
        """, unsafe_allow_html=True)

        training_steps = [
            ("Phase 1 — Freeze", "Freeze ทุก layer ของ MobileNetV2, เทรนแค่ top layer, lr=0.001, 5 epochs"),
            ("Phase 2 — Fine-tune", "Unfreeze layer หลังๆ (layer 70+), เทรนซ้ำด้วย lr=0.00005, สูงสุด 12 epochs"),
            ("Early Stopping", "หยุดเทรนอัตโนมัติถ้า val_loss ไม่ดีขึ้นใน 3 epochs ติดกัน"),
            ("Save Model", "บันทึกโมเดลที่ดีที่สุด (restore_best_weights=True) เป็น .h5"),
        ]
        training_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(training_steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Training Strategy</div>
            <p style="margin-bottom:0.8rem;">เทรนแบบ <b style="color:#f9c74f;">2-Phase Fine-tuning</b> เพื่อให้โมเดล adapt กับข้อมูลได้ดีที่สุด</p>
            <div class="steps">{training_html}</div>
        </div>
        """, unsafe_allow_html=True)

        pred_steps = [
            ("Upload", "ผู้ใช้อัปโหลดรูปอาหาร JPG/PNG"),
            ("Preprocess", "Resize เป็น 160×160 และ Normalize ÷255"),
            ("CNN Predict", "MobileNetV2 จำแนกประเภทอาหาร + แสดง Confidence"),
            ("Dataset Match", "ค้นหาชื่ออาหารใน ML Dataset ด้วย difflib fuzzy matching"),
            ("ML Predict", "Ensemble Model ทำนายระดับแคลอรี่ Low/Medium/High"),
            ("Show Result", "แสดงผล Calorie Level + kcal + Serving Size"),
        ]
        pred_html = "".join([f'<div class="step"><div class="step-num">{i+1}</div><div class="step-text"><b style="color:#d0cfc8;">{t}</b> — {d}</div></div>' for i, (t, d) in enumerate(pred_steps)])
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Prediction Pipeline</div>
            <p style="margin-bottom:0.8rem;">ระบบนี้เป็น <b style="color:#f9c74f;">Hybrid AI System</b> — CNN + ML ทำงานร่วมกัน</p>
            <div class="steps">{pred_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <div class="card-label">Model Performance</div>
        <div class="metric-grid">
            <div class="metric">
                <div class="metric-val">{cnn_metrics['Accuracy']*100:.2f}%</div>
                <div class="metric-lbl">Validation Accuracy</div>
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
            <div class="ref-text"><b style="color:#c8c4bc;">MobileNetV2</b> — Sandler et al., 2018 · Inverted Residuals and Linear Bottlenecks
            <br><a href="https://arxiv.org/abs/1801.04381" target="_blank">arxiv.org/abs/1801.04381 ↗</a></div>
        </div>
        <div class="ref">
            <div class="ref-dot"></div>
            <div class="ref-text"><b style="color:#c8c4bc;">TensorFlow / Keras</b> — <a href="https://www.tensorflow.org" target="_blank">tensorflow.org ↗</a></div>
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

    food_list = sorted(food_df["food"].unique())
    food_name = st.selectbox("เลือกอาหาร / Select Food", food_list)

    col_btn, _ = st.columns([1, 2])
    with col_btn:
        predict_clicked = st.button("✦  Predict Calorie Level")

    if predict_clicked:
        row = food_df[food_df["food"] == food_name]

        if len(row) > 0:
            # grams = row["Grams"].values[0]
            grams = row["serving_value"].values[0]
            actual_cal = row["calories_combined"].values[0]
            category = row["food_category"].values[0]
            category_encoded = food_category_encoder.transform([category])[0]
            # predicted_level = predict_calorie_level(food_name, grams)
            predicted_level = predict_calorie_level(
                food_name,
                grams,
                actual_cal,
                category_encoded
            )

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
            st.image(img_display, caption="Uploaded Image",  width=400)

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

            # # ML calorie match
            # row = pd.DataFrame()
            # food_list_ml = food_df["food"].tolist()
            # match = difflib.get_close_matches(predicted_food, food_list_ml, n=1, cutoff=0.5)
            # if match:
            #     row = food_df[food_df["food"] == match[0]]

            # if len(row) > 0:
            #     grams = row["serving_value"].values[0]
            #     actual_cal = row["cal_per_gram"].values[0]
            #     predicted_level = predict_calorie_level(row["food"].values[0], grams)

            #     palette = {
            #         "Low":    {"color": "#4caf50", "bg": "rgba(76,175,80,0.08)",    "border": "rgba(76,175,80,0.25)",  "emoji": "🟢"},
            #         "Medium": {"color": "#f9c74f", "bg": "rgba(249,199,79,0.08)",   "border": "rgba(249,199,79,0.25)", "emoji": "🟡"},
            #         "High":   {"color": "#f44336", "bg": "rgba(244,67,54,0.08)",    "border": "rgba(244,67,54,0.25)",  "emoji": "🔴"},
            #     }
            #     p = palette.get(predicted_level, {"color": "#9e9e9e", "bg": "rgba(158,158,158,0.08)", "border": "rgba(158,158,158,0.25)", "emoji": "⚪"})
            # ML calorie match
            row = pd.DataFrame()
            food_list_ml = food_df["food"].tolist()
            match = difflib.get_close_matches(predicted_food, food_list_ml, n=1, cutoff=0.5)

            if match:
                row = food_df[food_df["food"] == match[0]]

            if len(row) > 0:

                grams = row["serving_value"].values[0]
                cal_per_gram = row["cal_per_gram"].values[0]
                category = row["food_category"].values[0]

                # คำนวณ calories
                calories = grams * cal_per_gram

                # encode category
                category_encoded = food_category_encoder.transform([category])[0]

                # predict ML
                predicted_level = predict_calorie_level(
                    row["food"].values[0],
                    grams,
                    calories,
                    category_encoded
                )

                palette = {
                    "Low":    {"color": "#4caf50", "bg": "rgba(76,175,80,0.08)",    "border": "rgba(76,175,80,0.25)",  "emoji": "🟢"},
                    "Medium": {"color": "#f9c74f", "bg": "rgba(249,199,79,0.08)",   "border": "rgba(249,199,79,0.25)", "emoji": "🟡"},
                    "High":   {"color": "#f44336", "bg": "rgba(244,67,54,0.08)",    "border": "rgba(244,67,54,0.25)",  "emoji": "🔴"},
                }

                p = palette.get(predicted_level, {
                    "color": "#9e9e9e",
                    "bg": "rgba(158,158,158,0.08)",
                    "border": "rgba(158,158,158,0.25)",
                    "emoji": "⚪"
                })
                st.markdown(f"""
                <div style="background:{p['bg']}; border:1px solid {p['border']};
                            border-radius:16px; padding:1.5rem; text-align:center; margin-top:0.8rem;">
                    <div class="result-label-sm">Calorie Level</div>
                    <div style="font-size:2rem; margin:4px 0;">{p['emoji']}</div>
                    <div style="font-family:'Fraunces',serif; font-size:1.8rem; font-weight:700; color:{p['color']};">{predicted_level}</div>
                </div>
                <div style="display:flex; gap:10px; margin-top:10px;">
                    <div class="metric" style="flex:1; text-align:center;">
                        <div class="metric-val" style="font-size:1.6rem; color:#f9c74f;">{int(calories)}</div>
                        <div class="metric-lbl">kcal / serving</div>
                    </div>
                    <div class="metric" style="flex:1; text-align:center;">
                        <div class="metric-val" style="font-size:1.6rem; color:#f9c74f;">{int(grams)}g</div>
                        <div class="metric-lbl">Serving Size</div>
                    </div>
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