import pandas as pd
import os
from core.paths import EXCEL_FILE

def append_result(row):
    df = pd.DataFrame([row])

    if os.path.exists(EXCEL_FILE):
        existing = pd.read_excel(EXCEL_FILE)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_excel(EXCEL_FILE, index=False)
