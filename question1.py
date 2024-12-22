import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 500)
x = np.sin(2 * t)
y = np.sin(3 * t)

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_facecolor('white')
ax.xaxis.set_label_position('top')
ax.set_xlabel(r'$\mathscr{y}$', labelpad=10)
ax.yaxis.set_label_position('right')
ax.set_ylabel(r'$\mathscr{x}$', labelpad=10, rotation=0)
ax.plot(x, y, label="x=sin2t \n y=sin3t", color='#00abed')

ax.text(0, 1, '1', color='black', fontsize=10, ha='left', va='bottom')   # Top
ax.text(0, -1, '-1', color='black', fontsize=10, ha='left', va='top')    # Bottom
ax.text(1, 0, '1', color='black', fontsize=10, ha='left', va='bottom')   # Right
ax.text(-1, 0, '-1', color='black', fontsize=10, ha='right', va='bottom')  # Left

ax.legend()
plt.show()
