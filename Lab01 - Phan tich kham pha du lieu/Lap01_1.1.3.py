#=====================================================
# PHẦN 1: THỐNG KÊ MÔ TẢ
#=====================================================
import pandas as pd 
import numpy as np
from scipy import stats
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

# Take a quick look at the data 
winequality_red_data.head()
winequality_red_data.dtypes
winequality_red_data.shape
# Get the mean of the data 
data_mean = np.mean(winequality_red_data["quality"])
# Get the median of the data 
data_median = np.median(winequality_red_data["quality"]) 
# Get the mode of the data 
data_mode = stats.mode(winequality_red_data["quality"], keepdims=True)
mode_value = data_mode.mode if np.isscalar(data_mode.mode) else data_mode.mode[0]
# Obtain the variance of the data 
data_variance = np.var(winequality_red_data["quality"]) 
# Obtain the standard deviation of the data 
data_sd = np.std(winequality_red_data["quality"]) 
# Compute the maximum and minimum values of the data 
data_max = np.max(winequality_red_data["quality"]) 
data_min = np.min(winequality_red_data["quality"]) 
# Obtain the 60th percentile of the data 
data_percentile = np.percentile(winequality_red_data["quality"],60) 
# Obtain the quartiles of the data 
data_quartile = np.quantile(winequality_red_data["quality"],0.75) 
# Get the IQR of the data 
data_IQR = stats.iqr(winequality_red_data["quality"]) 
results = {
    "Statistic": ["Mean", "Median", "Mode", "Variance", "Standard Deviation", 
                  "Max", "Min", "60th Percentile", "75th Quantile", "IQR"],
    "Value": [data_mean, data_median, mode_value, data_variance, data_sd,
              data_max, data_min, data_percentile, data_quartile, data_IQR]
}
df_results = pd.DataFrame(results)
df_results.to_csv(r"e:\Download\winequality_summary.csv", index=False)