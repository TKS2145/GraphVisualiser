import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Sample data
categories = ['Strength', 'Speed', 'Intelligence', 'Skills', 'Energy']

N = len(categories)

# Normalize data to 0-1 range
data1 = [80, 60, 90, 70, 50]  # Group A
data2 = [50, 90, 40, 80, 70]  # Group B

# Convert to angles (0 to 2π)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]  # Complete the circle

# Add final data point to close the polygon
data1 += data1[:1]
data2 += data2[:1]

# Create plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot data
ax.plot(angles, data1, 'o-', linewidth=3, label='Group A', color='blue')
ax.fill(angles, data1, alpha=0.25, color='blue')
ax.plot(angles, data2, 'o-', linewidth=3, label='Group B', color='red')
ax.fill(angles, data2, alpha=0.25, color='red')

# Customize
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_ylim(0, 100)
ax.set_title('Radar Chart Comparison\n(Group A vs Group B)', size=16, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
ax.grid(True)

plt.tight_layout()
plt.show()
