import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Sphere where rho = 1 and phi ranges from 0 to pi/3
theta = np.linspace(0, 2 * np.pi, 500)  # Increased number of points
phi = np.linspace(0, np.pi / 3, 500)  # Increased number of points
theta, phi = np.meshgrid(theta, phi)

rho1 = 1  # Fixed radius

# Convert spherical to Cartesian for updated phi range (sphere)
x1 = rho1 * np.sin(phi) * np.cos(theta)
y1 = rho1 * np.sin(phi) * np.sin(theta)
z1 = rho1 * np.cos(phi)

# 2. Cone where phi = pi/3 (fixed polar angle)
phi2 = np.pi / 3  # Fixed polar angle for the cone

# Varying rho and theta
rho2 = np.linspace(0, 1, 500)  # Increased number of points
theta2 = np.linspace(0, 2 * np.pi, 500)  # Increased number of points
theta2, rho2 = np.meshgrid(theta2, rho2)

# Convert spherical to Cartesian for phi = pi/3 (cone)
x2 = rho2 * np.sin(phi2) * np.cos(theta2)
y2 = rho2 * np.sin(phi2) * np.sin(theta2)
z2 = rho2 * np.cos(phi2)

# Plot both surfaces on the same axes with the color #cde4d5
ax.plot_surface(x1, y1, z1, color='#ceefd7', alpha=0.5, rstride=3, cstride=3)  # Reduced stride for higher resolution
ax.plot_surface(x2, y2, z2, color='#ceefd7', alpha=0.5, rstride=3, cstride=3)  # Reduced stride for higher resolution

# 3. Add the z-axis line
ax.plot([0, 0], [0, 0], [1, 1.2], color='black', lw=2)
ax.plot([0, 0], [0, 0], [0, 1], color='black', lw=2, linestyle=':')
ax.plot([0, 0], [0, 1.2], [0, 0], color='black', lw=2)
ax.plot([0, 1.2], [0, 0], [0, 0], color='black', lw=2)
# 4. Add the intersection circle (where sphere meets cone)
intersection_radius = np.sin(phi2)  # Radius of the circle at intersection
intersection_z = np.cos(phi2)  # Z-coordinate of the intersection
circle_theta = np.linspace(0, 2 * np.pi, 500)

circle_x = intersection_radius * np.cos(circle_theta)
circle_y = intersection_radius * np.sin(circle_theta)
circle_z = np.full_like(circle_x, intersection_z)  # Z-coordinate is constant

ax.plot(circle_x, circle_y, circle_z, color='#00abed', lw=2, label='Intersection Circle')  # Circle in black

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set aspect ratio (equal scaling)
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio for x, y, z

# Change the viewing angle (elevation and azimuth)
ax.view_init(elev=10, azim=45)  # Example: Elevation 30 degrees, Azimuth 60 degrees

# Increase the x and y limits
ax.set_xlim([-0.6, 0.6])  # Increase x limits
ax.set_ylim([-0.6, 0.6])  # Increase y limits
ax.set_axis_off()
# Add legend
ax.legend()

# Show the plot
plt.show()
