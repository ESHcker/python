import matrices_operations as solver
import numpy as np

def test_add_matrices():
    array_to_add1 = np.array([1,2,3])
    array_to_add2 = np.array([1,2,3])

    result = solver.add_matrices(array_to_add1, array_to_add2)
    correct_result = np.array([2,4,6])

    assert np.array_equal(result, correct_result) == True