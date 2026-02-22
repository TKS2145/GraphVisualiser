import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from math import pi


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


def radarplot(listlabel= [], values =[]):

    labels = np.array(listlabel)

    # Calculate angles
    N = len(labels)

    # Convert to angles (0 to 2π)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # Complete the circle

    # Create polar subplot
    fig, ax = plt.subplots(figsize=(N, N), subplot_kw=dict(polar=True))

    # Add final data point to close the polygon
    values += values[:1]

    # Set the direction and offset
    ax.set_theta_offset(np.pi / 2)  # Start at top
    ax.set_theta_direction(-1)      # Clockwise

    # Create plot
    fig, ax = plt.subplots(figsize=(N, N), subplot_kw=dict(polar=True))


    # Plot data
    ax.plot(angles, values, 'o-', linewidth=3, label='Group A', color='blue')
    ax.fill(angles, values, alpha=0.25, color='blue')
    #ax.plot(angles, data2, 'o-', linewidth=3, label='Group B', color='red')
    #ax.fill(angles, data2, alpha=0.25, color='red')

    # Customize
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_ylim(0, 5)
    ax.set_title('Radar Chart Comparison\n(Group A vs Group B)', size=16, pad=1)
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))
    ax.grid(True)
   

    # Show the plot
    plt.tight_layout()
    plt.show()

