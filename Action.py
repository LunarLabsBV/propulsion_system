import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the action function
def action(phi, g):
    # Define the potential energy term
    V = phi**2
    
    # Calculate the action
    S = 0.5 * np.sum(g * phi**2) - V
    
    return S

# Create a grid of phi and g values
phi_values = np.linspace(-5, 5, 100)
g_values = np.linspace(-5, 5, 100)
phi_grid, g_grid = np.meshgrid(phi_values, g_values)

# Calculate the action for each combination of phi and g
S_values = action(phi_grid, g_grid)

# Plot the action surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(phi_grid, g_grid, S_values, cmap='viridis')

# Set labels
ax.set_xlabel('$\Phi$')
ax.set_ylabel('$g_{\mu\nu}$')
ax.set_zlabel('Action')
ax.set_title('Action for the Romulan Quantum Singularity Propulsion System')

plt.show()
