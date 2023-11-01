# How does purchase depend on ‘CC’ provider and time of purchase ‘AM or PM’?
import os
import pandas as pd 
import matplotlib.pyplot as plt
from Pre_processes import data_task5

# ['CC Provider', 'AM or PM', 'Purchase Price']

cards = data_task5.groupby('CC Provider')['Purchase Price'].count().rename('Purchase Frequency')
cards = cards.sort_values(ascending=False)
cards = cards.reset_index()


cards_time = data_task5.groupby(['CC Provider', 'AM or PM'])['Purchase Price'].count().rename('Purchase Frequency')
cards_time = cards_time.sort_values(ascending=False)
cards_time = cards_time.reset_index()

print(cards)

print(cards_time)
