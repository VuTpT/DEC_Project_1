# Find the relationship between top 5 Job designation and total Purchase amount
import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from Define_data import states, job_list, job_category

# Address,Lot,AM or PM,Browser Info,Company,Credit Card,CC Exp Date,
# CC Security Code,CC Provider,Email,Job,IP Address,Language,Purchase Price

path = 'Resource/Ecommerce_Purchases.csv'
data = pd.read_csv(filepath_or_buffer=path, delimiter=',')

# Task 1
col_names_1 = ['Job', 'Purchase Price']
jobs = data.loc[:, col_names_1]
job_list = pd.DataFrame(job_list, columns=['CodeID', 'Category', 'CodeName'])
result_task1 = jobs.merge(job_list, how='left', left_on='Job', right_on='CodeID')
col_task1 = ['Job', 'Purchase Price', 'Category']
data_task1 = result_task1[col_task1]
job_category = pd.DataFrame(job_category, columns=['CodeID', 'Lists', 'CodeName'])
result_task1 = data_task1.merge(job_category, how='left', left_on='Category', right_on='CodeID')
col_task1 = ['Job', 'Purchase Price', 'Category', 'Lists']
data_task1 = result_task1[col_task1]
#print(data_task1)

# Task 3
col_names_3 = ['Job', 'Purchase Price', 'Browser Info']
platform = data.loc[:, col_names_3]
platform['Platform'] = np.where(platform['Browser Info'].str.contains('Mobile', case=False, na=False), 'Mobile', 'Desktop')
platform['Browser Info'] = platform['Browser Info'].str.split('/').str[0]
data_task3 = platform
#print(data_task3)


# Task 4
col_names_4 = ['Address', 'AM or PM', 'Purchase Price']
addresses = data.loc[:, col_names_4]
addresses['State'] = addresses['Address'].str.extract(r'\s+([A-Z]{2})\s+', expand=False)
states = pd.DataFrame(states, columns=['CodeID', 'Region', 'CodeName'])
result_task4 = addresses.merge(states, how='left', left_on='State', right_on='CodeID')
col_task4 = ['State', 'Region', 'AM or PM', 'Purchase Price']
data_task4 = result_task4[col_task4]
#print(addresses['State'].unique())
#print(result[result['CodeID'].isna()]['State'].unique())
#print(data_task4)


# Task 5 
col_names_5 = ['CC Provider', 'AM or PM', 'Purchase Price']
cards = data.loc[:, col_names_5]
replacements = {
    r'American Express': 'American Express',
    r'Diners Club / Carte Blanche': 'Diners Club / Carte Blanche',
    r'Discover': 'Discover',
    r'JCB 15 digit': 'JCB',
    r'JCB 16 digit': 'JCB',
    r'Maestro': 'Maestro',
    r'Mastercard': 'Mastercard',
    r'VISA 13 digit': 'VISA',
    r'VISA 16 digit': 'VISA',
    r'Voyager': 'Voyager'
}
cards['CC Provider'] = cards['CC Provider'].replace(replacements, regex=True)
data_task5 = cards 
#print(cards['CC Provider'].unique())