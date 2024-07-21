import matplotlib.pyplot as plt
import numpy as np

def plot_solution(solutions, basis_vectors=None):
    """Plots the solution set in R3 if it's a line or plane."""

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if basis_vectors is None:  # Unique solution (point)
        ax.scatter(*solutions, color='red', marker='o', label='Solution')
    else:  # Infinitely many solutions (line or plane)
        # Calculate points on the line/plane
        u = np.linspace(-5, 5, 100)  # Parameter
        U, _ = np.meshgrid(u, u)

        # Ensure basis_vectors has at least 3 rows
        if basis_vectors.shape[0] < 3:
            basis_vectors = np.vstack((basis_vectors, np.zeros((3-basis_vectors.shape[0], basis_vectors.shape[1]))))

        # Reshape basis vectors for broadcasting
        basis_vectors = basis_vectors.reshape(-1, 1, 1)

        # Calculate X, Y, Z coordinates for the surface
        X = solutions[0] + basis_vectors[0] * U
        Y = solutions[1] + basis_vectors[1] * U
        Z = solutions[2] + basis_vectors[2] * U

        # Plot the surface (line in this case)
        for i in range(basis_vectors.shape[1]):  # Plot each line
            ax.plot(X[:, i], Y[:, i], Z[:, i], alpha=0.5, label=f'Solution Set {i+1}')

    # Set plot limits and labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Solution Set')
    ax.legend()

    plt.show()