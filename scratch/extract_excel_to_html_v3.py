import pandas as pd
import sys
import io

# Set encoding for stdout to utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

file_path = "Parts_DB_Detailed Definition.xlsx"

try:
    xl = pd.ExcelFile(file_path)
    sheet_names = xl.sheet_names
    
    targets = {
        'tb_Parts': '4.2.1. 파츠 정보',
        'tb_PartsOptionGroup': '4.2.2. 파츠 옵션 그룹'
    }
    
    for sheet_id, title in targets.items():
        if sheet_id in sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_id)
            df = df.dropna(how='all').fillna('')
            
            print(f"### TITLE: {title} ###")
            # Convert to HTML table
            html_table = df.to_html(index=False, classes='code-table')
            print(html_table)
            print("### END ###")
        else:
            print(f"Warning: Sheet {sheet_id} not found", file=sys.stderr)
            
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
