import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(-2.39 * np.pi, np.pi * 2.39, 500)
r = theta

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta + (r < 0) * np.pi, np.abs(r), color='#00abed')

ax.set_axis_off()

# Draw axis lines
ax.plot([0, 0], [0,7.5], color='black', lw=1)  # Vertical line at theta = 0
ax.plot([np.pi, np.pi], [0, 7.5], color='black', lw=1)  # Vertical line at theta = pi
ax.plot([np.pi/2, np.pi/2], [0, 7.5], color='black', lw=1)  # Horizontal line at theta = pi/2
ax.plot([3*np.pi/2, 3*np.pi/2], [0, 7.5], color='black', lw=1)  # Horizontal line at theta = 3pi/2

# Add labels at specific angles
ax.text(0, 7.7, r'$\mathscr{x}$', horizontalalignment='center', verticalalignment='bottom', fontsize=12)  # Y label (top)
ax.text(np.pi/2, 7.7, r'$\mathscr{y}$', horizontalalignment='center', verticalalignment='bottom', fontsize=12)  # X label (right)
3

plt.show()
