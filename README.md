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
car_cost_analyzer/ \\
│\\
├── data/\\
│   └── raw_pdfs/          # Input PDF receipts\\
│\\
├── src/\\
│   ├── extractor.py       # PDF text extraction\\
│   ├── parser.py          # Data parsing logic\\
│   ├── cleaner.py         # Data cleaning & formatting\\
│   ├── analyzer.py        # Insights & aggregations\\
│   ├── visualizer.py      # Charts & plots\\
│\\
├── app/\\
│   └── dashboard.py       # Streamlit dashboard\\
│\\
├── outputs/\\
│   ├── reports/           # CSV / reports\\
│   └── charts/            # Saved visualizations\\
│\\
├── main.py                # Main pipeline script\\
└── requirements.txt       # Dependencies\\

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
