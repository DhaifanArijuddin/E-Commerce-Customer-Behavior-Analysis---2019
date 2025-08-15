# E-Commerce Customer Behavior Analysis - 2019

Aplikasi ini dibuat menggunakan **Streamlit** untuk menganalisis perilaku pelanggan pada platform e-commerce.

## 🔍 Tujuan Proyek
- Memahami perilaku pelanggan selama sesi belanja online.
- Mengidentifikasi pola aktivitas yang mengarah ke pembelian.
- Mengukur **konversi funnel** dari `view` → `product_view` → `add_to_cart` → `purchase`.
- Memberikan rekomendasi untuk meningkatkan konversi penjualan.

## 🛠 Fitur Aplikasi
1. **Dashboard Overview**: Ringkasan jumlah sesi, total transaksi, dan aktivitas pelanggan.
2. **Top Products**: Visualisasi produk yang paling sering dicari, dilihat, dan dibeli.
3. **Conversion Funnel**: Persentase konversi dari setiap tahap aktivitas.
4. **Filter Interaktif**: Pilih kategori atau sub-category produk untuk analisis lebih spesifik.

## 📊 Dataset
- Sumber: [E-Commerce Customer Behavior Data - Kaggle](https://www.kaggle.com/datasets/adithiav/e-commerce-customer-behavior-data)  
- Kolom utama: `User_id`, `Session_id`, `DateTime`, `Category`, `SubCategory`, `Action`, `Quantity`, `Rate`, `Total Price`.
