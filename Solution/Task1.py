# Find the relationship between top 5 Job designation and total Purchase amount
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from Pre_processes import data_task1

# ['Job', 'Purchase Price', 'Category', 'Lists']

job_purchase_total = data_task1.groupby('Lists')['Purchase Price'].sum().reset_index(name='Total')
top_5_jobs = job_purchase_total.sort_values(by='Total', ascending=False).head(5)
top_5_jobs = top_5_jobs.reset_index().drop(columns='index')

#print(top_5_jobs)

top_5_jobs.plot(x='Lists', y='Total', figsize=(15, 7), kind='bar')
plt.xlabel('Lists')
plt.ylabel('Total Purchase Price')
plt.title('Top 5 Job Designation')
plt.xticks(rotation=0)
plt.show()

#print(top_5_jobs['Category'])
#print(data_task1[data_task1['Category'].isna()]['Job'].unique())
# ('FA', 'Finance and Accounting', 'Category'),
# ('DA', 'Design and Arts', 'Category'),
# ('HMH', 'Health and Mental Health', 'Category'),
# ('TE', 'Technology and Engineering', 'Category'),
# ('SR', 'Science and Research', 'Category')

top_5_jobs_FA = data_task1.loc[data_task1['Category'] == 'FA']
top_5_jobs_FA = top_5_jobs_FA.groupby('Job')['Purchase Price'].sum().reset_index(name='Total')
top_5_jobs_FA = top_5_jobs_FA.sort_values(by='Total', ascending=False).head(5)
top_5_jobs_FA = top_5_jobs_FA.reset_index().drop(columns='index')
#print(top_5_jobs_FA)

top_5_jobs_FA.plot(x='Job', y='Total', figsize=(15, 7), kind='bar')
plt.xlabel('Job')
plt.ylabel('Total Purchase Price')
plt.title('Top 5 Finance and Accounting')
plt.xticks(rotation=0)
plt.show()
    
top_5_jobs_DA = data_task1.loc[data_task1['Category'] == 'DA']
top_5_jobs_DA = top_5_jobs_DA.groupby('Job')['Purchase Price'].sum().reset_index(name='Total')
top_5_jobs_DA = top_5_jobs_DA.sort_values(by='Total', ascending=False).head(5)
top_5_jobs_DA = top_5_jobs_DA.reset_index().drop(columns='index')
#print(top_5_jobs_DA)
    
top_5_jobs_DA.plot(x='Job', y='Total', figsize=(15, 7), kind='bar')
plt.xlabel('Job')
plt.ylabel('Total Purchase Price')
plt.title('Top 5 Design and Arts')
plt.xticks(rotation=0)
plt.show()    

top_5_jobs_HMH = data_task1.loc[data_task1['Category'] == 'HMH']
top_5_jobs_HMH = top_5_jobs_HMH.groupby('Job')['Purchase Price'].sum().reset_index(name='Total')
top_5_jobs_HMH = top_5_jobs_HMH.sort_values(by='Total', ascending=False).head(5)
top_5_jobs_HMH = top_5_jobs_HMH.reset_index().drop(columns='index')
#print(top_5_jobs_HMH)    

top_5_jobs_HMH.plot(x='Job', y='Total', figsize=(15, 7), kind='bar')
plt.xlabel('Job')
plt.ylabel('Total Purchase Price')
plt.title('Top 5 Health and Mental Health')
plt.xticks(rotation=0)
plt.show()    


top_5_jobs_TE = data_task1.loc[data_task1['Category'] == 'TE']
top_5_jobs_TE = top_5_jobs_TE.groupby('Job')['Purchase Price'].sum().reset_index(name='Total')
top_5_jobs_TE = top_5_jobs_TE.sort_values(by='Total', ascending=False).head(5)
top_5_jobs_TE = top_5_jobs_TE.reset_index().drop(columns='index')
#print(top_5_jobs_TE)    

top_5_jobs_TE.plot(x='Job', y='Total', figsize=(15, 7), kind='bar')
plt.xlabel('Job')
plt.ylabel('Total Purchase Price')
plt.title('Top 5 Technology and Engineering')
plt.xticks(rotation=0)
plt.show()    


top_5_jobs_SR = data_task1.loc[data_task1['Category'] == 'SR']
top_5_jobs_SR = top_5_jobs_SR.groupby('Job')['Purchase Price'].sum().reset_index(name='Total')
top_5_jobs_SR = top_5_jobs_SR.sort_values(by='Total', ascending=False).head(5)
top_5_jobs_SR = top_5_jobs_SR.reset_index().drop(columns='index')
#print(top_5_jobs_SR)  

top_5_jobs_SR.plot(x='Job', y='Total', figsize=(15, 7), kind='bar')
plt.xlabel('Job')
plt.ylabel('Total Purchase Price')
plt.title('Top 5 Science and Research')
plt.xticks(rotation=0)
plt.show()    

    

# top_5_jobs.plot(x='Job', y='Total', figsize=(15, 7), kind='bar')
# plt.xlabel('Job')
# plt.ylabel('Purchase Price')
# plt.xticks(rotation=0)
# plt.show()


fig = plt.figure(figsize=(8,8))
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)
# ax5 = fig.add_subplot(225)

#ax1 = plt.subplot2grid((2,3),(0,1))
#ax1.plot(top_5_jobs_FA['Job'],top_5_jobs_FA['Total'])