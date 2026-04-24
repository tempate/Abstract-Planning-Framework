import pandas as pd
import os

EXCEL_FILE = os.path.join(os.path.dirname(__file__), "results_automatically.xlsx")

def append_to_excel(row):
    df = pd.DataFrame([row])

    if os.path.exists(EXCEL_FILE):
        existing = pd.read_excel(EXCEL_FILE)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_excel(EXCEL_FILE, index=False)