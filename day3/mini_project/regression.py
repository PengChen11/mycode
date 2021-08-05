import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# setup seaborn to make a better looking plot and output it
sns.set()
plt.figure(figsize=(10,6),dpi=100)
sns.regplot( x="age", y='charges', data=new_df, order=1)
plt.savefig("output.png")


print(f"\nPlease check the png file for plot. ")
print(f"\n1. Based on the Linear regression model, we can see that the patients' average medical charges are related to the age.\n2. In general, the higher the patients' age, the higher the medical charges.")
