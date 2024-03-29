import numpy as np
def problem1(n, mu_bar, d0):

    P = 2*np.eye(n)
    q = -2*mu_bar * np.ones(n)
    b = np.zeros(n) 
    b[0] = -d0
    A = np.zeros((n,n))
    _help_array = np.zeros(n)
    _help_array[0] = -1
    _help_array[-1] = 1
    A[0,:] = _help_array 
    _help_array = np.zeros(n)
    _help_array[-1] = -1
    _help_array[-2] = -1
    _help_array[-3] = 1
    A[1,:] = _help_array
    for i in range(2,n):
        j = i-2
        A[i,j] = 1
        A[i,j+1] = -1

    return P, q, A, b

if __name__ == "__main__":
    P,q, A, b = problem1(5, 1, 1)
    #  Lagrange
    phi = lambda x: 0.5*x.T @ P @ x + q.T @ x
    g = lambda x: A @ x - b
    lagrange = lambda x, l: phi(x) + l.T @ g(x)
    # We must get the hessian of the lagrange function and show it is positive definite (sufficient)
    # At the point for which we have a local minima (neccesary) 
    print(A)
from langchain_community.llms import VLLM


    
