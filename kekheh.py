# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 03:51:37 2020

@author: Torpeda
"""

import pandas
import pandas as pd
import matplotlib.pyplot as plt
data = pandas.read_csv('AdultEducationLevel.csv', header=1); #zagruzka faila
Adult1_df = pd.read_csv('AdultEducationLevel.csv', header=1)
df1=Adult1_df
df1.to_excel("AdultEducationLevel.xlsx")
countries = ['AUS', 'BEL', 'KOR', 'POL']
subjects = ['BUPPSRY', 'TRY', 'UPPSRY']

#risuem graphiki
fig =  plt.figure(figsize=(6,4*len(countries)))
for i, country in enumerate(countries):
    ax = plt.subplot(len(countries),1,i+1)
    for subject in subjects:
        cond = (data['LOCATION']==country) & (data['SUBJECT']==subject)
        ax.plot(data[cond] ['TIME'], data[cond] ['Value'])
 #podpisivaem osi
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.legend(subjects)
    ax.set_title(country)
#net peresechenii graphikov
plt.tight_layout()
plt.show()

k = 1
p = 1
test_subject = 'TRY'
mod_data = data[data['SUBJECT']==test_subject].copy()
mod_data['DECADE'] = (mod_data['TIME']//10)*10
mod_data.set_index(['DECADE','LOCATION'], inplace=True)
max_val = mod_data.groupby(['DECADE','LOCATION']).max().groupby('DECADE')['Value'].nlargest(k)
min_val = mod_data.groupby(['DECADE','LOCATION']).min().groupby('DECADE')['Value'].nsmallest(p)
print(max_val, min_val)
"""
df2=max_val
df2.to_excel("Макс значения.xlsx")
df3=min_val
df3.to_excel("Мин значения.xlsx")
"""
print("""
1) Записать максимальные значения в Ексель
2) Записать минимальные значения в ексель
3) Записать максимальные значения в CSV
4) Записать минимальные значения в CSV
""")
answer = input("Выберите пункт меню: ")
if answer == "1":
    print("Данные записаны")
    df2=max_val
    df2.to_excel("Макс значения.xlsx")
elif answer == "2":
    print("Данные записаны")
    df3=min_val
    df3.to_excel("Мин значения.xlsx")
elif answer == "3":
    print("Данные записаны")
    df4=max_val
    df4.to_csv("Макс значения.csv")
elif answer == "4":
    print("Данные записаны")
    df5=min_val
    df5.to_csv("Мин значения.csv")


    