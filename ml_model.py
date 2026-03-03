# # # # # import pandas as pd
# # # # # from sklearn.model_selection import train_test_split
# # # # # from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
# # # # # from sklearn.neighbors import KNeighborsRegressor
# # # # # import joblib

# # # # # # โหลดข้อมูล
# # # # # df = pd.read_csv("data/Food and Calories - Sheet1.csv")

# # # # # print(df.columns)
# # # # # exit()
# # # # # # ทำความสะอาด
# # # # # df = df.dropna()
# # # # # df = df.drop_duplicates()

# # # # # # เลือก feature (แก้ชื่อคอลัมน์ให้ตรงของจริง)
# # # # # X = df[['Fat', 'Protein', 'Carbs', 'Sugar']]
# # # # # y = df['Calories']

# # # # # # แบ่งข้อมูล
# # # # # X_train, X_test, y_train, y_test = train_test_split(
# # # # #     X, y, test_size=0.2, random_state=42
# # # # # )

# # # # # # สร้างโมเดล 3 ตัว
# # # # # rf = RandomForestRegressor()
# # # # # gb = GradientBoostingRegressor()
# # # # # knn = KNeighborsRegressor()

# # # # # # ทำ Ensemble
# # # # # ensemble = VotingRegressor([
# # # # #     ('rf', rf),
# # # # #     ('gb', gb),
# # # # #     ('knn', knn)
# # # # # ])

# # # # # # เทรน
# # # # # ensemble.fit(X_train, y_train)

# # # # # # บันทึกโมเดล
# # # # # joblib.dump(ensemble, "models/ensemble_model.pkl")

# # # # # print("ML Model saved successfully!")
# # # # import pandas as pd
# # # # from sklearn.model_selection import train_test_split
# # # # from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
# # # # from sklearn.preprocessing import LabelEncoder
# # # # import joblib
# # # # from sklearn.metrics import accuracy_score
# # # # from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
# # # # from sklearn.metrics import mean_absolute_error, r2_score

# # # # # โหลดข้อมูล
# # # # df = pd.read_csv("data/Food and Calories - Sheet1.csv")


# # # # # แปลง Calories เป็นตัวเลข
# # # # df['Calories'] = df['Calories'].astype(str)  # บังคับเป็น string ก่อน
# # # # df['Calories'] = df['Calories'].str.replace('[^0-9.]', '', regex=True)  # ลบตัวอักษร
# # # # df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')  # แปลงเป็นตัวเลข

# # # # # ลบค่าว่าง
# # # # df = df.dropna()

# # # # # ดึงตัวเลขกรัมจาก Serving
# # # # df['Serving'] = df['Serving'].astype(str)

# # # # # df['Grams'] = df['Serving'].str.extract(r'(\d+)')
# # # # # df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')
# # # # df['Serving'] = df['Serving'].astype(str)

# # # # df['Grams'] = df['Serving'].str.extract(r'\(?(\d+)\s*g\)?', expand=False)

# # # # df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')

# # # # df = df.dropna(subset=['Grams'])

# # # # # สร้าง Class จาก Calories
# # # # def calorie_category(cal):
# # # #     if cal < 150:
# # # #         return "Low"
# # # #     elif cal < 300:
# # # #         return "Medium"
# # # #     else:
# # # #         return "High"

# # # # df['Calorie_Level'] = df['Calories'].apply(calorie_category)

# # # # # แปลง Food เป็นตัวเลข
# # # # le = LabelEncoder()
# # # # df['Food_encoded'] = le.fit_transform(df['Food'])

# # # # # # Feature และ Target
# # # # # X = df[['Food_encoded']]
# # # # # y = df['Calories']

# # # # # # แบ่งข้อมูล
# # # # # X_train, X_test, y_train, y_test = train_test_split(
# # # # #     X, y, test_size=0.2, random_state=42
# # # # # )

# # # # # # # สร้าง 3 โมเดล
# # # # # # rf = RandomForestClassifier()
# # # # # # gb = GradientBoostingClassifier()

# # # # # # # Ensemble
# # # # # # ensemble = VotingClassifier(
# # # # # #     estimators=[
# # # # # #         ('rf', rf),
# # # # # #         ('gb', gb)
# # # # # #     ],
# # # # # #     voting='hard'
# # # # # # )

# # # # # # # เทรน
# # # # # # ensemble.fit(X_train, y_train)

# # # # # # # บันทึกโมเดล
# # # # # # joblib.dump(ensemble, "models/ensemble_model.pkl")
# # # # # # joblib.dump(le, "models/label_encoder.pkl")

# # # # # # y_pred = ensemble.predict(X_test)
# # # # # # acc = accuracy_score(y_test, y_pred)

# # # # # # print("Model Accuracy:", acc)
# # # # # rf = RandomForestRegressor()
# # # # # gb = GradientBoostingRegressor()

# # # # # ensemble = VotingRegressor(
# # # # #     estimators=[
# # # # #         ('rf', rf),
# # # # #         ('gb', gb)
# # # # #     ]
# # # # # )

# # # # # ensemble.fit(X_train, y_train)

# # # # # joblib.dump(ensemble, "models/ensemble_model.pkl")
# # # # # joblib.dump(le, "models/label_encoder.pkl")

# # # # # y_pred = ensemble.predict(X_test)

# # # # # from sklearn.metrics import mean_absolute_error
# # # # # mae = mean_absolute_error(y_test, y_pred)

# # # # # print("MAE:", mae)
# # # # # joblib.dump(df, "models/food_full_data.pkl")
# # # # # print("ML Classification Model saved successfully!")

# # # # # y_pred = ensemble.predict(X_test)

# # # # # mae = mean_absolute_error(y_test, y_pred)
# # # # # r2 = r2_score(y_test, y_pred)

# # # # # print("MAE:", mae)
# # # # # print("R2 Score:", r2)

# # # # # # บันทึก metrics
# # # # # ml_metrics = {
# # # # #     "MAE": mae,
# # # # #     "R2": r2
# # # # # }

# # # # # joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# # # # # ----------------------------
# # # # # Feature Engineering
# # # # # ----------------------------

# # # # # df['Cal_per_gram'] = df['Calories'] / df['Grams']

# # # # # X = df[['Grams', 'Cal_per_gram']]
# # # # # y = df['Calories']

# # # # # # แบ่งข้อมูล
# # # # # X_train, X_test, y_train, y_test = train_test_split(
# # # # #     X, y, test_size=0.2, random_state=42
# # # # # )

# # # # # # โมเดล
# # # # # rf = RandomForestRegressor()
# # # # # gb = GradientBoostingRegressor()

# # # # # ensemble = VotingRegressor(
# # # # #     estimators=[
# # # # #         ('rf', rf),
# # # # #         ('gb', gb)
# # # # #     ]
# # # # # )

# # # # # ensemble.fit(X_train, y_train)

# # # # # # ประเมินผล
# # # # # y_pred = ensemble.predict(X_test)

# # # # # from sklearn.metrics import mean_absolute_error, r2_score

# # # # # mae = mean_absolute_error(y_test, y_pred)
# # # # # r2 = r2_score(y_test, y_pred)

# # # # # print("MAE:", mae)
# # # # # print("R2 Score:", r2)

# # # # # ml_metrics = {
# # # # #     "MAE": mae,
# # # # #     "R2": r2
# # # # # }

# # # # # joblib.dump(ensemble, "models/ensemble_model.pkl")
# # # # # joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# # # # # joblib.dump(df, "models/food_full_data.pkl")
# # # # # ----------------------------
# # # # # Feature Engineering (No Leakage)
# # # # # ----------------------------

# # # # X = df[['Grams']]
# # # # y = df['Calories']

# # # # X_train, X_test, y_train, y_test = train_test_split(
# # # #     X, y, test_size=0.2, random_state=42
# # # # )

# # # # rf = RandomForestRegressor()
# # # # gb = GradientBoostingRegressor()

# # # # ensemble = VotingRegressor(
# # # #     estimators=[
# # # #         ('rf', rf),
# # # #         ('gb', gb)
# # # #     ]
# # # # )

# # # # ensemble.fit(X_train, y_train)

# # # # y_pred = ensemble.predict(X_test)

# # # # mae = mean_absolute_error(y_test, y_pred)
# # # # r2 = r2_score(y_test, y_pred)

# # # # print("MAE:", mae)
# # # # print("R2 Score:", r2)

# # # # ml_metrics = {
# # # #     "MAE": mae,
# # # #     "R2": r2
# # # # }

# # # # joblib.dump(ensemble, "models/ensemble_model.pkl")
# # # # joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# # # # joblib.dump(df, "models/food_full_data.pkl")
# # # import pandas as pd
# # # import joblib
# # # from sklearn.model_selection import train_test_split
# # # from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
# # # from sklearn.metrics import mean_absolute_error, r2_score

# # # # ----------------------------
# # # # โหลดข้อมูล
# # # # ----------------------------
# # # df = pd.read_csv("data/Food and Calories - Sheet1.csv")

# # # # ----------------------------
# # # # ทำความสะอาด Calories
# # # # ----------------------------
# # # df['Calories'] = df['Calories'].astype(str)
# # # df['Calories'] = df['Calories'].str.replace('[^0-9.]', '', regex=True)
# # # df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

# # # df = df.dropna()

# # # # ----------------------------
# # # # ดึงค่า Grams จาก Serving
# # # # ----------------------------
# # # df['Serving'] = df['Serving'].astype(str)
# # # df['Grams'] = df['Serving'].str.extract(r'\(?(\d+)\s*g\)?', expand=False)
# # # df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')

# # # df = df.dropna(subset=['Grams'])

# # # # ----------------------------
# # # # สร้าง Category (ไม่ใช้ Calories สร้าง feature)
# # # # ----------------------------
# # # def categorize_food(name):
# # #     name = name.lower()

# # #     if any(word in name for word in ["burger", "whopper", "sandwich"]):
# # #         return "FastFood"
# # #     elif any(word in name for word in ["apple", "banana", "orange", "fruit"]):
# # #         return "Fruit"
# # #     elif any(word in name for word in ["chicken", "beef", "pork", "meat"]):
# # #         return "Meat"
# # #     elif any(word in name for word in ["rice", "pasta", "noodle", "bread"]):
# # #         return "Carb"
# # #     else:
# # #         return "Other"

# # # df['Category'] = df['Food'].apply(categorize_food)

# # # # One-hot encoding
# # # df = pd.get_dummies(df, columns=['Category'])

# # # # ----------------------------
# # # # Feature และ Target
# # # # ----------------------------
# # # feature_cols = ['Grams'] + [col for col in df.columns if col.startswith('Category_')]

# # # X = df[feature_cols]
# # # y = df['Calories']

# # # # ----------------------------
# # # # แบ่ง Train/Test
# # # # ----------------------------
# # # X_train, X_test, y_train, y_test = train_test_split(
# # #     X, y, test_size=0.2, random_state=42
# # # )

# # # # ----------------------------
# # # # โมเดล (ปรับ Hyperparameter ให้แม่นขึ้น)
# # # # ----------------------------
# # # rf = RandomForestRegressor(
# # #     n_estimators=300,
# # #     max_depth=None,
# # #     random_state=42
# # # )

# # # gb = GradientBoostingRegressor(
# # #     n_estimators=300,
# # #     learning_rate=0.05,
# # #     random_state=42
# # # )

# # # ensemble = VotingRegressor(
# # #     estimators=[
# # #         ('rf', rf),
# # #         ('gb', gb)
# # #     ]
# # # )

# # # # ----------------------------
# # # # Train
# # # # ----------------------------
# # # ensemble.fit(X_train, y_train)

# # # # ----------------------------
# # # # ประเมินผล
# # # # ----------------------------
# # # y_pred = ensemble.predict(X_test)

# # # mae = mean_absolute_error(y_test, y_pred)
# # # r2 = r2_score(y_test, y_pred)

# # # print("MAE:", mae)
# # # print("R2 Score:", r2)

# # # # ----------------------------
# # # # บันทึกโมเดลและ metrics
# # # # ----------------------------
# # # ml_metrics = {
# # #     "MAE": mae,
# # #     "R2": r2
# # # }

# # # joblib.dump(ensemble, "models/ensemble_model.pkl")
# # # joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# # # joblib.dump(df, "models/food_full_data.pkl")

# # # print("Model saved successfully!")
# # import pandas as pd
# # import joblib
# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
# # from sklearn.metrics import mean_absolute_error, r2_score

# # # ----------------------------
# # # โหลดข้อมูล
# # # ----------------------------
# # df = pd.read_csv("data/Food and Calories - Sheet1.csv")

# # # ----------------------------
# # # ทำความสะอาด Calories
# # # ----------------------------
# # df['Calories'] = df['Calories'].astype(str)
# # df['Calories'] = df['Calories'].str.replace('[^0-9.]', '', regex=True)
# # df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

# # df = df.dropna()

# # # ----------------------------
# # # ดึงค่า Grams จาก Serving
# # # ----------------------------
# # df['Serving'] = df['Serving'].astype(str)
# # df['Grams'] = df['Serving'].str.extract(r'\(?(\d+)\s*g\)?', expand=False)
# # df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')

# # df = df.dropna(subset=['Grams'])

# # # ----------------------------
# # # 🎯 เปลี่ยน Target เป็น Calories per 100g
# # # ----------------------------
# # df['Cal_per_100g'] = (df['Calories'] / df['Grams']) * 100

# # # ----------------------------
# # # สร้าง Category (ไม่ใช้ target สร้าง feature)
# # # ----------------------------
# # def categorize_food(name):
# #     name = name.lower()

# #     if any(word in name for word in ["burger", "whopper", "sandwich"]):
# #         return "FastFood"
# #     elif any(word in name for word in ["apple", "banana", "orange", "fruit"]):
# #         return "Fruit"
# #     elif any(word in name for word in ["chicken", "beef", "pork", "meat"]):
# #         return "Meat"
# #     elif any(word in name for word in ["rice", "pasta", "noodle", "bread"]):
# #         return "Carb"
# #     else:
# #         return "Other"

# # df['Category'] = df['Food'].apply(categorize_food)

# # # One-hot encoding
# # df = pd.get_dummies(df, columns=['Category'])

# # # ----------------------------
# # # Feature และ Target
# # # ----------------------------
# # feature_cols = ['Grams'] + [col for col in df.columns if col.startswith('Category_')]

# # X = df[feature_cols]
# # y = df['Cal_per_100g']

# # # ----------------------------
# # # แบ่ง Train/Test
# # # ----------------------------
# # X_train, X_test, y_train, y_test = train_test_split(
# #     X, y, test_size=0.2, random_state=42
# # )

# # # ----------------------------
# # # โมเดล (ปรับให้แม่นขึ้น)
# # # ----------------------------
# # rf = RandomForestRegressor(
# #     n_estimators=300,
# #     max_depth=None,
# #     random_state=42
# # )

# # gb = GradientBoostingRegressor(
# #     n_estimators=300,
# #     learning_rate=0.05,
# #     random_state=42
# # )

# # ensemble = VotingRegressor(
# #     estimators=[
# #         ('rf', rf),
# #         ('gb', gb)
# #     ]
# # )

# # # ----------------------------
# # # Train
# # # ----------------------------
# # ensemble.fit(X_train, y_train)

# # # ----------------------------
# # # ประเมินผล
# # # ----------------------------
# # y_pred = ensemble.predict(X_test)

# # mae = mean_absolute_error(y_test, y_pred)
# # r2 = r2_score(y_test, y_pred)

# # print("MAE (Cal per 100g):", mae)
# # print("R2 Score:", r2)

# # # ----------------------------
# # # บันทึกโมเดลและ metrics
# # # ----------------------------
# # ml_metrics = {
# #     "MAE_Cal_per_100g": mae,
# #     "R2": r2
# # }

# # joblib.dump(ensemble, "models/ensemble_model.pkl")
# # joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# # joblib.dump(df, "models/food_full_data.pkl")

# # print("Model saved successfully!")
# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
# from sklearn.metrics import mean_absolute_error, r2_score

# # ----------------------------
# # โหลดข้อมูล
# # ----------------------------
# df = pd.read_csv("data/Food and Calories - Sheet1.csv")

# # ----------------------------
# # ทำความสะอาด Calories
# # ----------------------------
# df['Calories'] = df['Calories'].astype(str)
# df['Calories'] = df['Calories'].str.replace('[^0-9.]', '', regex=True)
# df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

# df = df.dropna()

# # ----------------------------
# # ดึงค่า Grams จาก Serving
# # ----------------------------
# df['Serving'] = df['Serving'].astype(str)
# df['Grams'] = df['Serving'].str.extract(r'(\d+\.?\d*)\s*g', expand=False)
# df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')

# df = df.dropna(subset=['Grams'])

# # ----------------------------
# # 🎯 สร้าง Target: Calories per 100g
# # ----------------------------
# df['Cal_per_100g'] = (df['Calories'] / df['Grams']) * 100

# # ----------------------------
# # 🎯 One-Hot Encoding Food
# # ----------------------------
# df_encoded = pd.get_dummies(df, columns=['Food'])

# # ----------------------------
# # Feature และ Target
# # ----------------------------
# X = df_encoded.drop(columns=['Calories', 'Cal_per_100g', 'Serving'])
# y = df_encoded['Cal_per_100g']

# # ----------------------------
# # แบ่ง Train/Test
# # ----------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # ----------------------------
# # โมเดล (ปรับ Hyperparameter)
# # ----------------------------
# rf = RandomForestRegressor(
#     n_estimators=400,
#     max_depth=None,
#     random_state=42
# )

# gb = GradientBoostingRegressor(
#     n_estimators=400,
#     learning_rate=0.05,
#     random_state=42
# )

# ensemble = VotingRegressor(
#     estimators=[
#         ('rf', rf),
#         ('gb', gb)
#     ]
# )

# # ----------------------------
# # Train
# # ----------------------------
# ensemble.fit(X_train, y_train)

# # ----------------------------
# # ประเมินผล
# # ----------------------------
# y_pred = ensemble.predict(X_test)

# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print("MAE (Cal per 100g):", mae)
# print("R2 Score:", r2)

# # ----------------------------
# # บันทึกโมเดลและข้อมูลที่จำเป็น
# # ----------------------------
# ml_metrics = {
#     "MAE_Cal_per_100g": mae,
#     "R2": r2
# }

# joblib.dump(ensemble, "models/ensemble_model.pkl")
# joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")
# joblib.dump(df, "models/food_full_data.pkl")

# print("Model saved successfully!")
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report

# ----------------------------
# โหลดข้อมูล
# ----------------------------
df = pd.read_csv("data/Food and Calories - Sheet1.csv")

# ----------------------------
# ทำความสะอาด Calories
# ----------------------------
df['Calories'] = df['Calories'].astype(str)
df['Calories'] = df['Calories'].str.replace('[^0-9.]', '', regex=True)
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

df = df.dropna()

# ----------------------------
# ดึง Grams จาก Serving
# ----------------------------
df['Serving'] = df['Serving'].astype(str)
df['Grams'] = df['Serving'].str.extract(r'(\d+\.?\d*)\s*g', expand=False)
df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')

df = df.dropna(subset=['Grams'])

# ----------------------------
# 🎯 สร้าง Calorie_Level
# ----------------------------
def calorie_category(cal):
    if cal < 150:
        return "Low"
    elif cal < 300:
        return "Medium"
    else:
        return "High"

df['Calorie_Level'] = df['Calories'].apply(calorie_category)

# ----------------------------
# 🎯 One-Hot Encoding Food
# ----------------------------
df_encoded = pd.get_dummies(df, columns=['Food'])

# ----------------------------
# Feature และ Target
# ----------------------------
X = df_encoded.drop(columns=['Calories', 'Calorie_Level', 'Serving'])
y = df_encoded['Calorie_Level']

# ----------------------------
# Train/Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# โมเดล Ensemble
# ----------------------------
rf = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

gb = GradientBoostingClassifier(
    n_estimators=300,
    learning_rate=0.05,
    random_state=42
)

ensemble = VotingClassifier(
    estimators=[
        ('rf', rf),
        ('gb', gb)
    ],
    voting='soft'
)

# ----------------------------
# Train
# ----------------------------
ensemble.fit(X_train, y_train)

# ----------------------------
# Evaluate
# ----------------------------
y_pred = ensemble.predict(X_test)

acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ----------------------------
# Save Model
# ----------------------------
ml_metrics = {
    "Accuracy": acc
}

joblib.dump(ensemble, "models/ensemble_model.pkl")
joblib.dump(ml_metrics, "models/ml_metrics.pkl")
joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")
joblib.dump(df, "models/food_full_data.pkl")

print("Classification Model saved successfully!")