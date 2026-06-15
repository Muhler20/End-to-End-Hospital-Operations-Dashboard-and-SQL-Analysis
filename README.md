<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B0000,100:DC2626&height=250&section=header&text=Hospital%20Operations%20Dashboard&fontSize=55&animation=fadeIn&fontAlignY=38&desc=End-to-End%20Healthcare%20Analytics%20%2B%20SQL&descAlignY=51&descAlign=62" width="100%" />

[![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge\&logo=jupyter\&logoColor=white)](https://jupyter.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)](https://sqlite.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Visualizations-3F4F75?style=for-the-badge\&logo=plotly\&logoColor=white)](https://plotly.com)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](https://pandas.pydata.org)

<br/>

**This project is a Hospital Operations Dashboard ** is an end-to-end healthcare analytics project that transforms raw hospital operations data into actionable business intelligence. The project combines Python, SQL, SQLite, Streamlit, and Plotly to analyze patient flow, resource utilization, departmental performance, length of stay, and readmission trends through an interactive dashboard.

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1000&color=0EA5E9&center=true&vCenter=true&width=700&lines=Analyze+5,000%2B+Hospital+Visits;Track+Length+of+Stay+and+Readmissions;Monitor+Bed+and+ICU+Utilization;Interactive+Healthcare+Dashboard;End-to-End+Analytics+Workflow" />
</p>

</div>

---

# 🏥 Project Overview

Healthcare organizations generate large volumes of operational data every day. This project demonstrates how healthcare data can be transformed into meaningful operational insights through a complete analytics workflow.

The project includes:

* Data Cleaning and Standardization
* Exploratory Data Analysis (EDA)
* SQL Database Creation
* Business Intelligence Queries
* Interactive Streamlit Dashboard
* Healthcare KPI Monitoring

---

# 📊 Key Features

### 📂 Automated Data Pipeline

* Raw CSV ingestion
* Data cleaning and validation
* Categorical value standardization
* SQLite database creation

### 🧹 Data Quality Improvements

The dataset contained inconsistent categorical values such as:

```text
SEVERE
Severe
severe

OPD
Opd
opd
```

These values were standardized to ensure accurate filtering and reporting.

### 📈 Healthcare KPI Tracking

Monitor:

* Total Patients
* Average Length of Stay
* Bed Occupancy Rate
* ICU Utilization
* Readmission Rate

### 🗄 SQL Analytics

Business-focused SQL analysis including:

* Department Performance
* Resource Utilization
* Disease Trends
* Readmission Analysis
* Patient Volume Metrics

### 💻 Interactive Dashboard

Built with:

* Streamlit
* Plotly
* SQLite

Features:

* Dynamic filtering
* Interactive visualizations
* Department-level analysis
* Resource utilization monitoring

---

# 📁 Project Structure

```text
Hospital-Operations-Dashboard/

│
├── hospital_operations_dataset.csv
├── hospital_operations.db
├── hospital_analysis.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

# 🔧 Technologies Used

| Technology       | Purpose                  |
| ---------------- | ------------------------ |
| Python           | Data Processing          |
| Pandas           | Data Cleaning & Analysis |
| SQLite           | Database Storage         |
| SQL              | Business Queries         |
| Plotly           | Interactive Charts       |
| Streamlit        | Dashboard Development    |
| Jupyter Notebook | Analysis Workflow        |

---

# 📈 Business Questions Answered

### Patient Operations

* Which departments handle the highest patient volume?
* Which departments have the longest average stays?
* Which diseases contribute most to hospital demand?

### Resource Utilization

* Which departments have the highest bed occupancy?
* Which departments utilize ICU resources most heavily?
* How is oxygen usage distributed across departments?

### Quality Metrics

* Which departments have the highest readmission rates?
* Which diseases are associated with higher readmission risk?
* How does severity impact operational performance?

---

# 🚀 Running The Project

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Hospital-Operations-Dashboard.git
cd Hospital-Operations-Dashboard
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Dashboard

```bash
streamlit run app.py
```



