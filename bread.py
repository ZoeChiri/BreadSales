import pandas as pd
import numpy as np
import random

# Prices dictionary

bread_prices = {
    "Challah": 4.5,
    "Pumpkin": 5,
    "Chocolate Chip": 4,
    "Cinnamon Bread": 3.5,
    "White Bread": 3,
    "Sourdough": 5.5
}

# Total revenue new column
df['Total Revenue'] = 0
for index, row in df.iterrows():
    total_revenue = 0
    for bread_type, quantity in row[['Challah', 'Pumpkin', 'Chocolate Chip', 'Cinnamon Bread', 'White Bread', 'Sourdough']].items():
        total_revenue += quantity * bread_prices[bread_type]
    df.loc[index, 'Total Revenue'] = total_revenue

total_revenue = df['Total Revenue'].sum()

df

# Total bread sold 
total_bread_sold = df[['Challah', 'Pumpkin', 'Chocolate Chip', 'Cinnamon Bread', 'White Bread', 'Sourdough']].sum()
print(total_bread_sold)

# Which bread generates the most revenue 
revenue_by_bread = {}
for bread_type in ['Challah', 'Pumpkin', 'Chocolate Chip', 'Cinnamon Bread', 'White Bread', 'Sourdough']:
  revenue_by_bread[bread_type] = (df[bread_type] * bread_prices[bread_type]).sum()

max_revenue_bread = max(revenue_by_bread, key=revenue_by_bread.get)
print(f"The bread that generates the most revenue is: {max_revenue_bread}")

# Which bread is the most popular
most_popular_bread_by_location = df.groupby('Farmers Market')[['Challah', 'Pumpkin', 'Chocolate Chip', 'Cinnamon Bread', 'White Bread', 'Sourdough']].sum().idxmax(axis=1)

print(most_popular_bread_by_location)

# Most popular bread per location per month
most_popular_bread_per_location_month = df.groupby(['Farmers Market', df.index.month])[[
    'Challah', 'Pumpkin', 'Chocolate Chip', 'Cinnamon Bread', 'White Bread', 'Sourdough'
]].sum().idxmax(axis=1)

print(most_popular_bread_per_location_month)

# Average bread sold per weekend
average_bread_sold = df[['Challah', 'Pumpkin', 'Chocolate Chip', 'Cinnamon Bread', 'White Bread', 'Sourdough']].mean().mean()
print(f"The average amount of bread sold per weekend is: {average_bread_sold:.2f}")


