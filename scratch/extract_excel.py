import pandas as pd

try:
    df = pd.read_excel('UI_DESC.xlsx', sheet_name='pickup_results_UI')
    df.to_csv('scratch/ui_desc_output.csv', index=False, encoding='utf-8-sig')
except Exception as e:
    print(f"Error: {e}")
