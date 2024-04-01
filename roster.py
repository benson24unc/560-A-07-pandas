#https://goheels.com/sports/mens-basketball/roster
import pandas as pd


last_names = ['Lebo', 'Davis', 'Trimble']

data = pd.DataFrame(last_names, columns=['Last Name'])
print(data)