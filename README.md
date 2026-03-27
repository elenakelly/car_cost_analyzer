# 🚗 Car Rental Cost Analyzer

A Python tool for extracting, analyzing, and visualizing car rental expenses from PDF receipts.

This project transforms raw rental receipts into structured data and actionable insights, helping you better understand your spending patterns and identify opportunities to reduce costs.

---

## 📌 Features

- 📄 Extract data from PDF receipts
- 🔍 Parse trip details (date, price, etc.)
- 🧹 Clean and structure raw data
- 📊 Analyze spending behavior
- 📈 Interactive visualizations
- 🌐 Dashboard interface using Streamlit
- 📁 Export processed data and reports

---

## 🏗️ Project Structure
car_cost_analyzer/ <br>
│<br>
├── data/<br>
│   └── raw_pdfs/          # Input PDF receipts<br>
│<br>
├── src/<br>
│   ├── extractor.py       # PDF text extraction<br>
│   ├── parser.py          # Data parsing logic<br>
│   ├── cleaner.py         # Data cleaning & formatting<br>
│   ├── analyzer.py        # Insights & aggregations<br>
│   ├── visualizer.py      # Charts & plots<br>
│<br>
├── app/<br>
│   └── dashboard.py       # Streamlit dashboard<br>
│<br>
├── outputs/<br>
│   ├── reports/           # CSV / reports<br>
│   └── charts/            # Saved visualizations<br>
│<br>
├── main.py                # Main pipeline script<br>
└── requirements.txt       # Dependencies<br>

## How It Works
1.	Extraction
2.	Parsing
3.	Cleaning
4.	Analysis
5.	Visualization

## Future Improvements
- Smart categorization
- Cost optimization insights
- ML predictions
- Database integration
