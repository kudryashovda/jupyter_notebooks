import seaborn as sns


y = [...]

x = range(0,len(y))
ax = sns.scatterplot(x=x,y=y, color='blue')
ax.set_ylim(0, 300)

ax.set(xlabel='', ylabel='', title='')

# add to the botton the same sns with diff x,y - plot all on one image
