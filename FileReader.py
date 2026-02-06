'''
import pandas as pd

data = pd.read_csv('Org Diagnostic.csv')

x = data.to_dict()

print(x)

'''

import csv

with open('Org Diagnostic.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)   
        print()
        

