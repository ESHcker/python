import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

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
            
    

if __name__ == "__main__":
    print("Demo of the package:") 
    arr1 = np.array([1,2,3])
    arr2 = np.array([1,2,3])
    print(f"Add of matrices -> first matriz:{arr1}, second matriz:{arr2} | Result: {add_matrices(arr1, arr2)}")