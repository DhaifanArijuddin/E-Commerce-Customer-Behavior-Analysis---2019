import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("data/dataset_clean_final_customer.csv")

# Pastikan kolom DateTime jadi tipe datetime
df['DateTime'] = pd.to_datetime(df['DateTime'])

# ==============================
# SIDEBAR FILTER
# ==============================
st.sidebar.header("Filter Data")
category_filter = st.sidebar.multiselect("Pilih Kategori", options=df['Category'].unique(), default=df['Category'].unique())
action_filter = st.sidebar.multiselect("Pilih Action", options=df['Action'].unique(), default=df['Action'].unique())

df_filtered = df[
    (df['Category'].isin(category_filter)) &
    (df['Action'].isin(action_filter))
]

# ==============================
# HEADER
# ==============================
st.title("📊 E-Commerce Customer Behavior Analysis - 2019 Dashboard")
st.markdown("Analisis perilaku pelanggan dan konversi funnel berdasarkan data event.")

# ==============================
# KPI METRICS
# ==============================
col1, col2, col3 = st.columns(3)
col1.metric("Total User", df_filtered['User_id'].nunique())
col2.metric("Total Session", df_filtered['Session_id'].nunique())
col3.metric("Total Event", len(df_filtered))

# ==============================
# FUNNEL CHART
# ==============================
st.subheader("Funnel Konversi")
funnel_order = ["view", "search", "cart", "purchase"]
funnel_df = df_filtered.groupby("Action")['User_id'].nunique().reindex(funnel_order).dropna().reset_index()
funnel_df.columns = ["Stage", "Unique Users"]

fig_funnel = px.funnel(funnel_df, x="Unique Users", y="Stage", title="User Funnel")
st.plotly_chart(fig_funnel, use_container_width=True)

# ==============================
# TREND AKTIVITAS USER
# ==============================
st.subheader("Tren Aktivitas User per Hari")
trend_df = df_filtered.groupby(df_filtered['DateTime'].dt.date)['User_id'].nunique().reset_index()
trend_df.columns = ["Date", "Unique Users"]

fig_trend = px.line(trend_df, x="Date", y="Unique Users", markers=True, title="Tren Harian User Unik")
st.plotly_chart(fig_trend, use_container_width=True)

# ==============================
# TOP CATEGORY
# ==============================
st.subheader("Top 10 Kategori Berdasarkan Aktivitas")
cat_df = df_filtered['Category'].value_counts().reset_index()
cat_df.columns = ["Category", "Event Count"]
cat_df = cat_df.head(10)

fig_cat = px.bar(cat_df, x="Category", y="Event Count", title="Top Kategori", text="Event Count")
fig_cat.update_traces(textposition="outside")
st.plotly_chart(fig_cat, use_container_width=True)

# ==============================
# TABEL DATA
# ==============================
st.subheader("Data Sample")
st.dataframe(df_filtered.head(50))
