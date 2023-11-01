# How does purchase value depend on the Internet Browser used and Job (Profession) of the purchaser?
import os
import pandas as pd 
import matplotlib.pyplot as plt

from Pre_processes import data_task3

purchase_frequency = data_task3.groupby('Platform')['Browser Info'].count().reset_index(name='Purchase Frequency')
desktop = data_task3.loc[data_task3['Platform'] == 'Desktop']
mobile = data_task3.loc[data_task3['Platform'] == 'Mobile']

desktop = desktop.groupby('Browser Info')['Browser Info'].count().reset_index(name='Purchase Frequency')
mobile = mobile.groupby('Browser Info')['Browser Info'].count().reset_index(name='Purchase Frequency')

print(purchase_frequency)
print(desktop)
print(mobile)


# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
# plt.scatter(jobs['Browser Info'].str.split('/').str[0], jobs['Job'], c=jobs['Purchase Price'], cmap='viridis', s=jobs['Purchase Price']*5)
# plt.colorbar(label='Purchase Price')
# plt.xlabel('Internet Browser')
# plt.ylabel('Job')
# plt.title('Purchase Value vs. Internet Browser and Job')

# plt.show()