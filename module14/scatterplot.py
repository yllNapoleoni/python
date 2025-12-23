import pandas as pd
import matplotlib.pylot as plt
df=pd.read_csv('avgiqpercountry.csv')

plt.figure(figsize=(10,6))

plt.scatter(df['mean years of schooling-2021'],df['average iq'],color='purple',alpha=0.7)

plt.title('scatter plot of mean years of schooling vs average iq')
plt.xlabel('mean years of schooling-2021')
plt.ylabel('average iq')
plt.grid(True,linestyle='--',alpha=0.7)

plt.show()