#=====================================================
# PHẦN 1: THỐNG KÊ MÔ TẢ
#=====================================================
import pandas as pd 
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
diabetes_data = pd.read_csv("e:/Download/diabetes.csv")
diabetes_data = diabetes_data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                                             'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']]
# Xem 5 dòng đầu tiên
print(diabetes_data.head())
# Thông tin tổng quát
print("\nThông tin dữ liệu:")
print(diabetes_data.info())
# Mô tả nhanh các thống kê cơ bản
print("\nThống kê mô tả tổng quát:")
print(diabetes_data.describe())

# Take a quick look at the data 
diabetes_data.head()
diabetes_data.dtypes
diabetes_data.shape
# Get the mean of the data 
data_mean = diabetes_data.mean()
# Get the median of the data 
data_median = diabetes_data.median() 
# Get the mode of the data 
data_mode = diabetes_data.mode().iloc[0]
# Obtain the variance of the data 
data_variance = diabetes_data.var() 
# Obtain the standard deviation of the data 
data_sd = diabetes_data.std() 
# Compute the maximum and minimum values of the data 
data_max = diabetes_data.max()  
data_min = diabetes_data.min() 
# Obtain the 60th percentile of the data 
data_percentile = diabetes_data.quantile(0.6)
# Obtain the quartiles of the data 
data_quartile = diabetes_data.quantile(0.75) 
# Get the IQR of the data 
data_IQR = data_quartile - diabetes_data.quantile(0.25)
results = pd.DataFrame({
    "Statistic": ["Mean", "Median", "Mode", "Variance", "Standard Deviation", 
                  "Max", "Min", "60th Percentile", "75th Quantile", "IQR"],
    "Value": [data_mean, data_median, data_mode, data_variance, data_sd,
              data_max, data_min, data_percentile, data_quartile, data_IQR]
})
df_results = pd.DataFrame(results)
df_results.to_csv(r"e:\Download\diabetes_summary.csv", index=False)