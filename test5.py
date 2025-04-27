# Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime

# Streamlit page settings
st.set_page_config(
    page_title="Associates Performance Dashboard",
    layout="wide",
)

# CSS for style
st.markdown(
    """
<style>
    .main {padding: 1rem;}
    .highlight-card {background-color: #f0f7ff; border-left: 5px solid #3498db; padding: 10px; margin: 10px 0;}
    .stPlotlyChart, .stPyplot, .stAltairChart {
        margin: auto;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.title("📊 Associates Performance Dashboard")
st.caption(f"Date: {datetime.now().strftime('%B %d, %Y')}")


# Load Data
@st.cache_data
def load_data():
    file_path = "Data Assignment.xlsx"
    sheets = pd.read_excel(file_path, sheet_name=None)
    df_list = []
    for name, data in sheets.items():
        data["Associate"] = name
        df_list.append(data)
    df = pd.concat(df_list, ignore_index=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    df["Month_str"] = df["Month"].astype(str)
    df["Day"] = df["Date"].dt.day_name()
    np.random.seed(42)
    df["Team_Review_Attended"] = np.random.choice(
        [True, False], size=len(df), p=[0.8, 0.2]
    )
    return df


df = load_data()

# Chart settings
chart_width = 6
chart_height = 4

# ROW 1 - 3 Charts
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.subheader("📈 Performance Trend with Attendance")
    attendance_df = (
        df.groupby(["Date", "Associate", "Team_Review_Attended"])["Leads"]
        .sum()
        .reset_index()
    )

    attended = attendance_df[attendance_df["Team_Review_Attended"]]
    missed = attendance_df[~attendance_df["Team_Review_Attended"]]

    fig, ax = plt.subplots(figsize=(chart_width, chart_height))
    for associate in df["Associate"].unique():
        data_attended = attended[attended["Associate"] == associate]
        data_missed = missed[missed["Associate"] == associate]
        if not data_attended.empty:
            ax.plot(
                data_attended["Date"],
                data_attended["Leads"],
                label=f"{associate} (Attended)",
                marker="o",
            )
        if not data_missed.empty:
            ax.plot(
                data_missed["Date"],
                data_missed["Leads"],
                label=f"{associate} (Missed)",
                linestyle="--",
                marker="x",
            )
    ax.set_xlabel("Date")
    ax.set_ylabel("Leads")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize="small")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with row1_col2:
    st.subheader("🔥 Time vs Leads Heatmap")
    time_bins = [0, 30, 60, 90, 120, 150, 180, 210, 240]
    leads_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40]

    df["Time_Bin"] = pd.cut(
        df["Time spent on LG (mins)"],
        bins=time_bins,
        labels=[f"{time_bins[i]}-{time_bins[i+1]}" for i in range(len(time_bins) - 1)],
    )
    df["Leads_Bin"] = pd.cut(
        df["Leads"],
        bins=leads_bins,
        labels=[
            f"{leads_bins[i]}-{leads_bins[i+1]}" for i in range(len(leads_bins) - 1)
        ],
    )

    heatmap_data = pd.crosstab(df["Time_Bin"], df["Leads_Bin"])

    fig, ax = plt.subplots(figsize=(chart_width, chart_height))
    sns.heatmap(heatmap_data, annot=True, fmt="g", cmap="YlGnBu", cbar=False, ax=ax)
    ax.set_xlabel("Leads Bin")
    ax.set_ylabel("Time Bin")
    st.pyplot(fig)

with row1_col3:
    st.subheader("📊 Monthly Performance")
    monthly_df = df.groupby(["Month_str", "Associate"])["Leads"].sum().reset_index()

    fig, ax = plt.subplots(figsize=(chart_width, chart_height))
    sns.barplot(data=monthly_df, x="Month_str", y="Leads", hue="Associate", ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Leads")
    plt.xticks(rotation=45)
    ax.legend(fontsize="small")
    st.pyplot(fig)

# ROW 2 - 3 Charts
row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.subheader("📉 Daily Incomplete Leads")
    incomplete_trend = (
        df.groupby(["Date", "Associate"])["No. of Incomplete Leads"].sum().reset_index()
    )

    fig, ax = plt.subplots(figsize=(chart_width, chart_height))
    sns.lineplot(
        data=incomplete_trend,
        x="Date",
        y="No. of Incomplete Leads",
        hue="Associate",
        marker="o",
        ax=ax,
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Incomplete Leads")
    plt.xticks(rotation=45)
    ax.legend(fontsize="small")
    st.pyplot(fig)

with row2_col2:
    st.subheader("⏱️ Time Distribution")
    fig, ax = plt.subplots(figsize=(chart_width, chart_height))
    sns.boxplot(
        data=df, x="Associate", y="Time spent on LG (mins)", palette="pastel", ax=ax
    )
    ax.set_xlabel("Associate")
    ax.set_ylabel("Time Spent (mins)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with row2_col3:
    st.subheader("🚀 Efficiency Analysis")
    fig, ax = plt.subplots(figsize=(chart_width, chart_height))
    sns.scatterplot(
        data=df,
        x="Time spent on LG (mins)",
        y="Leads",
        hue="Associate",
        size="Leads",
        sizes=(50, 300),
        alpha=0.7,
        ax=ax,
    )
    ax.set_xlabel("Time Spent (mins)")
    ax.set_ylabel("Leads")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize="small")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Created by Harisha Patkar")
