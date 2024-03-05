import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define the objective function
def objective_function(x, P, q):
    return 0.5 * np.dot(x.T, np.dot(P, x)) + np.dot(q.T, x)

# Define the constraints
def inequality_constraints(x, G, h):
    return np.all(np.dot(G, x) <= h)

def equality_constraints(x, A, b):
    return np.all(np.dot(A, x) == b)


def problem1():
    P = 2*np.eye(2) 
    q = np.array([-2,-5])
    G = -np.array([[1,-2],[-1,-2],[-1,2],[1,0],[0,1]])
    h = np.array([2,6,2,0,0])
    # Gx <= h
    # min 1/2 x^T P x + q^T x
    return P, q, G, h

def contourplot(P,q,G,h, A=np.zeros((2,2)), b=np.zeros(2), lb = np.array([0,0]), ub = np.array([np.inf,np.inf])):

    X1 = np.linspace(0,10,100)
    X2 = np.linspace(0,10,100)
    X1, X2 = np.meshgrid(X1,X2)

    Z = np.zeros_like(X1)

    # Calculate the objective function value for each x
    for i in range(X1.shape[0]):
        for j in range(X1.shape[1]):
            x = np.array([X1[i, j], X2[i, j]])
            Z[i, j] = objective_function(x, P, q)



    contour = plt.contourf(X1, X2, Z, levels=50, cmap='viridis')

    feasible_points = []
    for i in range(X1.shape[0]):
        for j in range(X1.shape[1]):
            x = np.array([X1[i, j], X2[i, j]])
            if (inequality_constraints(x, G, h) and
                equality_constraints(x, A, b) and
                np.all(x >= lb) and np.all(x <= ub)):
                feasible_points.append(x)
    feasible_points = np.array(feasible_points)

    # If we have feasible points, plot the feasible region
    if feasible_points.size:
        plt.scatter(feasible_points[:, 0], feasible_points[:, 1], color='red', s=1,label='Feasible Points')
    if feasible_points.size:
        objective_values = np.array([objective_function(point, P, q) for point in feasible_points])
        min_index = np.argmin(objective_values)
        min_point = feasible_points[min_index]
        plt.plot(min_point[0], min_point[1], 'x', markersize=10, color='white', label=f'Minimum Feasible Point: [x1,x2] = [{min_point[0]:.3f}, {min_point[1]:.3f}]')

    # Add some labels and a legend
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Contour plot with feasible region')
    plt.colorbar(contour, label='Objective function value')
    plt.legend()
    plt.show() 


def primal_active_set_algorithm(P, q, G, h, A, b, x0, tol=1e-6, max_iter=1000):
    # Initialize the active set
    active_set = np.zeros(G.shape[0], dtype=bool)
    # Initialize the solution
    x = x0
    # Initialize the iteration counter
    it = 0
    # Iterate
    while it < max_iter:
        # Increment the iteration counter
        it += 1
        # Compute the gradient
        grad = np.dot(P, x) + q
        # Compute the active set
        active_set = np.isclose(np.dot(G, x), h, atol=tol)
        # Compute the active gradient
        grad_a = grad + np.dot(G[active_set].T, np.dot(np.linalg.inv(np.dot(G[active_set], G[active_set].T)), np.dot(G[active_set], grad)))
        # Check for optimality
        if np.all(grad_a < tol):
            return x
        # Compute the search direction
        d = -grad_a
        # Compute the step length
        alpha = np.inf
        for i in range(G.shape[0]):
            if not active_set[i] and np.dot(G[i], d) > 0:
                alpha = min(alpha, (h[i] - np.dot(G[i], x)) / np.dot(G[i], d))
        # Update the solution
        x = x + alpha * d
    return x

if __name__ == "__main__":
    P, q, G, h = problem1()
    contourplot(P,q,G,h)
    x0 = np.array([0, 0])
    x = primal_active_set_algorithm(P, q, G, h, np.zeros((2,2)), np.zeros(2), x0)
    print(x)
