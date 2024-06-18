import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Membaca data dari file CSV
penjualan_ikan_df = pd.read_csv('penjualan_ikan.csv')
produk_df = pd.read_csv('produk.csv')

# Merge tabel-tabel yang dibutuhkan
merged_df = pd.merge(penjualan_ikan_df, produk_df, on='id_produk')

# 1. Korelasi antara harga per unit produk dan total penjualan
correlation = merged_df['harga_per_unit'].corr(merged_df['total_harga'])
print("Korelasi antara harga per unit produk dan total penjualan:", correlation)

# 2. Regresi linier antara jumlah produk yang terjual dan total harga
X = merged_df['kuantitas'].values.reshape(-1, 1)
y = merged_df['total_harga'].values.reshape(-1, 1)

regressor = LinearRegression()
regressor.fit(X, y)
y_pred = regressor.predict(X)

plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('Regresi Linier Antara Jumlah Produk dan Total Harga')
plt.xlabel('Jumlah Produk Terjual')
plt.ylabel('Total Harga')
plt.show()

# 3. Analisis tren penjualan dari waktu ke waktu
merged_df['tanggal'] = pd.to_datetime(merged_df['tanggal'])
monthly_sales = merged_df.resample('M', on='tanggal').sum()['total_harga']
monthly_sales.plot(figsize=(10, 6), marker='o', color='green')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Tanggal')
plt.ylabel('Total Penjualan (Rupiah)')
plt.show()
