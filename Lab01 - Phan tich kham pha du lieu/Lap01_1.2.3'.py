#=====================================================
# PHẦN 2: XỬ LÝ VÀ TRỰC QUAN HÓA DỮ LIỆU
#=====================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"e:\Download\Online Retail.csv", encoding='ISO-8859-1')
# --- 1. Histogram về số lượng bán ---
plt.figure(figsize=(8,5))
sns.histplot(df['Quantity'], bins=30, kde=True)
plt.title("Phân phối số lượng sản phẩm bán")
plt.xlabel("Quantity")
plt.ylabel("Tần suất")
plt.show()

# --- 2. Boxplot phát hiện outlier của giá ---
plt.figure(figsize=(8,5))
sns.boxplot(x=df['UnitPrice'])
plt.title("Boxplot - Đơn giá sản phẩm")
plt.xlabel("Unit Price")
plt.show()

# --- 3. Doanh thu theo thời gian ---
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
daily_sales = df.groupby(df['InvoiceDate'].dt.date)['TotalPrice'].sum()

plt.figure(figsize=(10,5))
daily_sales.plot()
plt.title("Doanh thu theo ngày")
plt.xlabel("Ngày")
plt.ylabel("Tổng doanh thu")
plt.show()

# --- 4. Top 10 sản phẩm bán chạy ---
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 sản phẩm bán chạy nhất")
plt.xlabel("Tổng số lượng bán")
plt.ylabel("Sản phẩm")
plt.show()

# --- 5. Top 10 khách hàng có doanh thu cao nhất ---
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title("Top 10 khách hàng mua nhiều nhất")
plt.xlabel("Tổng giá trị mua hàng")
plt.ylabel("Customer ID")
plt.show()

# --- 6. Doanh thu theo quốc gia ---
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(x=country_sales.values, y=country_sales.index)
plt.title("Doanh thu theo quốc gia")
plt.xlabel("Tổng doanh thu")
plt.ylabel("Quốc gia")
plt.show()