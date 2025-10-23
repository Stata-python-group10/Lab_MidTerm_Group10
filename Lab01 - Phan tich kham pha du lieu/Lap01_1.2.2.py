#=====================================================
# PHẦN 2: XỬ LÝ VÀ TRỰC QUAN HÓA DỮ LIỆU
#=====================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
winequality_red_data = pd.read_csv("e:/Download/winequality-red.csv")
winequality_red_data = winequality_red_data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 
                                             'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 
                                             'pH', 'sulphates', 'alcohol', 'quality']]
# Xem 5 dòng đầu tiên
print(winequality_red_data.head())
# Thông tin tổng quát
print("\nThông tin dữ liệu:")
print(winequality_red_data.info())
# Mô tả nhanh các thống kê cơ bản
print("\nThống kê mô tả tổng quát:")
print(winequality_red_data.describe())
# Histogram - Phân phối dữ liệu
winequality_red_data.hist(bins=15, figsize=(15,10), color='steelblue', edgecolor='black')
plt.suptitle("Phân phối các đặc trưng hóa học của rượu đỏ", fontsize=16)
plt.show()

# Boxplot - Phát hiện ngoại lệ
plt.figure(figsize=(15,8))
sns.boxplot(data=winequality_red_data, orient="h", palette="Set2")
plt.title("Boxplot các biến hóa học của rượu đỏ")
plt.show()

# Phân bố chất lượng rượu
plt.figure(figsize=(8,5))
sns.countplot(x='quality', data=winequality_red_data, palette='viridis')
plt.title("Phân bố chất lượng rượu đỏ")
plt.xlabel("Mức chất lượng (quality)")
plt.ylabel("Số lượng mẫu")
plt.show()

# Ma trận tương quan giữa các biến
plt.figure(figsize=(12,10))
corr = winequality_red_data.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Ma trận tương quan giữa các biến trong tập dữ liệu rượu đỏ")
plt.show()

# Xem các biến tương quan mạnh nhất với quality
corr_target = corr['quality'].sort_values(ascending=False)
print("\nTương quan giữa các biến với 'quality':")
print(corr_target)

# Scatter plot giữa alcohol và density, phân màu theo quality
plt.figure(figsize=(8,6))
sns.scatterplot(x='alcohol', y='density', hue='quality', data=winequality_red_data, palette='coolwarm')
plt.title("Mối quan hệ giữa Alcohol, Density và Quality")
plt.show()

# Boxplot giữa từng biến quan trọng và quality
features = ['volatile acidity', 'citric acid', 'residual sugar', 'alcohol']
plt.figure(figsize=(14,10))

for i, col in enumerate(features, 1):
    plt.subplot(2,2,i)
    sns.boxplot(x='quality', y=col, data=winequality_red_data, palette='Set3')
    plt.title(f"{col} vs Quality")

plt.tight_layout()
plt.show()