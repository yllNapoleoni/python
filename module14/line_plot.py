from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.lines import lineStyles

df=pd.read_csv('averageiqpercountry.csv')

avg_iq_by_continent=df.groupby('continent')['average iq'].mean()
plt.figure(figsize=(10,6))

avg_iq_by_continent.plot(kind='line',marker='o',color='skyblue')

plt.title=('average iq by continent')
plt.xlabel=('continent')
plt.ylabel=('average iq')

plt.grid(axis='both',linestyle='--',alpha=0.7)

plt.show()
