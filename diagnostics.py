import pandas as pd

def calculate_metrics(math, science, english, history):
    data = {
        "Subject": ["Math", "Science", "English", "History"],
        "Grade": [math, science, english, history]
    }
    return pd.DataFrame(data)

def generate_insights(df):
    highest_idx = df["Grade"].idxmax()
    lowest_idx = df["Grade"].idxmin()
    
    return {
        "highest_sub": df.loc[highest_idx]["Subject"],
        "lowest_sub": df.loc[lowest_idx]["Subject"],
        "lowest_grade": df["Grade"].min(),
        "avg_grade": df["Grade"].mean()
    }