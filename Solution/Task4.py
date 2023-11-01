# What are the patterns, if any, on the purchases based on Location (State) and time of purchase (AM or PM)?
import os
import pandas as pd 
import matplotlib.pyplot as plt
from Pre_processes import data_task4

# ['State', 'Region', 'AM or PM', 'Purchase Price']

region = data_task4.groupby(['Region'])['Purchase Price'].count()
region = region.sort_values(ascending=False)
region = region.reset_index()

region_time = data_task4.groupby(['Region', 'AM or PM'])['Purchase Price'].count()
region_time = region_time.sort_values(ascending=False)
region_time = region_time.reset_index()

print(region)

print(region_time)