import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px

st.set_page_config(
    page_title="Hospital Operations Dashboard",
    layout="wide",
    page_icon="🏥"
)

@st.cache_data
def load_data():
    csv_path = "hospital_operations_dataset.csv"
    db_path = "hospital_operations.db"

    if not os.path.exists(db_path):
        df = pd.read_csv(csv_path)

        df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
        df["Length_of_Stay"] = df["Length_of_Stay"].fillna(df["Length_of_Stay"].median())
        df["Oxygen_Units_Used"] = df["Oxygen_Units_Used"].fillna(0)

        df["Visit_Date"] = pd.to_datetime(
            df["Visit_Date"],
            dayfirst=True,
            errors="coerce"
        )

        df["Year"] = df["Visit_Date"].dt.year
        df["Month_Name"] = df["Visit_Date"].dt.month_name()

        df["Bed_Occupancy_Rate"] = (
            df["Beds_Occupied"] / df["Total_Beds_Available"]
        ) * 100

        df["ICU_Occupancy_Rate"] = (
            df["ICU_Beds_Occupied"] / df["ICU_Beds_Available"]
        ) * 100

        df["Readmission_Flag"] = df["Readmission_Within_30_Days"].map({
            "Yes": 1,
            "No": 0
        })

        conn = sqlite3.connect(db_path)
        df.to_sql("hospital_operations", conn, if_exists="replace", index=False)
        conn.close()

    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM hospital_operations", conn)
    conn.close()

    return df


df = load_data()

st.title("🏥 Hospital Operations Dashboard + SQL Analysis")
st.write(
    "An end-to-end healthcare analytics dashboard analyzing patient volume, "
    "department performance, resource utilization, length of stay, and readmission trends."
)

# Sidebar filters
st.sidebar.header("Filters")

departments = st.sidebar.multiselect(
    "Department",
    sorted(df["Department"].dropna().unique()),
    default=sorted(df["Department"].dropna().unique())
)

severity = st.sidebar.multiselect(
    "Severity",
    sorted(df["Severity"].dropna().unique()),
    default=sorted(df["Severity"].dropna().unique())
)

admission_type = st.sidebar.multiselect(
    "Admission Type",
    sorted(df["Admission_Type"].dropna().unique()),
    default=sorted(df["Admission_Type"].dropna().unique())
)

filtered = df[
    df["Department"].isin(departments)
    & df["Severity"].isin(severity)
    & df["Admission_Type"].isin(admission_type)
]

# KPI cards
total_patients = len(filtered)
avg_los = round(filtered["Length_of_Stay"].mean(), 2)
avg_bed_occupancy = round(filtered["Bed_Occupancy_Rate"].mean(), 2)
readmission_rate = round(filtered["Readmission_Flag"].mean() * 100, 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", f"{total_patients:,}")
col2.metric("Avg Length of Stay", f"{avg_los} days")
col3.metric("Avg Bed Occupancy", f"{avg_bed_occupancy}%")
col4.metric("Readmission Rate", f"{readmission_rate}%")

st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Department Performance",
    "Resource Utilization",
    "Readmissions"
])

with tab1:
    st.subheader("Patient Volume Overview")

    dept_volume = (
        filtered.groupby("Department")
        .size()
        .reset_index(name="Total_Patients")
        .sort_values("Total_Patients", ascending=False)
    )

    fig1 = px.bar(
        dept_volume,
        x="Total_Patients",
        y="Department",
        orientation="h",
        title="Patient Volume by Department"
    )
    st.plotly_chart(fig1, use_container_width=True)

    disease_counts = (
        filtered["Disease"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    disease_counts.columns = ["Disease", "Total_Cases"]

    fig2 = px.bar(
        disease_counts,
        x="Total_Cases",
        y="Disease",
        orientation="h",
        title="Top 10 Diseases by Patient Count"
    )
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Department Performance")

    los = (
        filtered.groupby("Department")["Length_of_Stay"]
        .mean()
        .reset_index()
        .sort_values("Length_of_Stay", ascending=False)
    )

    fig3 = px.bar(
        los,
        x="Length_of_Stay",
        y="Department",
        orientation="h",
        title="Average Length of Stay by Department"
    )
    st.plotly_chart(fig3, use_container_width=True)

    severity_count = (
        filtered["Severity"]
        .value_counts()
        .reset_index()
    )
    severity_count.columns = ["Severity", "Total_Patients"]

    fig4 = px.pie(
        severity_count,
        names="Severity",
        values="Total_Patients",
        title="Severity Distribution"
    )
    st.plotly_chart(fig4, use_container_width=True)

with tab3:
    st.subheader("Resource Utilization")

    resource = (
        filtered.groupby("Department")
        .agg(
            Avg_Bed_Occupancy=("Bed_Occupancy_Rate", "mean"),
            Avg_ICU_Occupancy=("ICU_Occupancy_Rate", "mean"),
            Avg_Oxygen_Used=("Oxygen_Units_Used", "mean")
        )
        .reset_index()
    )

    fig5 = px.bar(
        resource,
        x="Department",
        y="Avg_Bed_Occupancy",
        title="Average Bed Occupancy Rate by Department"
    )
    st.plotly_chart(fig5, use_container_width=True)

    fig6 = px.bar(
        resource,
        x="Department",
        y="Avg_ICU_Occupancy",
        title="Average ICU Occupancy Rate by Department"
    )
    st.plotly_chart(fig6, use_container_width=True)

    fig7 = px.bar(
        resource,
        x="Department",
        y="Avg_Oxygen_Used",
        title="Average Oxygen Units Used by Department"
    )
    st.plotly_chart(fig7, use_container_width=True)

with tab4:
    st.subheader("Readmission Analysis")

    readmit_dept = (
        filtered.groupby("Department")["Readmission_Flag"]
        .mean()
        .reset_index()
    )
    readmit_dept["Readmission_Rate"] = readmit_dept["Readmission_Flag"] * 100

    fig8 = px.bar(
        readmit_dept.sort_values("Readmission_Rate", ascending=False),
        x="Readmission_Rate",
        y="Department",
        orientation="h",
        title="Readmission Rate by Department"
    )
    st.plotly_chart(fig8, use_container_width=True)

    readmit_disease = (
        filtered.groupby("Disease")["Readmission_Flag"]
        .mean()
        .reset_index()
    )
    readmit_disease["Readmission_Rate"] = readmit_disease["Readmission_Flag"] * 100

    fig9 = px.bar(
        readmit_disease.sort_values("Readmission_Rate", ascending=False).head(10),
        x="Readmission_Rate",
        y="Disease",
        orientation="h",
        title="Top 10 Diseases by Readmission Rate"
    )
    st.plotly_chart(fig9, use_container_width=True)

st.divider()

with st.expander("Raw Data Explorer"):
    st.dataframe(filtered.head(500), use_container_width=True)

st.caption("Built with Python, SQL, SQLite, Streamlit, pandas, and Plotly.")