import seaborn as sns

sns.set_style('whitegrid')

Y1 = [...]
Y2 = [...]

ax = sns.lineplot(x=range(0, len(Y1)), y=Y1, color='red', lw=2)
ax1 = sns.lineplot(x=range(0, len(Y2)), y=Y2, color='blue', lw=2)

ax1.set_ylim(200, 1500)
ax1.set_xlim(0, 50)
ax1.figure.set_size_inches(15,5)
