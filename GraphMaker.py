import matplotlib.pyplot as plt
from Globals import DataList


def plotgraph():

    print("Processing graph")

    TempList = list(DataList)
    NewDataList = []

    for x in TempList: #for each list of collected data
        print(type(x))
        print(x)
        print()
        for y in x: #for each item in the list
            print()
            print(y)
            print()

            try:
                int(y) #Checking if interger
            except:
                try:

                    x.remove(y) #if not integer then remove from list
                except:

                    x = None #I have no idea what is happening now

        NewDataList.append(x)

    i = 0
    x =[]
    y = []

    for Data in NewDataList:
        
        if i % 2 == 0:
            x = Data
        else:
            y = Data
        
        i*=1
        
    print(x)
    print(y)

    plt.scatter(x, y)
    plt.show()
