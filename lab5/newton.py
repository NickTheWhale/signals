import numpy as np

W1, W2, W3 = 49, 400, 5500
# x = [a1, a2, a3]
# x = [ 0,  1,  2]
def gain(x, w0):
    A = (w0 * x[0]) / np.sqrt(W1**2 + w0**2)
    B = x[1] / np.sqrt(W2**2 + w0**2)
    C = x[2] / np.sqrt(W3**2 + w0**2)
    return A * B * C

# x = [a1, a2, a3]
# x = [ 0,  1,  2]
def d_a1_gain(x, w0):
    N = x[1] * x[2] * w0
    D = np.sqrt(W1**2 + w0**2) * np.sqrt(W2**2 + w0**2) * np.sqrt(W3**2 + w0**2)
    return N / D

def d_a2_gain(x, w0):
    N = x[0] * x[2] * w0
    D = np.sqrt(W1**2 + w0**2) * np.sqrt(W2**2 + w0**2) * np.sqrt(W3**2 + w0**2)
    return N / D

def d_a3_gain(x, w0):
    N = x[0] * x[1] * w0
    D = np.sqrt(W1**2 + w0**2) * np.sqrt(W2**2 + w0**2) * np.sqrt(W3**2 + w0**2)
    return N / D

# Define the non-linear system of equations as a function f(x) = 0
def f(x):
    # Define the system of equations here as a vector-valued function
    return np.array([gain(x, 1) - 0.1, gain(x, 10) - 1, gain(x, 150) - 5.01])

# Define the Jacobian matrix J(x)
def J(x):
    # Define the Jacobian matrix here using partial derivatives of the equations
    return np.array([[d_a1_gain(x, 1), d_a2_gain(x, 1), d_a3_gain(x, 1)],
                     [d_a1_gain(x, 10), d_a2_gain(x, 10), d_a3_gain(x, 10)],
                     [d_a1_gain(x, 150), d_a2_gain(x, 150), d_a3_gain(x, 150)]])

# Set the initial guess for the solution
x0 = np.array([0.0001, 50000, 50000])

# Set the maximum number of iterations and the desired tolerance
max_iter = 100
tolerance = 1e-6

# Iterate using the Newton-Raphson method until convergence
for i in range(max_iter):
    # Calculate the increment Δx
    print(J(x0))
    J_inv = np.linalg.inv(J(x0))
    fx = f(x0)
    dx = -J_inv.dot(fx)
    
    # Update the solution
    x = x0 + dx
    
    # Check for convergence
    if np.linalg.norm(x - x0) < tolerance:
        break
    
    # Update the initial guess
    x0 = x
    
# Print the solution and number of iterations
print("Solution:", x)
print("Number of iterations:", i+1)
