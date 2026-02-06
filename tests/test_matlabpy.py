import unittest
import numpy as np
from matlabpy import M, mat, zeros, ones, eye, rand, linspace, diag

class TestMatlabPy(unittest.TestCase):
    def test_matrix_construction(self):
        A = mat("1 2; 3 4")
        self.assertEqual(A.shape, (2, 2))
        self.assertEqual(A(1, 1), 1)
        self.assertEqual(A(2, 2), 4)

    def test_arithmetic(self):
        A = mat("1 2; 3 4")
        B = mat("5 6; 7 8")
        
        # Matrix multiplication
        C = A * B
        self.assertTrue(np.allclose(C.A, np.dot(A.A, B.A)))
        
        # Elementwise multiplication
        D = A.emul(B)
        self.assertTrue(np.allclose(D.A, A.A * B.A))
        
        # Power
        E = A ** 2
        self.assertTrue(np.allclose(E.A, np.linalg.matrix_power(A.A, 2)))

    def test_indexing(self):
        A = mat("1 2 3; 4 5 6")
        self.assertEqual(A(1, 1), 1)
        self.assertEqual(A(2, 3), 6)
        # Check 1-based indexing logic
        self.assertEqual(A(1, 2), 2)

    def test_concatenation(self):
        A = mat("1 2")
        B = mat("3 4")
        C = M.vcat(A, B)
        self.assertEqual(C.shape, (2, 2))
        self.assertEqual(C(1, 1), 1)
        self.assertEqual(C(2, 1), 3)

if __name__ == '__main__':
    unittest.main()
