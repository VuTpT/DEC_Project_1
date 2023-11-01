# Find the relationship between Job designation and mean Purchase amount
import os
import pandas as pd 
import matplotlib.pyplot as plt

from Pre_processes import data_task1

# ['Job', 'Purchase Price', 'Category', 'Lists']

# Category
list_purchase_avg = data_task1.groupby('Lists')['Purchase Price'].mean().reset_index(name='Mean')
list_purchase_avg = list_purchase_avg.sort_values(by='Mean', ascending=False)
list_purchase_avg = list_purchase_avg.reset_index().drop(columns='index')

# Job Detail
job_purchase_avg = data_task1.groupby('Job')['Purchase Price'].mean().reset_index(name='Mean')
job_purchase_avg = job_purchase_avg.sort_values(by='Mean', ascending=False)
job_purchase_avg = job_purchase_avg.reset_index().drop(columns='index')
job_purchase_avg['Lists'] = data_task1['Lists']
#total = list_purchase_avg['Mean'].sum()
#print(round((list_purchase_avg['Mean'] / total) * 100,0))

# Category
print(list_purchase_avg)
# Job Detail
print(job_purchase_avg.head(5))
