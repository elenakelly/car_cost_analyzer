import os

from src.extractor import extract_text_from_pdf
from src.parser import parse_receipt
from src.cleaner import clean_data
from src.analyzer import analyze
from src.visualizer import plot_monthly

DATA_FOLDER = "data/raw_pdfs"

def main():
    all_data = []

    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".pdf"):
            path = os.path.join(DATA_FOLDER, file)

            print(f"Processing: {file}")

            text = extract_text_from_pdf(path)
            parsed = parse_receipt(text)

            all_data.extend(parsed)

    df = clean_data(all_data)

    analyze(df)
    plot_monthly(df)

    # Save output
    df.to_csv("output.csv", index=False)
    print("\nData saved to output.csv")


if __name__ == "__main__":
    main()