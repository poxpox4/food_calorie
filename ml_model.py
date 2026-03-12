# import pandas as pd
# import joblib
# import re

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.utils import resample


# # =========================
# # LOAD DATA
# # =========================

# df1 = pd.read_csv("data/calorie_infos.csv")
# df2 = pd.read_csv("data/Food and Calories - Sheet1.csv")

# print("Dataset1 size:", len(df1))
# print("Dataset2 size:", len(df2))

# # lowercase columns
# df1.columns = df1.columns.str.lower()
# df2.columns = df2.columns.str.lower()

# df = pd.concat([df1, df2], ignore_index=True)

# print("\nTotal dataset size:", len(df))
# print("\nColumns in dataset:")
# print(df.columns)


# # =========================
# # CREATE CALORIES COLUMN
# # =========================

# df["calories_combined"] = None

# if "calories" in df.columns:
#     df["calories_combined"] = df["calories"]

# if "cal_per_serving" in df.columns:
#     df["calories_combined"] = df["calories_combined"].fillna(df["cal_per_serving"])

# if "cal_per_100_ml_or_gms" in df.columns:
#     df["calories_combined"] = df["calories_combined"].fillna(df["cal_per_100_ml_or_gms"])

# print("\nCalories column used: calories_combined")


# # =========================
# # EXTRACT NUMBER FUNCTION
# # =========================

# def extract_number(x):

#     if pd.isna(x):
#         return None

#     numbers = re.findall(r"\d+\.?\d*", str(x))

#     if len(numbers) == 0:
#         return None

#     return float(numbers[0])


# def extract_serving(x):

#     if pd.isna(x):
#         return None

#     numbers = re.findall(r"\d+\.?\d*", str(x))

#     if len(numbers) == 0:
#         return None

#     return float(numbers[-1])  # เช่น (300 g) → 300


# # =========================
# # CLEAN DATA
# # =========================

# df["calories_combined"] = df["calories_combined"].apply(extract_number)

# df["serving_value"] = df["serving"].apply(extract_serving)

# df = df.dropna(subset=["calories_combined", "serving_value"])

# if "food_category" not in df.columns:
#     df["food_category"] = "unknown"

# df["food_category"] = df["food_category"].fillna("unknown")

# print("\nRows after cleaning:", len(df))


# # =========================
# # FEATURE ENGINEERING
# # =========================

# # calories per gram
# df["cal_per_gram"] = df["calories_combined"] / df["serving_value"]


# # =========================
# # CREATE LABEL
# # =========================

# def calorie_level(c):

#     if c < 150:
#         return "Low"
#     elif c < 350:
#         return "Medium"
#     else:
#         return "High"


# df["calorie_level"] = df["calories_combined"].apply(calorie_level)

# print("\nClass Distribution (Before Balancing):")
# print(df["calorie_level"].value_counts())


# # =========================
# # BALANCE DATASET
# # =========================

# low = df[df.calorie_level == "Low"]
# medium = df[df.calorie_level == "Medium"]
# high = df[df.calorie_level == "High"]

# min_size = min(len(low), len(medium), len(high))

# low_bal = resample(low, replace=False, n_samples=min_size, random_state=42)
# medium_bal = resample(medium, replace=False, n_samples=min_size, random_state=42)
# high_bal = resample(high, replace=False, n_samples=min_size, random_state=42)

# df_balanced = pd.concat([low_bal, medium_bal, high_bal])

# print("\nClass Distribution (Balanced):")
# print(df_balanced["calorie_level"].value_counts())


# # =========================
# # FEATURES
# # =========================

# X = df_balanced[["serving_value", "cal_per_gram", "food_category"]].copy()
# y = df_balanced["calorie_level"]

# encoder = LabelEncoder()
# X["food_category"] = encoder.fit_transform(X["food_category"])


# # =========================
# # SPLIT DATA
# # =========================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )


# # =========================
# # MODEL
# # =========================

# model = RandomForestClassifier(
#     n_estimators=200,
#     max_depth=10,
#     random_state=42
# )

# model.fit(X_train, y_train)


# # =========================
# # EVALUATE
# # =========================

# y_pred = model.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred)

# print("\nAccuracy:", accuracy)

# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred))


# # =========================
# # SAVE MODEL
# # =========================

# joblib.dump(model, "models/food_calorie_model.pkl")
# joblib.dump(encoder, "models/food_category_encoder.pkl")

# import pickle

# # # save model
# # pickle.dump(model, open("models/ml_model.pkl", "wb"))

# # # save label encoder
# # pickle.dump(label_encoder, open("models/ml_label_encoder.pkl", "wb"))

# # # save feature columns
# # pickle.dump(feature_columns, open("models/feature_columns.pkl", "wb"))

# # # save metrics
# # pickle.dump({"Accuracy": accuracy}, open("models/ml_metrics.pkl", "wb"))
# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(y)

# # train model
# model.fit(X, y)

# # save model
# pickle.dump(model, open("models/ml_model.pkl", "wb"))

# # save encoder
# pickle.dump(label_encoder, open("models/ml_label_encoder.pkl", "wb"))

# import json

# metrics = {
#     "Accuracy": accuracy
# }

# with open("models/metrics.json", "w") as f:
#     json.dump(metrics, f)

# ml_metrics = {
#     "Accuracy": accuracy
# }

# feature_columns = X.columns.tolist()
# joblib.dump(feature_columns, "models/feature_columns.pkl")

# joblib.dump(ml_metrics, "models/ml_metrics.pkl")

# print("\n🔥 ML Model saved successfully!")

import pandas as pd
import joblib
import re
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample


# =========================
# CREATE MODELS FOLDER
# =========================

os.makedirs("models", exist_ok=True)


# =========================
# LOAD DATA
# =========================

df1 = pd.read_csv("data/calorie_infos.csv")
df2 = pd.read_csv("data/Food and Calories - Sheet1.csv")

print("Dataset1 size:", len(df1))
print("Dataset2 size:", len(df2))

df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()

df = pd.concat([df1, df2], ignore_index=True)

print("\nTotal dataset size:", len(df))
print("\nColumns:")
print(df.columns)


# =========================
# CREATE CALORIES COLUMN
# =========================

df["calories_combined"] = None

if "calories" in df.columns:
    df["calories_combined"] = df["calories"]

if "cal_per_serving" in df.columns:
    df["calories_combined"] = df["calories_combined"].fillna(df["cal_per_serving"])

if "cal_per_100_ml_or_gms" in df.columns:
    df["calories_combined"] = df["calories_combined"].fillna(df["cal_per_100_ml_or_gms"])

print("\nCalories column used: calories_combined")


# =========================
# EXTRACT NUMBER FUNCTION
# =========================

def extract_number(x):

    if pd.isna(x):
        return None

    numbers = re.findall(r"\d+\.?\d*", str(x))

    if len(numbers) == 0:
        return None

    return float(numbers[0])


def extract_serving(x):

    if pd.isna(x):
        return None

    numbers = re.findall(r"\d+\.?\d*", str(x))

    if len(numbers) == 0:
        return None

    return float(numbers[-1])


# =========================
# CLEAN DATA
# =========================

df["calories_combined"] = df["calories_combined"].apply(extract_number)

df["serving_value"] = df["serving"].apply(extract_serving)

df = df.dropna(subset=["calories_combined", "serving_value"])

if "food_category" not in df.columns:
    df["food_category"] = "unknown"

df["food_category"] = df["food_category"].fillna("unknown")

print("\nRows after cleaning:", len(df))


# =========================
# FEATURE ENGINEERING
# =========================

df["cal_per_gram"] = df["calories_combined"] / df["serving_value"]


# =========================
# CREATE LABEL
# =========================

def calorie_level(c):

    if c < 150:
        return "Low"
    elif c < 350:
        return "Medium"
    else:
        return "High"


df["calorie_level"] = df["calories_combined"].apply(calorie_level)

print("\nClass Distribution (Before Balancing):")
print(df["calorie_level"].value_counts())


# =========================
# BALANCE DATASET
# =========================

low = df[df.calorie_level == "Low"]
medium = df[df.calorie_level == "Medium"]
high = df[df.calorie_level == "High"]

min_size = min(len(low), len(medium), len(high))

low_bal = resample(low, replace=False, n_samples=min_size, random_state=42)
medium_bal = resample(medium, replace=False, n_samples=min_size, random_state=42)
high_bal = resample(high, replace=False, n_samples=min_size, random_state=42)

df_balanced = pd.concat([low_bal, medium_bal, high_bal])

print("\nClass Distribution (Balanced):")
print(df_balanced["calorie_level"].value_counts())


# =========================
# FEATURES
# =========================

X = df_balanced[["serving_value", "cal_per_gram", "food_category"]].copy()
y = df_balanced["calorie_level"]

encoder = LabelEncoder()
X["food_category"] = encoder.fit_transform(X["food_category"])


# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# =========================
# MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)


# =========================
# EVALUATE
# =========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# =========================
# SAVE FILES FOR STREAMLIT
# =========================

# model
joblib.dump(model, "models/ml_model.pkl")

# encoder
joblib.dump(encoder, "models/food_category_encoder.pkl")

# dataset
joblib.dump(df_balanced, "models/food_full_data.pkl")

# feature columns
feature_columns = X.columns.tolist()
joblib.dump(feature_columns, "models/feature_columns.pkl")

# metrics
ml_metrics = {
    "Accuracy": round(accuracy, 4)
}

joblib.dump(ml_metrics, "models/ml_metrics.pkl")

print("\n🔥 ML Model saved successfully!")