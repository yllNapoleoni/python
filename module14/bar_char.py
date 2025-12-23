import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('avgiqpercountry.csv')
filtered_df=df[df['average iq']>=100]

filtered_df=filtered_df.sort_values(by='average iq',ascending=False)

print(filtered_df)

plt.figure(figsize=(14,8))

bars=plt.bar(filtered_df['country'],filtered_df['aberaqe iq'],color='skyblue')

plt.title('average iq by vountry(iq>=100)',fontsize=16)

plt.xlabel('country',frontside=14)
plt.ylabel('average iq',frontside=14)

plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis='y',linestyle='--',alpha=0.8)

plt.bar_label(bars,fmt='%.2f',fontsize=10,color='black')
plt.tight_layout()
plt.show()



















