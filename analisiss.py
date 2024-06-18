import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
penjualan_ikan_df = pd.read_csv('penjualan_ikan.csv')
produk_df = pd.read_csv('produk.csv')
wilayah_df = pd.read_csv('wilayah.csv')
penjualan_per_wilayah_df = pd.read_csv('penjualan_per_wilayah.csv')

# Merge tabel-tabel yang dibutuhkan
merged_df = pd.merge(penjualan_ikan_df, produk_df, on='id_produk')
merged_df = pd.merge(merged_df, penjualan_per_wilayah_df, on='id_transaksi')
merged_df = pd.merge(merged_df, wilayah_df, on='id_wilayah')

# Plot Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='nama_produk', y='total_harga', data=merged_df, palette='Set3')
plt.title('Boxplot Total Penjualan per Produk')
plt.xlabel('Nama Produk')
plt.ylabel('Total Penjualan (Rupiah)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Grafik Garis
plt.figure(figsize=(10, 6))
total_penjualan_per_tanggal = merged_df.groupby('tanggal')['total_harga'].sum()
total_penjualan_per_tanggal.plot(kind='line', marker='o', color='green')
plt.title('Grafik Garis Total Penjualan per Tanggal')
plt.xlabel('Tanggal')
plt.ylabel('Total Penjualan (Rupiah)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Barplot dengan warna berbeda-beda
plt.figure(figsize=(10, 6))
total_penjualan_per_wilayah = merged_df.groupby('nama_wilayah')['total_harga'].sum().sort_values(ascending=False)
colors = sns.color_palette('husl', len(total_penjualan_per_wilayah))
total_penjualan_per_wilayah.plot(kind='bar', color=colors)
plt.title('Barplot Total Penjualan per Wilayah')
plt.xlabel('Wilayah')
plt.ylabel('Total Penjualan (Rupiah)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Area Chart
plt.figure(figsize=(10, 6))
total_penjualan_per_produk = merged_df.groupby('nama_produk')['total_harga'].sum().sort_values(ascending=False)
total_penjualan_per_produk.plot(kind='area', color='skyblue', alpha=0.5)
plt.title('Area Chart Total Penjualan per Produk')
plt.xlabel('Produk')
plt.ylabel('Total Penjualan (Rupiah)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
