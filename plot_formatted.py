import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

db_soc = 'file.xlsx'

df_old = pd.read_excel(db_soc, engine='openpyxl')
df = df_old.filter(['col1','col2','col3'], axis=1)

df_range = df.loc[(df['col1'] > '2000-01-01 00:00:00') & (df['col1'] < '2000-01-01 12:00:00')]

df_range["col1"] = pd.to_datetime(df_range["col1"], format = "%Y-%m-%d %H:%M:%S")

fig, ax = plt.subplots(figsize=(20,8))

diag = sb.scatterplot(data=df_range, x='col1', y='col2', ax=ax)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M:%S'))

plt.xticks(rotation=45)
