import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("Zomato_data.csv")
print(dataframe.head())


def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

dataframe.info()

sns.coutplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")

grouped_data = dataframe.groupby('listed_in(type)') ['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)

plt.hist(dataframe['rate'],bins=5)
plt.title("Rating Distribution")
plt.show()

couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)