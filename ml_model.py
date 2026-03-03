# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
# from sklearn.neighbors import KNeighborsRegressor
# import joblib

# # โหลดข้อมูล
# df = pd.read_csv("data/Food and Calories - Sheet1.csv")

# print(df.columns)
# exit()
# # ทำความสะอาด
# df = df.dropna()
# df = df.drop_duplicates()

# # เลือก feature (แก้ชื่อคอลัมน์ให้ตรงของจริง)
# X = df[['Fat', 'Protein', 'Carbs', 'Sugar']]
# y = df['Calories']

# # แบ่งข้อมูล
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # สร้างโมเดล 3 ตัว
# rf = RandomForestRegressor()
# gb = GradientBoostingRegressor()
# knn = KNeighborsRegressor()

# # ทำ Ensemble
# ensemble = VotingRegressor([
#     ('rf', rf),
#     ('gb', gb),
#     ('knn', knn)
# ])

# # เทรน
# ensemble.fit(X_train, y_train)

# # บันทึกโมเดล
# joblib.dump(ensemble, "models/ensemble_model.pkl")

# print("ML Model saved successfully!")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor

# โหลดข้อมูล
df = pd.read_csv("data/Food and Calories - Sheet1.csv")


# แปลง Calories เป็นตัวเลข
df['Calories'] = df['Calories'].astype(str)  # บังคับเป็น string ก่อน
df['Calories'] = df['Calories'].str.replace('[^0-9.]', '', regex=True)  # ลบตัวอักษร
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')  # แปลงเป็นตัวเลข

# ลบค่าว่าง
df = df.dropna()

# สร้าง Class จาก Calories
def calorie_category(cal):
    if cal < 150:
        return "Low"
    elif cal < 300:
        return "Medium"
    else:
        return "High"

df['Calorie_Level'] = df['Calories'].apply(calorie_category)

# แปลง Food เป็นตัวเลข
le = LabelEncoder()
df['Food_encoded'] = le.fit_transform(df['Food'])

# Feature และ Target
X = df[['Food_encoded']]
y = df['Calories']

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# # สร้าง 3 โมเดล
# rf = RandomForestClassifier()
# gb = GradientBoostingClassifier()

# # Ensemble
# ensemble = VotingClassifier(
#     estimators=[
#         ('rf', rf),
#         ('gb', gb)
#     ],
#     voting='hard'
# )

# # เทรน
# ensemble.fit(X_train, y_train)

# # บันทึกโมเดล
# joblib.dump(ensemble, "models/ensemble_model.pkl")
# joblib.dump(le, "models/label_encoder.pkl")

# y_pred = ensemble.predict(X_test)
# acc = accuracy_score(y_test, y_pred)

# print("Model Accuracy:", acc)
rf = RandomForestRegressor()
gb = GradientBoostingRegressor()

ensemble = VotingRegressor(
    estimators=[
        ('rf', rf),
        ('gb', gb)
    ]
)

ensemble.fit(X_train, y_train)

joblib.dump(ensemble, "models/ensemble_model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

y_pred = ensemble.predict(X_test)

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)

print("MAE:", mae)

print("ML Classification Model saved successfully!")