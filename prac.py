import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter t
t = np.linspace(0, 4 * np.pi, 500)  # Covers two full turns of the helix

# Parametric equations
x = 2 * np.cos(t)
y = 2 * np.sin(t)
z = t

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the helix
ax.plot(x, y, z, label=r"$\mathbf{r}(t) = 2\cos t \mathbf{i} + 2\sin t \mathbf{j} + t \mathbf{k}$", color="blue")

# Add arrows for direction of increasing t
for i in range(0, len(t), 50):  # Add an arrow every 50 points
    ax.quiver(x[i], y[i], z[i], 
              -np.sin(t[i]), np.cos(t[i]), 1,  # Tangent vector components
              length=0.5, normalize=True, color="red")

# Labels and title
ax.set_title("Helix: Parametric Curve of $r(t)$", fontsize=14)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

# Set aspect ratio for better visualization
ax.set_box_aspect([2, 2, 4])

plt.show()
