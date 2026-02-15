import matplotlib.pyplot as plt
from Globals import DataList
from collections import Counter
import numpy as np

def plotgraph(x = [], y = []):

    print("Processing graph")

    ''' 
    print()        
    print("List of x coordinates is" , x)
    print()
    print("List of y coordinates is" , y)
    '''

    # Count occurrences of each (x, y) pair
    
    point_counts = Counter(zip(x, y))

    # Assign sizes based on overlap count (e.g., scale by 100 for visibility)
    sizes = [100 * count for point, count in point_counts.items()]
    x_coords = [point[0] for point in point_counts.keys()]
    y_coords = [point[1] for point in point_counts.keys()]

    # Plot scatter with varying sizes
    plt.scatter(x_coords, y_coords, s=sizes, alpha=0.6, c='blue')
    plt.xlabel('Importance')
    plt.ylabel('Performance')
    plt.title('Importance V/S Performance Graph')
    plt.grid(True)
    plt.show()


def radarplot(listlabel= []):

    labels=np.array(listlabel)
    markers = [0, 1, 2, 3, 4, 5]
    str_markers = ["0", "1", "2", "3", "4", "5"]

    # Calculate angles
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    values += values[:1]  # Close the loop
    angles = np.concatenate([angles, [angles[0]]])

    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    ax.plot(angles, values, linewidth=2, linestyle='solid', marker='o')
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_rlabel_position(0)
    plt.title("Radar Chart from List", pad=20)
    plt.show()