from Globals import DataList


def extracting_points():

    TempList = list(DataList)
    NewDataList = []


    for x in TempList: #for each list of collected data
        

        for y in x:

            try:
                NewDataList.append(int(y)) #Checking if interger adn adding to list of number
            except:
                continue

    #print("New list of data is " , NewDataList) Testing Purposes
    
    i = 0
    x =[]
    y = []

    for Data in NewDataList:
        
        if i % 2 == 0:
            x.append(Data)
        else:
            y.append(Data)
        
        i+=1

    return x, y
