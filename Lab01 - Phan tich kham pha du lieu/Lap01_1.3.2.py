#=====================================================
# PHẦN 3: PHÂN TÍCH ĐƠN BIẾN VÀ HAI BIẾN
#=====================================================
# Khởi tạo AutoViz
import pandas as pd
from autoviz import AutoViz_Class

# Khởi tạo AutoViz
AV = AutoViz_Class()

# Đọc dữ liệu Marketing Campaign
file_path = r"e:\Download\marketing_campaign.csv"
data = pd.read_csv(file_path, sep='\t', encoding='latin1')

# Xem 5 dòng đầu
print(data.head(), "\n")

# ====================================================
# PHÂN TÍCH TỰ ĐỘNG
# ====================================================

AV = AutoViz_Class()

df_return = AV.AutoViz(
    filename=file_path,
    sep=',',
    depVar='Response'
)
print(df_return.head())