import numpy as np
import matplotlib.pyplot as plt

# Create a range of 't' values (parameter for the curve)
# t determines the shape of the curve
t = np.linspace(0, 2 * np.pi, 1000)  # 1000 points between 0 and 2π for smoothness

# Define x and y using the parametric equations
x = np.sin(2 * t)  # x-coordinate is sin(2t)
y = np.sin(3 * t)  # y-coordinate is sin(3t)

# Create the plot
plt.figure(figsize=(8, 8))  # Set the figure size to be square for better proportions

# Plot the parametric curve
plt.plot(x, y, color="purple", label=r"$x = \sin(2t), y = \sin(3t)$")

# Add labels and title
plt.title(r"Parametric Curve: $x = \sin(2t)$, $y = \sin(3t)$", fontsize=14)  # Use raw string for LaTeX
plt.xlabel("x-axis", fontsize=12)
plt.ylabel("y-axis", fontsize=12)

# Add a grid for better visualization
plt.grid(True, linestyle="--", alpha=0.7)

# Add a legend
plt.legend()

# Set an equal aspect ratio for a non-distorted plot
plt.axis("equal")

# Display the plot
plt.show()
