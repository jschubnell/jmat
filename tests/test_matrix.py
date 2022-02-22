import pytest
from jmat.matrix import Matrix

def test_matrix_constructor():
    a = Matrix(2, 3, [98, 54, 69,81, 47, 19])
    assert a.i == 2
    assert a.j == 3
    assert a.values == [98, 54, 69,81, 47, 19]

def test_matrix_addition_1_succesfull_case_2x3_plus_2x3():
    a = Matrix(2, 3, [98, 54, 69,81, 47, 19])
    b = Matrix(2, 3, [26, 69, 13,99, 17, 61])
    c = a + b
    assert c.values == [124, 123, 82, 180, 64, 80]

def test_matrix_addition_2_fail_case_2x3_plus_2x5():
    a = Matrix(2, 3, [98, 54, 69,81, 47, 19])
    b = Matrix(2, 5, [35 ,93 ,32 ,18 ,26, 53 ,47 ,76 ,70 ,2])
    with pytest.raises(AssertionError):
        c = a + b

def test_matrix_subtraction_1_successfull_case_2x2_minus_2x2():
    a = Matrix(2, 2, [99 ,47, 29 ,16])
    b = Matrix(2, 2, [16 ,22, 72 ,68])
    c = a - b
    assert c.values == [83 ,25, -43 ,-52]

def test_matrix_subtraction_2_fail_case_2x2_minus_2x4():
    a = Matrix(2, 2, [99 ,47, 29 ,16])
    b = Matrix(2, 4 , [16 ,22, 72 ,68, 47 ,76 ,70 ,2])
    with pytest.raises(AssertionError):
        c = a - b

def test_multiplication_1_succesfull_case_4x5_times_5x2():
    a = Matrix(4, 5, [45 ,40 ,75 ,50 ,55, 49 ,12 ,4 ,49 ,67, 78 ,23 ,2 ,47 ,76, 31 ,43 ,63 ,100 ,38])
    b = Matrix(5, 2, [30 ,71, 41 ,64, 42 ,36, 15 ,90, 28 ,60])
    c = a*b
    assert c.values == [8430 ,16255, 4741 ,12821, 6200 ,15872, 7903 ,18501]

def test_multiplication_2_fail_case_4x2_times_5x2():
    a = Matrix(4, 2, [45 ,40 ,75 ,50 ,55, 49 ,12 ,4])
    b = Matrix(5, 2, [30 ,71, 41 ,64, 42 ,36, 15 ,90, 28 ,60])
    with pytest.raises(AssertionError):
        c = a*b

def test_transpose_1_successfull_case_3x7():
    a = Matrix(3, 7, [98 ,25 ,38 ,56 ,74 ,20 ,55, 37 ,94 ,58 ,38 ,48 ,100 ,73, 76 ,62 ,11 ,85 ,77 ,79 ,21])
    b = a.transpose()
    assert b.values == [98 ,37 ,76, 25 ,94 ,62, 38 ,58 ,11, 56 ,38 ,85, 74 ,48 ,77, 20 ,100 ,79, 55 ,73 ,21]

def test_repr_1():
    a = Matrix(2, 2, [99 ,47, 29 ,16])
    assert repr(a) == "\n|99  47|\n|29  16|\n\nMatrix Dimensions: 2 x 2"

def test_repr_2():
    a = Matrix(3, 7, [98 ,25 ,38 ,56 ,74 ,20 ,55, 37 ,94 ,58 ,38 ,48 ,100 ,73, 76 ,62 ,11 ,85 ,77 ,79 ,21])
    assert repr(a) == "\n|98  25  38  56  74  20  55|\n|37  94  58  38  48  100  73|\n|76  62  11  85  77  79  21|\n\nMatrix Dimensions: 3 x 7"