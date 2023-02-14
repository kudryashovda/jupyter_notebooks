import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15,5))
ax.grid()
ax.set_ylim(200, 1000)
ax.set_xlim(0, 120)
ax.set(xlabel='step', ylabel='', title='')

y = [...]
x = range(0,len(y))
ax = sns.lineplot(x=x,y=y, color='red')
