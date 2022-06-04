import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

base_2019 = 'statistics.xlsx'

df_2019 = pd.read_excel(base_2019, engine='openpyxl')

df_2019_monthly = df_2019.resample('M', on='Date').sum()

# resample changes indexes
df_2019_monthly.reset_index(inplace=True)

# replace 2019 to 2022
df_2019_monthly['Date'] = df_2019_monthly['Date'] + pd.DateOffset(years=3) 

fig, ax = plt.subplots(figsize=(6,4))

x_data_name = 'Date'
y_data_name = 'Price'

p1 = sb.lineplot(data=df_2019_monthly, x=x_data_name, y=y_data_name, ax=ax, label='2019')
# p2 = sb.lineplot(data=df_2020_monthly, x=x_data_name, y=y_data_name, ax=ax, label='2020')

ax.figure.autofmt_xdate()
