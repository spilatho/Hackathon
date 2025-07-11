import pandas as pd
import openpyxl
filePath='C:\\AgenticAiData\\Vacation Tracker_2025. Compass.3.0.xlsx'
sheetName="Sep\'25"


def getLeaveData():
    filePath='C:\\AgenticAiData\\Vacation Tracker_2025. Compass.3.0.xlsx'
    sheetName="Sep'25"
    df = pd.read_excel(filePath,sheet_name=sheetName)
    df_cleaned = df.dropna(how='all')
    print(df_cleaned.head())
    json_data = df_cleaned.where(pd.notnull(df_cleaned), None).to_dict(orient="records")
    # return df_cleaned.to_dict(orient="records")
    return json_data

    # df_cleaned.to_excel("cleaned_file.xlsx", index=False)


getLeaveData()