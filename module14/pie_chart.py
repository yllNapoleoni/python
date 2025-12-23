import pandas as pd
import matplotlib.pylot as plt

df=pd.read_csv('avgiqpercountry.csv')

novel_prizes_by_continent=df.groupby('continent')['nobel prize']).sum()

no_of_continents=novel_prizes_by_continent.count()
print(no_of_continents)

colors=['gold','lightcoral','yellow','orange','thistle','skyeblue','aquamarine','burlywood']
plt.figure=(figsize=(10,10))
novel_prizes_by_continent.plot(kind='pie',color=colors,autopct='%1.1f%%')
plt.title('distribution of nobel prizes by continent')

plt.axis('equa;')
plt.ylabel('')

plt.tight_layout()
plt.show()