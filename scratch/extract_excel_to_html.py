import pandas as pd
import sys

file_path = "Parts_DB_Detailed Definition.xlsx"

try:
    xl = pd.ExcelFile(file_path)
    sheet_names = xl.sheet_names
    
    print(f"Sheet Names: {sheet_names}", file=sys.stderr)
    
    for sheet_name in sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Drop rows where all elements are NaN
        df = df.dropna(how='all')
        # Fill NaN with empty string
        df = df.fillna('')
        
        print(f"--- SHEET: {sheet_name} ---")
        # Convert to HTML table with specific class
        html_table = df.to_html(index=False, classes='code-table')
        print(html_table)
        print("--- END ---")
        
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
