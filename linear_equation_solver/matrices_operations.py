import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
from numpy.linalg import eig

def add_matrices(matrix1, matrix2):  
    return matrix1 + matrix2

def subtract_matrices(matrix1, matrix2):
    return matrix1 - matrix2

def multiplication_matrices(matrix1, matrix2):
    return matrix1 * matrix2

def invert_matrix(matrix):
    try:
        return inv(matrix)
    except np.linalg.LinAlgError:
        return f"Cant be inverted"
            
def eigenvalue_matrix(matrix):
    try:
        return eig(matrix).eigenvalues
    except np.linalg.LinAlgError:
        return f"Must be a square"
    


if __name__ == "__main__":
    print("Demo of the package:") 
    arr1 = np.array([1,2,3])
    arr2 = np.array([1,2,3])
    print(f"Add of matrices -> first matriz:{arr1}, second matriz:{arr2} | Result: {add_matrices(arr1, arr2)}")
    arr3 = np.array([[1,3], [2,7]])
    print(f"eigenvalue:{eigenvalue_matrix(arr3)}")