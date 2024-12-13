import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define r and theta for cylindrical coordinates
r = np.linspace(0, 1, 200)  # More points for smoother plots
theta = np.linspace(0, 2 * np.pi, 200)
R, Theta = np.meshgrid(r, theta)

# Define the z bounds
Z1 = R  # Lower bound: z = r
Z2 = np.sqrt(2 - R**2)  # Upper bound: z = sqrt(2 - r^2)

# Convert cylindrical to Cartesian coordinates
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Create the figure and 3D axis
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the lower surface (z = r)
lower_surface = ax.plot_surface(
    X, Y, Z1, 
    alpha=0.6,  # Transparency
    cmap="plasma",  # Gradient color map
    edgecolor="none",
    label="z = r"
)

# Plot the upper surface (z = sqrt(2 - r^2))
upper_surface = ax.plot_surface(
    X, Y, Z2, 
    alpha=0.6,  # Transparency
    cmap="plasma",  # Gradient color map
    edgecolor="none",
    label="z = sqrt(2 - r^2)"
)

# Add contour lines for better perspective
ax.contour(X, Y, Z2, zdir='z', offset=0, cmap="plasma", linewidths=1)

# Add color bars for each surface
fig.colorbar(lower_surface, ax=ax, shrink=0.5, aspect=10, label="z = r")
fig.colorbar(upper_surface, ax=ax, shrink=0.5, aspect=10, label="z = sqrt(2 - r^2)")

# Styling for the axes
ax.set_title("Prettier Volume Bounded by $z = r$ and $z = \\sqrt{2 - r^2}$", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("X-axis", fontsize=12, labelpad=10)
ax.set_ylabel("Y-axis", fontsize=12, labelpad=10)
ax.set_zlabel("Z-axis", fontsize=12, labelpad=10)
ax.tick_params(axis='both', which='major', labelsize=10)

# Set axis limits for better proportions
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 1.5])

# Adjust the viewing angle
ax.view_init(elev=15, azim=30)  # Elevation (height), Azimuth (rotation)

# Add a legend manually
ax.text2D(0.1, 0.9, "Lower Surface: $z = r$\nUpper Surface: $z = \\sqrt{2 - r^2}$", 
          transform=ax.transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Display the plot
plt.tight_layout()
plt.show()
