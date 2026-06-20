import unittest
import numpy as np
from src.crypto.lattice import LatticeEngine

class TestLatticeNoise(unittest.TestCase):
    def test_parameter_dimensions(self):
        engine = LatticeEngine(rank=8)
        params = engine.generate_parameter_matrix()
        self.assertEqual(np.array(params["public_key"]["A"]).shape, (8, 8))
      
