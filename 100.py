import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# Define function for gradient descent
def gradient_descent(tangent_factor, learning_rate):
    return tangent_factor - learning_rate * np.sin(tangent_factor)

# Define function to animate tangent function with gradient descent
def update_3d(frame):
    time_step = np.linspace(0, 2*np.pi, 100)  # Time steps
    trajectory_x = np.sin(time_step) * np.cos(time_step)
    trajectory_y = np.sin(time_step) * np.sin(time_step)
    
    # Initialize tangent factor and learning rate
    tangent_factor = frame
    learning_rate = 0.1
    
    # Perform gradient descent for the tangent factor
    tangent_factor = gradient_descent(tangent_factor, learning_rate)
    
    # Bound the z-coordinate to be non-negative (perturbation at bottom half of curve)
    trajectory_z = -np.clip(np.tan(tangent_factor * time_step), 0, np.inf)
    
    ax.clear()
    ax.plot(trajectory_x, trajectory_y, trajectory_z)
    
    # Define coordinates for the micro-black hole containment field
    r = 1
    z = np.linspace(0, 4, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    Z, Theta = np.meshgrid(z, theta)
    X = r * np.cos(Theta)
    Y = r * np.sin(Theta)

    # Plot containment field
    ax.plot_surface(X, Y, Z, alpha=0.5)

    # Plot micro-black hole at the center
    ax.scatter(0, 0, 2, c='black', label='Micro-Black Hole')

    # Define funnel coordinates
    funnel_z = np.linspace(2, 0, 20)
    funnel_theta = np.linspace(0, 2*np.pi, 20)
    Funnel_Z, Funnel_Theta = np.meshgrid(funnel_z, funnel_theta)
    Funnel_R = 0.5 * Funnel_Z

    # Plot funnel 1
    Funnel_X = Funnel_R * np.cos(Funnel_Theta)
    Funnel_Y = Funnel_R * np.sin(Funnel_Theta)
    ax.plot_surface(Funnel_X, Funnel_Y, Funnel_Z, color='blue', alpha=0.5)

    # Plot funnel 2
    ax.plot_surface(-Funnel_X, -Funnel_Y, Funnel_Z, color='blue', alpha=0.5)

    # Set labels
    ax.set_xlabel('X (Distance)')
    ax.set_ylabel('Y (Distance)')
    ax.set_zlabel('Z (Distance)')
    ax.set_title('Combined Animation of Trajectory and Romulan Quantum Singularity Propulsion System')

# Animate
ani = FuncAnimation(fig, update_3d, frames=np.linspace(0, 2*np.pi, 100), interval=100)

plt.show()
