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

# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
# from sklearn.metrics import accuracy_score, classification_report

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
# # ดึง Grams จาก Serving
# # ----------------------------
# df['Serving'] = df['Serving'].astype(str)
# df['Grams'] = df['Serving'].str.extract(r'(\d+\.?\d*)\s*g', expand=False)
# df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')

# df = df.dropna(subset=['Grams'])

# # ----------------------------
# # 🎯 สร้าง Calorie_Level
# # ----------------------------
# def calorie_category(cal):
#     if cal < 150:
#         return "Low"
#     elif cal < 300:
#         return "Medium"
#     else:
#         return "High"

# df['Calorie_Level'] = df['Calories'].apply(calorie_category)

# # ----------------------------
# # 🎯 One-Hot Encoding Food
# # ----------------------------
# df_encoded = pd.get_dummies(df, columns=['Food'])

# # ----------------------------
# # Feature และ Target
# # ----------------------------
# X = df_encoded.drop(columns=['Calories', 'Calorie_Level', 'Serving'])
# y = df_encoded['Calorie_Level']

# # ----------------------------
# # Train/Test Split
# # ----------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # ----------------------------
# # โมเดล Ensemble
# # ----------------------------
# rf = RandomForestClassifier(
#     n_estimators=300,
#     random_state=42
# )

# gb = GradientBoostingClassifier(
#     n_estimators=300,
#     learning_rate=0.05,
#     random_state=42
# )

# ensemble = VotingClassifier(
#     estimators=[
#         ('rf', rf),
#         ('gb', gb)
#     ],
#     voting='soft'
# )

# # ----------------------------
# # Train
# # ----------------------------
# ensemble.fit(X_train, y_train)

# # ----------------------------
# # Evaluate
# # ----------------------------
# y_pred = ensemble.predict(X_test)

# acc = accuracy_score(y_test, y_pred)

# print("Accuracy:", acc)
# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred))

# # ----------------------------
# # Save Model
# # ----------------------------
# ml_metrics = {
#     "Accuracy": acc
# }

# joblib.dump(ensemble, "models/ensemble_model.pkl")
# joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")
# joblib.dump(df, "models/food_full_data.pkl")

# print("Classification Model saved successfully!")

# import pandas as pd
# import joblib
# import os

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, VotingClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from xgboost import XGBClassifier

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
# # ดึง Grams จาก Serving
# # ----------------------------
# df['Serving'] = df['Serving'].astype(str)
# df['Grams'] = df['Serving'].str.extract(r'(\d+\.?\d*)\s*g', expand=False)
# df['Grams'] = pd.to_numeric(df['Grams'], errors='coerce')

# df = df.dropna(subset=['Grams'])

# # ----------------------------
# # เพิ่ม Feature สำคัญ
# # ----------------------------
# df['Cal_per_gram'] = df['Calories'] / df['Grams']

# # ----------------------------
# # สร้าง Calorie_Level
# # ----------------------------
# def calorie_category(cal):
#     if cal < 150:
#         return "Low"
#     elif cal < 300:
#         return "Medium"
#     else:
#         return "High"

# df['Calorie_Level'] = df['Calories'].apply(calorie_category)

# # ----------------------------
# # ตรวจสอบ class balance
# # ----------------------------
# print("Class Distribution:")
# print(df['Calorie_Level'].value_counts())

# # ----------------------------
# # One-Hot Encoding
# # ----------------------------
# df_encoded = pd.get_dummies(df, columns=['Food'])

# # ----------------------------
# # Feature และ Target
# # ----------------------------
# X = df_encoded.drop(columns=['Calories', 'Calorie_Level', 'Serving'])
# y = df_encoded['Calorie_Level']

# # ----------------------------
# # Train/Test Split (สำคัญมาก)
# # ----------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )

# # ----------------------------
# # โมเดล 1: Random Forest
# # ----------------------------
# rf = RandomForestClassifier(
#     n_estimators=500,
#     max_depth=None,
#     min_samples_split=2,
#     random_state=42
# )

# # ----------------------------
# # โมเดล 2: XGBoost
# # ----------------------------
# xgb = XGBClassifier(
#     n_estimators=300,
#     learning_rate=0.1,
#     max_depth=4,
#     use_label_encoder=False,
#     eval_metric='mlogloss'
# )

# # ----------------------------
# # Ensemble Voting
# # ----------------------------
# ensemble = VotingClassifier(
#     estimators=[
#         ('rf', rf),
#         ('xgb', xgb)
#     ],
#     voting='soft'
# )

# # ----------------------------
# # Train
# # ----------------------------
# ensemble.fit(X_train, y_train)

# # ----------------------------
# # Evaluate
# # ----------------------------
# y_pred = ensemble.predict(X_test)

# acc = accuracy_score(y_test, y_pred)

# print("\nAccuracy:", acc)
# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred))

# # ----------------------------
# # Save Model
# # ----------------------------
# os.makedirs("models", exist_ok=True)

# ml_metrics = {
#     "Accuracy": float(acc)
# }

# joblib.dump(ensemble, "models/ensemble_model.pkl")
# joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")
# joblib.dump(df, "models/food_full_data.pkl")

# print("\n🔥 Classification Model saved successfully!")

# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from xgboost import XGBClassifier

# # ----------------------------
# # Dataset 1 (ของเดิม)
# # ----------------------------
# df1 = pd.read_csv("data/Food and Calories - Sheet1.csv")

# # clean calories
# df1['Calories'] = df1['Calories'].astype(str)
# df1['Calories'] = df1['Calories'].str.replace('[^0-9.]', '', regex=True)
# df1['Calories'] = pd.to_numeric(df1['Calories'], errors='coerce')

# df1 = df1.dropna()

# # extract grams
# df1['Serving'] = df1['Serving'].astype(str)
# df1['Grams'] = df1['Serving'].str.extract(r'(\d+\.?\d*)\s*g', expand=False)
# df1['Grams'] = pd.to_numeric(df1['Grams'], errors='coerce')

# df1 = df1.dropna(subset=['Grams'])

# df1 = df1[['Food','Calories','Grams']]

# # ----------------------------
# # Dataset 2 (calorie_infos)
# # ----------------------------
# df2 = pd.read_csv("data/calorie_infos.csv")

# df2['Calories'] = df2['cal_per_100_ml_or_gms'].str.replace(' cal','')
# df2['Calories'] = pd.to_numeric(df2['Calories'], errors='coerce')

# df2['Food'] = df2['food_name']
# df2['Grams'] = 100   # เพราะเป็น per 100g

# df2 = df2[['Food','Calories','Grams']]
# df2 = df2.dropna()

# # ----------------------------
# # รวม dataset
# # ----------------------------
# df = pd.concat([df1, df2], ignore_index=True)

# print("Total dataset size:", len(df))

# # ----------------------------
# # สร้าง Calorie Level
# # ----------------------------
# def calorie_category(cal):

#     if cal < 150:
#         return "Low"

#     elif cal < 300:
#         return "Medium"

#     else:
#         return "High"

# df['Calorie_Level'] = df['Calories'].apply(calorie_category)

# print("\nClass Distribution:")
# print(df['Calorie_Level'].value_counts())

# # ----------------------------
# # One Hot Encoding
# # ----------------------------
# df_encoded = pd.get_dummies(df, columns=['Food'])

# X = df_encoded.drop(columns=['Calories','Calorie_Level'])
# y = df_encoded['Calorie_Level']

# # ----------------------------
# # Train Test Split
# # ----------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )

# # ----------------------------
# # Models
# # ----------------------------
# rf = RandomForestClassifier(
#     n_estimators=400,
#     random_state=42
# )

# gb = GradientBoostingClassifier(
#     n_estimators=300,
#     learning_rate=0.05,
#     random_state=42
# )

# xgb = XGBClassifier(
#     n_estimators=400,
#     max_depth=6,
#     learning_rate=0.05,
#     eval_metric='mlogloss'
# )

# ensemble = VotingClassifier(
#     estimators=[
#         ('rf', rf),
#         ('gb', gb),
#         ('xgb', xgb)
#     ],
#     voting='soft'
# )

# # ----------------------------
# # Train
# # ----------------------------
# ensemble.fit(X_train, y_train)

# # ----------------------------
# # Evaluate
# # ----------------------------
# y_pred = ensemble.predict(X_test)

# acc = accuracy_score(y_test, y_pred)

# print("\nAccuracy:", acc)
# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred))

# # ----------------------------
# # Save Model
# # ----------------------------
# ml_metrics = {
#     "Accuracy": acc
# }

# joblib.dump(ensemble, "models/ensemble_model.pkl")
# joblib.dump(ml_metrics, "models/ml_metrics.pkl")
# joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")
# joblib.dump(df, "models/food_full_data.pkl")

# print("\n🔥 Combined Dataset Model saved successfully!")

# import pandas as pd
# import numpy as np

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
# from sklearn.impute import SimpleImputer

# import joblib


# # ==============================
# # LOAD DATASET
# # ==============================

# df1 = pd.read_csv("data/Food and Calories - Sheet1.csv")
# df2 = pd.read_csv("data/calorie_infos.csv")

# df = pd.concat([df1, df2], ignore_index=True)

# print("Total dataset size:", len(df))


# # ==============================
# # CLEAN DATA
# # ==============================

# # ลบคอลัมน์ที่ไม่ใช้
# drop_cols = ['Food_Name','Food','food','name']
# for col in drop_cols:
#     if col in df.columns:
#         df = df.drop(columns=[col])

# # แปลงเป็นตัวเลข
# df = df.apply(pd.to_numeric, errors='coerce')

# # ลบค่า NaN
# df = df.dropna()

# # ==============================
# # CREATE CALORIE LEVEL
# # ==============================

# def calorie_level(c):
#     if c < 200:
#         return "Low"
#     elif c < 400:
#         return "Medium"
#     else:
#         return "High"

# df["Calorie_Level"] = df["Calories"].apply(calorie_level)

# print("\nClass Distribution:")
# print(df["Calorie_Level"].value_counts())


# # ==============================
# # FEATURES / LABEL
# # ==============================

# X = df[['Calories','Protein','Carbs','Fat']]
# y = df['Calorie_Level']


# # ==============================
# # ENCODE LABEL
# # ==============================

# le = LabelEncoder()
# y = le.fit_transform(y)


# # ==============================
# # TRAIN TEST SPLIT
# # ==============================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )


# # ==============================
# # HANDLE MISSING VALUES
# # ==============================

# imputer = SimpleImputer(strategy="mean")

# X_train = imputer.fit_transform(X_train)
# X_test = imputer.transform(X_test)


# # ==============================
# # MODELS
# # ==============================

# rf = RandomForestClassifier(
#     n_estimators=200,
#     random_state=42
# )

# gb = GradientBoostingClassifier()


# # ==============================
# # ENSEMBLE MODEL
# # ==============================

# ensemble = VotingClassifier(
#     estimators=[
#         ('rf', rf),
#         ('gb', gb)
#     ],
#     voting='soft'
# )


# # ==============================
# # TRAIN MODEL
# # ==============================

# ensemble.fit(X_train, y_train)


# # ==============================
# # EVALUATE
# # ==============================

# y_pred = ensemble.predict(X_test)

# print("\nAccuracy:", accuracy_score(y_test, y_pred))

# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred, target_names=le.classes_))


# # ==============================
# # SAVE MODEL
# # ==============================

# joblib.dump(ensemble, "food_calorie_model.pkl")
# joblib.dump(le, "label_encoder.pkl")

# print("\n🔥 Combined Dataset Model saved successfully!")


# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.ensemble import RandomForestClassifier
# import joblib


# # ==============================
# # LOAD DATASET
# # ==============================

# df1 = pd.read_csv("data/Food and Calories - Sheet1.csv")
# df2 = pd.read_csv("data/calorie_infos.csv")

# df = pd.concat([df1, df2], ignore_index=True)

# print("Total dataset size:", len(df))


# # ==============================
# # CLEAN COLUMN NAMES
# # ==============================

# df.columns = df.columns.str.lower().str.strip()

# print("\nColumns in dataset:")
# print(df.columns)


# # ==============================
# # FIND CALORIES COLUMN
# # ==============================

# cal_col = None

# for col in df.columns:
#     if "cal" in col:
#         cal_col = col
#         break

# if cal_col is None:
#     raise Exception("Calories column not found in dataset")

# print("\nCalories column used:", cal_col)


# # ==============================
# # CLEAN CALORIES DATA
# # ==============================

# df[cal_col] = df[cal_col].astype(str)

# # ลบตัวอักษร เช่น kcal
# df[cal_col] = df[cal_col].str.replace(r'[^0-9.]', '', regex=True)

# df[cal_col] = pd.to_numeric(df[cal_col], errors='coerce')

# df = df.dropna(subset=[cal_col])

# print("\nRows after cleaning:", len(df))


# # ==============================
# # CREATE CALORIE LEVEL
# # ==============================

# def calorie_level(c):

#     if c < 200:
#         return "Low"
#     elif c < 400:
#         return "Medium"
#     else:
#         return "High"


# df["Calorie_Level"] = df[cal_col].apply(calorie_level)

# print("\nClass Distribution:")
# print(df["Calorie_Level"].value_counts())


# # ==============================
# # FEATURES / LABEL
# # ==============================

# X = df[[cal_col]]

# y = df["Calorie_Level"]


# # ==============================
# # ENCODE LABEL
# # ==============================

# le = LabelEncoder()

# y = le.fit_transform(y)


# # ==============================
# # TRAIN TEST SPLIT
# # ==============================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )


# # ==============================
# # MODEL
# # ==============================

# model = RandomForestClassifier(
#     n_estimators=200,
#     random_state=42
# )


# # ==============================
# # TRAIN
# # ==============================

# model.fit(X_train, y_train)


# # ==============================
# # EVALUATE
# # ==============================

# y_pred = model.predict(X_test)

# acc = accuracy_score(y_test, y_pred)

# print("\nAccuracy:", acc)

# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred, target_names=le.classes_))


# # ==============================
# # SAVE MODEL
# # ==============================

# joblib.dump(model, "models/ml_model.pkl")
# joblib.dump(le, "models/ml_label_encoder.pkl")

# print("\n🔥 ML Model saved successfully!")

# import pandas as pd
# import numpy as np
# import joblib

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier

# # =========================
# # LOAD DATA
# # =========================

# df1 = pd.read_csv("data/Food and Calories - Sheet1.csv")
# df2 = pd.read_csv("data/calorie_infos.csv")

# df = pd.concat([df1, df2], ignore_index=True)

# print("Total dataset size:", len(df))

# # =========================
# # CLEAN COLUMN NAME
# # =========================

# df.columns = df.columns.str.lower()

# print("\nColumns in dataset:")
# print(df.columns)

# # =========================
# # FIND CALORIES COLUMN
# # =========================

# calorie_col = None

# for col in df.columns:
#     if "calorie" in col:
#         calorie_col = col
#         break

# print("\nCalories column used:", calorie_col)

# # =========================
# # EXTRACT NUMBER FROM STRING
# # =========================

# df[calorie_col] = df[calorie_col].astype(str)

# df[calorie_col] = df[calorie_col].str.extract(r'(\d+\.?\d*)')

# df[calorie_col] = pd.to_numeric(df[calorie_col], errors='coerce')

# # ลบ NaN
# df = df.dropna(subset=[calorie_col])

# print("\nRows after cleaning:", len(df))

# # =========================
# # CREATE CALORIE LEVEL
# # =========================

# def calorie_level(c):
#     if c < 200:
#         return "Low"
#     elif c < 400:
#         return "Medium"
#     else:
#         return "High"

# df["calorie_level"] = df[calorie_col].apply(calorie_level)

# print("\nClass Distribution:")
# print(df["calorie_level"].value_counts())

# # =========================
# # FEATURES
# # =========================

# X = df[[calorie_col]]
# y = df["calorie_level"]

# # =========================
# # ENCODE LABEL
# # =========================

# le = LabelEncoder()
# y = le.fit_transform(y)

# # =========================
# # TRAIN TEST SPLIT
# # =========================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )

# # =========================
# # MODELS
# # =========================

# rf = RandomForestClassifier(
#     n_estimators=200,
#     random_state=42
# )

# gb = GradientBoostingClassifier()

# ensemble = VotingClassifier(
#     estimators=[
#         ("rf", rf),
#         ("gb", gb)
#     ],
#     voting="soft"
# )

# # =========================
# # TRAIN
# # =========================

# ensemble.fit(X_train, y_train)

# # =========================
# # EVALUATE
# # =========================

# y_pred = ensemble.predict(X_test)

# acc = accuracy_score(y_test, y_pred)

# print("\nAccuracy:", acc)

# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred, target_names=le.classes_))

# # =========================
# # SAVE MODEL
# # =========================

# joblib.dump(ensemble, "models/ensemble_model.pkl")
# joblib.dump(le, "models/label_encoder.pkl")
# joblib.dump([calorie_col], "models/feature_columns.pkl")

# print("\n🔥 ML Model saved successfully!")

# import pandas as pd
# import joblib
# import re

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report

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
# # EXTRACT NUMBER FROM STRING
# # =========================

# def extract_number(x):

#     if pd.isna(x):
#         return None

#     numbers = re.findall(r"\d+\.?\d*", str(x))

#     if len(numbers) == 0:
#         return None

#     return float(numbers[0])


# df["calories_combined"] = df["calories_combined"].apply(extract_number)

# # =========================
# # CLEAN DATA
# # =========================

# df = df.dropna(subset=["calories_combined"])

# if "food_category" not in df.columns:
#     df["food_category"] = "unknown"

# df["food_category"] = df["food_category"].fillna("unknown")

# print("\nRows after cleaning:", len(df))

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

# print("\nClass Distribution:")
# print(df["calorie_level"].value_counts())

# # =========================
# # FEATURE
# # =========================

# X = df[["calories_combined","food_category"]]
# y = df["calorie_level"]

# encoder = LabelEncoder()

# X["food_category"] = encoder.fit_transform(X["food_category"])

# # =========================
# # SPLIT
# # =========================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# # =========================
# # MODEL
# # =========================

# model = RandomForestClassifier(
#     n_estimators=150,
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

# joblib.dump(model, "food_calorie_model.pkl")
# joblib.dump(encoder, "food_category_encoder.pkl")

# print("\n🔥 ML Model saved successfully!")

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

# # import pickle

# # # save model
# # pickle.dump(model, open("models/ml_model.pkl", "wb"))

# # # save label encoder
# # pickle.dump(label_encoder, open("models/ml_label_encoder.pkl", "wb"))

# # # save feature columns
# # pickle.dump(feature_columns, open("models/feature_columns.pkl", "wb"))

# # # save metrics
# # pickle.dump({"Accuracy": accuracy}, open("models/ml_metrics.pkl", "wb"))


# print("\n🔥 ML Model saved successfully!")

import pandas as pd
import joblib
import re

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample


# =========================
# LOAD DATA
# =========================

df1 = pd.read_csv("data/calorie_infos.csv")
df2 = pd.read_csv("data/Food and Calories - Sheet1.csv")

print("Dataset1 size:", len(df1))
print("Dataset2 size:", len(df2))

# lowercase columns
df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()

df = pd.concat([df1, df2], ignore_index=True)

print("\nTotal dataset size:", len(df))
print("\nColumns in dataset:")
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

    return float(numbers[-1])  # เช่น (300 g) → 300


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

# calories per gram
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
# SPLIT DATA
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
# SAVE MODEL
# =========================

joblib.dump(model, "models/food_calorie_model.pkl")
joblib.dump(encoder, "models/food_category_encoder.pkl")

import pickle

# # save model
# pickle.dump(model, open("models/ml_model.pkl", "wb"))

# # save label encoder
# pickle.dump(label_encoder, open("models/ml_label_encoder.pkl", "wb"))

# # save feature columns
# pickle.dump(feature_columns, open("models/feature_columns.pkl", "wb"))

# # save metrics
# pickle.dump({"Accuracy": accuracy}, open("models/ml_metrics.pkl", "wb"))
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# train model
model.fit(X, y)

# save model
pickle.dump(model, open("models/ml_model.pkl", "wb"))

# save encoder
pickle.dump(label_encoder, open("models/ml_label_encoder.pkl", "wb"))

import json

metrics = {
    "Accuracy": accuracy
}

with open("models/metrics.json", "w") as f:
    json.dump(metrics, f)

ml_metrics = {
    "Accuracy": accuracy
}

joblib.dump(ml_metrics, "models/ml_metrics.pkl")

print("\n🔥 ML Model saved successfully!")