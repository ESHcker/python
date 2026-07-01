import matrices_operations as solver
import numpy as np

def test_add_matrices():
    #Normal cases
    assert np.array_equal(solver.add_matrices(np.array([11,22,34,58]), np.array([10,23,47,71])), np.array([21,45,81,129])) == True
    assert np.array_equal(solver.add_matrices(np.array([1,2,3]), np.array([1,2,3])), np.array([2,4,6])) == True
    assert np.array_equal(solver.add_matrices(np.array([1,2]), np.array([1,2])), np.array([2,4])) == True
    assert np.array_equal(solver.add_matrices(np.array([1]), np.array([1])), np.array([2])) == True

    #Limit cases
    assert np.array_equal(solver.add_matrices(np.array([]), np.array([])), np.array([])) == True
    assert np.array_equal(solver.add_matrices(np.array([1]), np.array([])), np.array([])) == True
    



