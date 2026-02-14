import matplotlib.pyplot as plt
from Globals import DataList
#import plotly.graph_objects as go
from collections import Counter


def plotgraph():

    print("Processing graph")

    TempList = list(DataList)
    NewDataList = []


    for x in TempList: #for each list of collected data
        

        for y in x:

            try:
                NewDataList.append(int(y)) #Checking if interger adn adding to list of number
            except:
                continue

    print("New list of data is " , NewDataList)
    i = 0
    x =[]
    y = []

    for Data in NewDataList:
        
        if i % 2 == 0:
            x.append(Data)
        else:
            y.append(Data)
        
        i+=1
    '''
    print()        
    print("List od x coordinates is" , x)
    print()
    print("List of y coordinates is" , y)

    plt.scatter(x_coords, y_coords)
    plt.show()

    '''

    # Count occurrences of each (x, y) pair
    
    point_counts = Counter(zip(x, y))

    # Assign sizes based on overlap count (e.g., scale by 100 for visibility)
    sizes = [100 * count for point, count in point_counts.items()]
    x_coords = [point[0] for point in point_counts.keys()]
    y_coords = [point[1] for point in point_counts.keys()]

    # Plot scatter with varying sizes
    plt.scatter(x_coords, y_coords, s=sizes, alpha=0.6, c='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Importance V/S Performance Graph')
    plt.grid(True)
    plt.show()


    #ALternate graph 
'''
    fig = go.Figure(data=[go.Scatter(
    x, y,
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4
    )
    )])

    fig.show()

'''
