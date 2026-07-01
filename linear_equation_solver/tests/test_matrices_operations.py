import matrices_operations as solver
import numpy as np

def test_add_matrices():
    #Normal cases
    assert np.array_equal(solver.add_matrices(np.array([11,22,34,58]), np.array([10,23,47,71])), np.array([21,45,81,129])) == True
    assert np.array_equal(solver.add_matrices(np.array([[1,2,3], [2,4,5]]), np.array([[1,2,3], [5,6,7]])), np.array([[2,4,6], [7,10,12]])) == True

    #Limit cases
    assert np.array_equal(solver.add_matrices(np.array([]), np.array([])), np.array([])) == True
    assert np.array_equal(solver.add_matrices(np.array([1]), np.array([])), np.array([])) == True

def test_subtract_matrices():
    #Normal cases
    assert np.array_equal(solver.subtract_matrices(np.array([11,22,34,58]), np.array([10,23,47,71])), np.array([1,-1,-13,-13])) == True
    assert np.array_equal(solver.subtract_matrices(np.array([[1,2,3], [2,4,5]]), np.array([[1,2,3], [5,6,7]])), np.array([[0,0,0], [-3,-2,-2]])) == True

    #Limit cases
    assert np.array_equal(solver.subtract_matrices(np.array([]), np.array([])), np.array([])) == True
    assert np.array_equal(solver.subtract_matrices(np.array([1]), np.array([])), np.array([])) == True

def test_multiplication_matrices():
    #Normal cases
    assert np.array_equal(solver.multiplication_matrices(np.array([11,22,34,58]), np.array([10,23,47,71])), np.array([110,506,1598,4118])) == True
    assert np.array_equal(solver.multiplication_matrices(np.array([[1,2,3], [2,4,5]]), np.array([[1,2,3], [5,6,7]])), np.array([[1,4,9], [10,24,35]])) == True

    #Limit cases
    assert np.array_equal(solver.multiplication_matrices(np.array([]), np.array([])), np.array([])) == True
    assert np.array_equal(solver.multiplication_matrices(np.array([1]), np.array([])), np.array([])) == True

def test_invert_matrix():
    #Normal cases
    assert np.array_equal(solver.invert_matrix(np.array([[1,3], [2,7]])), np.array([[7,-3],[-2,1]])) == True
    assert solver.invert_matrix(np.array([[4,5,-1], [-1,3,2], [3,8,1]])) == "Cant be inverted"

    #Limit cases
    assert solver.invert_matrix(np.array([])) == "Cant be inverted"

def test_eigenvalue_matrix():
    #Normal cases
    assert np.allclose(solver.eigenvalue_matrix(np.array([[1,3], [2,7]])), np.array([0.12701665, 7.87298335])) == True
    assert solver.eigenvalue_matrix(np.array([[4,5,-1], [-1,3,2]])) == "Must be a square"

    #Limit cases
    assert solver.eigenvalue_matrix(np.array([])) == "Must be a square"




  
    



