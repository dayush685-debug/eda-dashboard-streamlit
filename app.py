import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("📊 EDA Dashboard")
st.write("Upload a CSV file to explore the data")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ================= DATA PREVIEW =================
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # ================= DATASET INFO =================
    st.subheader("📐 Dataset Info")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Cells", df.isnull().sum().sum())

    # ================= MISSING VALUES =================
    st.subheader("🧹 Missing Values")
    missing_df = df.isnull().sum()
    missing_df = missing_df[missing_df > 0]

    if len(missing_df) > 0:
        st.write(missing_df)
    else:
        st.success("No missing values found 🎉")

    # ================= SUMMARY STATISTICS =================
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    # ================= SIDEBAR FILTERS =================
    st.sidebar.header("🔧 Filters")

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_cols) > 0:
        selected_col = st.sidebar.selectbox(
            "Select numeric column",
            numeric_cols
        )

        min_val = float(df[selected_col].min())
        max_val = float(df[selected_col].max())

        selected_range = st.sidebar.slider(
            "Select value range",
            min_val,
            max_val,
            (min_val, max_val)
        )

        filtered_df = df[
            (df[selected_col] >= selected_range[0]) &
            (df[selected_col] <= selected_range[1])
        ]
    else:
        filtered_df = df

    # ================= FILTERED DATA =================
    st.subheader("📁 Filtered Data")
    st.dataframe(filtered_df.head())

    # ================= VISUALIZATIONS =================
    st.subheader("📈 Column Visualization")

    if len(numeric_cols) > 0:
        chart_col = st.selectbox(
            "Choose column for chart",
            numeric_cols,
            key="chart_col"
        )
        st.line_chart(filtered_df[chart_col])

    # ================= CORRELATION HEATMAP =================
    st.subheader("🔗 Correlation Matrix")
    corr = df[numeric_cols].corr()
    st.dataframe(corr.style.background_gradient(cmap="coolwarm"))

else:
    st.info("👆 Please upload a CSV file to continue")