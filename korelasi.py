import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
penjualan_ikan_df = pd.read_csv('penjualan_ikan.csv')
produk_df = pd.read_csv('produk.csv')

# Merge tabel-tabel yang dibutuhkan
merged_df = pd.merge(penjualan_ikan_df, produk_df, on='id_produk')

# Plot scatter plot untuk visualisasi korelasi
plt.figure(figsize=(8, 6))
sns.scatterplot(data=merged_df, x='harga_per_unit', y='total_harga', color='blue')
plt.title('Korelasi antara Harga per Unit Produk dan Total Penjualan')
plt.xlabel('Harga per Unit (Rupiah)')
plt.ylabel('Total Penjualan (Rupiah)')
plt.grid(True)
plt.show()
