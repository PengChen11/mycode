import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns

"""
This program take an insruance costs data sheet with patients in different age group, trying to see whether the medical cost is related to age
"""


insurance_df = pd.read_csv('./insurance.csv')

#  will choose only "age" and "charges" colums, group data by "age", calculate the mean for each age group,
#  then round it to 0 digit, take the value of "charges" coloum (ages will no longer be used)

mean_charge_by_age = insurance_df[["age","charges"]].groupby("age").mean().round(0)["charges"].values

# groupby returns a dataFrameGroupBy instance, it is different to data frame. that's why I can only take the mean values.

# we know the age start and ending point, now making an age array with numpy
age = np.asarray(list(range(18,65)))

# becasue of groupby issue, I have to make a new data frame object
new_df = pd.DataFrame({'age': age, 'charges':mean_charge_by_age})

sns.set()
plt.figure(figsize=(10,6),dpi=300)
sns.regplot( x="age", y='charges', data=new_df, order=1)
plt.savefig("output.png")


x=age.reshape(-1,1)
y=mean_charge_by_age
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=100)

lm = LinearRegression()
lm.fit(x_train,y_train)
print(f"Train accuracy {round(lm.score(x_train,y_train)*100,2)} %")
print(f"Test accuracy {round(lm.score(x_test,y_test)*100,2)} %")
