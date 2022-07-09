# Dataframe sort:
df_sorted = df.sort_values(by=['Colums'], ascending=[True|False])

# Get columns
df = df_old.filter(['Column1','Column2'], axis=1)

# Count rows
df_vals = df['Column'].value_counts().index.tolist()
df_vals_count = df['Column'].value_counts().tolist()

# Dataframe to dict
dictionary = {}
for index in range(len(df)):
    ln = df['Column1'][index]
    delay = df['Column2'][index]

# Dict to dataframe:
df = pd.DataFrame()
   
for key, value in dictionary.items():
    df = df.append({'Column1' : key, 'Column2' : value}, 
                ignore_index = True)
