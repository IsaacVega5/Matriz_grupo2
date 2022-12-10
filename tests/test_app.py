import unittest
import numpy as np

from app.app import *

class test_calculadora(unittest.TestCase):
    def test_transpose(self):
        x=np.array([[1,4,7],[2,5,8],[3,6,9]])
        result = transpose_np(x)
        correcto = np.array([[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(result.tolist(), correcto.tolist(), "El resultado debería ser [1, 2, 3] [4, 5, 6] [7, 8, 9]")


if __name__ == "__main__":
    unittest.main()