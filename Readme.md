# Associates Performance Dashboard

## Overview
This interactive Streamlit dashboard provides a comprehensive analysis of associates' performance based on lead generation data. The application visualizes key performance metrics through six distinct visual components that help managers and team leaders identify trends, efficiency patterns, and areas for improvement.

## Dashboard Components

### 1. 📈 Performance Trend with Attendance
Tracks lead generation performance against team meeting attendance, helping identify correlation between team review participation and productivity. Associates who attended reviews are shown with solid lines and circle markers, while those who missed reviews appear with dashed lines and X markers.

### 2. 🔥 Time vs Leads Heatmap
A color-coded matrix visualization showing the relationship between time invested in lead generation and results achieved. The heatmap makes it easy to identify optimal time investment zones and diminishing returns.

### 3. 📊 Monthly Performance Comparison
Bar charts comparing lead generation performance across associates on a monthly basis, allowing for easy identification of consistent performers and those who may need additional support.

### 4. 📉 Daily Incomplete Leads Tracking
Line graph showing incomplete leads over time for each associate, helping identify patterns in lead quality and follow-through that may require attention.

### 5. ⏱️ Time Distribution Analysis
Boxplot visualization showing the distribution of time spent on lead generation tasks across associates, highlighting work pattern differences and potential efficiency issues.

### 6. 🚀 Efficiency Scatter Analysis
Scatter plot displaying the relationship between time invested and leads generated, with point size indicating lead volume. This visualization helps identify associates who achieve optimal results with minimal time investment.

## Demo

Access a live demo of the dashboard here: [Associates Performance Dashboard Demo](https://reportdashboard.streamlit.app/)

## How to run the dashboard

### Step 1: Clone from GitHub
```bash
git clone https://github.com/Harishapatkar/Report
```
### Step 2: Download required libraries
```bash
pip install -r requirements.txt
```
### Step 3: Run the code
```bash
streamlit run test5.py
```

