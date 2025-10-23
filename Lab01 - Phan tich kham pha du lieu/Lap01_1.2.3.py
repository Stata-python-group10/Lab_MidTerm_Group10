#=====================================================
# PHẦN 2: XỬ LÝ VÀ TRỰC QUAN HÓA DỮ LIỆU
#=====================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
diabetes_data = pd.read_csv("e:/Download/diabetes.csv")
diabetes_data = diabetes_data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                                             'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']]
#=================================================================================================
# Xem 5 dòng đầu tiên
print(diabetes_data.head())
# Thông tin tổng quát
print("\nThông tin dữ liệu:")
print(diabetes_data.info())
# Mô tả nhanh các thống kê cơ bản
print("\nThống kê mô tả tổng quát:")
print(diabetes_data.describe())
#=================================================================================================
# Histogram cho từng biến
diabetes_data.hist(figsize=(12, 10), bins=20, color='skyblue', edgecolor='black')
plt.suptitle("Phân phối các biến trong bộ dữ liệu tiểu đường", fontsize=14)
plt.tight_layout()
plt.show()

# Boxplot: So sánh sự khác biệt giữa nhóm mắc bệnh và không mắc bệnh
plt.figure(figsize=(12, 6))
sns.boxplot(x='Outcome', y='Glucose', data=diabetes_data, palette='Set2')
plt.title("Phân phối nồng độ Glucose theo tình trạng bệnh", fontsize=14)
plt.show()

# Ma trận tương quan (Heatmap)
plt.figure(figsize=(10, 8))
corr = diabetes_data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Ma trận tương quan giữa các biến", fontsize=14)
plt.show()

# Scatter plot: Mối quan hệ giữa Glucose và BMI
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Glucose', y='BMI', hue='Outcome', data=diabetes_data, palette='Set1')
plt.title("Mối quan hệ giữa Glucose và BMI", fontsize=14)
plt.show()

# Histogram chồng giữa 2 nhóm bệnh / không bệnh
plt.figure(figsize=(10, 6))
sns.histplot(data=diabetes_data, x='Glucose', hue='Outcome', kde=True, bins=30, palette='Set1')
plt.title("Phân phối Glucose theo nhóm bệnh / không bệnh", fontsize=14)
plt.show()

# Pairplot tổng thể
sns.pairplot(diabetes_data, hue='Outcome', diag_kind='kde', palette='husl')
plt.suptitle("Biểu đồ Pairplot cho tập dữ liệu tiểu đường", y=1.02)
plt.show()