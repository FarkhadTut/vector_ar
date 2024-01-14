import pandas as pd

# Sample long-format DataFrame
df_long = pd.DataFrame({
    'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
    'Variable': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
})

# Pivot the DataFrame from long to wide format
df_wide = df_long.pivot(index='Date', columns='Variable', values='Value')
print(df_long)
print(df_wide)