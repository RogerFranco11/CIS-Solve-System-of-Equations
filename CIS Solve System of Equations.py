# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

def solve_system_of_equations():
    # Coefficient matrix A
    A = np.array([[2, -1, 3],
                  [-1, 3, -1],
                  [4, -4, 3]])

    # Constant matrix B
    B = np.array([10, -1, 3])

    # Solve the system of equations using NumPy's linear algebra function
    X = np.linalg.solve(A, B)

    return X

# Call the function to get the solution
solution = solve_system_of_equations()

# Print the solution
print("Solution:")
print(f"x1 = {solution[0]}")
print(f"x2 = {solution[1]}")
print(f"x3 = {solution[2]}")


