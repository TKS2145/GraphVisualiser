'''
import pandas as pd

data = pd.read_csv('Org Diagnostic.csv')

x = data.to_dict()

print(x)

'''

import csv
from Globals import DataList

def readfile():

    print("Reading from file")


    templist = []
    with open('Org Diagnostic.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for x in row:
                templist.append(x)
        DataList.append(templist)

