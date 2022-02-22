import pytest
from jmat.matrix import Matrix

def test_matrix_addition_1_2x3_plus_2x3():
    a = Matrix(2, 3, [98, 54, 69,81, 47, 19])
    b = Matrix(2, 3, [26, 69, 13,99, 17, 61])
    c = a + b
    assert c.values == [124, 123, 82, 180, 64, 80]

def test_matrix_addition_2_2x3_plus_2x5():
    a = Matrix(2, 3, [98, 54, 69,81, 47, 19])
    b = Matrix(2, 5, [35 ,93 ,32 ,18 ,26, 53 ,47 ,76 ,70 ,2])
    with pytest.raises(AssertionError):
        c = a + b