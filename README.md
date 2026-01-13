# Weather Station Data Analytics System

## Overview
This project is a Python-based data analytics pipeline designed to process and analyze weather station sensor data.  
It simulates how real-world IoT weather data is handled in industry by performing data cleaning, validation, statistical analysis, visualization, and automated reporting.

The project focuses on **clean, modular Python scripts** rather than notebooks, following industry-style development practices.

---

## Problem Statement
Weather stations continuously generate large volumes of raw sensor data.  
This data often contains:
- Missing values
- Duplicate records
- Invalid or unrealistic sensor readings

Raw data cannot be used directly for analysis.  
A reliable preprocessing pipeline is required to clean, validate, analyze, and visualize this data before it can be used for decision-making.

---

## Project Objectives
- Read and process real-world weather station CSV data  
- Handle missing and duplicate sensor readings  
- Validate sensor values using realistic physical ranges  
- Perform basic statistical analysis  
- Visualize time-series temperature trends  
- Automate generation of summary reports  
- Maintain a clean and modular project structure  

---

## Dataset
The project uses a real-world Kaggle dataset:

**Global Weather Repository (Kaggle)**  

Columns used in this project:
- `last_updated`
- `temperature_celsius`
- `humidity`
- `pressure_mb`
- `wind_kph`

The raw dataset is kept intact, and only required columns are selected during processing.

---

## Tech Stack
- Python 3  
- Pandas  
- Matplotlib  
- Visual Studio Code  
- Git & GitHub  

---

## Project Structure
```
weather_station_analytics/
│
├── data/
│   └── kaggle_weather.csv
│
├── scripts/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── statistics.py
│   └── visualization.py
│
├── automation/
│   └── daily_report.py
│
├── main.py
├── README.md
└── .gitignore
```
---

## Data Processing Pipeline
1. **Data Loading**  
   - Reads CSV data and parses timestamps  

2. **Data Cleaning**  
   - Sorts time-series data  
   - Removes duplicate records  
   - Handles missing values using forward-fill  
   - Validates temperature and wind speed ranges  

3. **Feature Selection**  
   - Selects only relevant sensor columns for analysis  

4. **Statistical Analysis**  
   - Computes summary statistics such as mean, minimum, and maximum values  

5. **Visualization**  
   - Plots daily average temperature trends  

6. **Automation**  
   - Generates a daily summary report as a text file  

---
## How to Run the Project

### Install dependencies
```bash
pip install pandas matplotlib
```

### Run main analysis
```bash
python main.py
```

### Generate automated report
```bash
python -m automation.daily_report
```
_Last updated via GitHub UI._

