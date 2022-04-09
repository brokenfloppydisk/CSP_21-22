import matplotlib
import pandas

honey_df = pandas.read_csv("honey.csv")

honey_df['Value'] = honey_df['Value'].str.replace(',', '')
honey_df['Value'] = pandas.to_numeric(honey_df['Value'], errors='coerce')
honey_df.dropna(subset=['Value'], inplace=True)

print(honey_df)