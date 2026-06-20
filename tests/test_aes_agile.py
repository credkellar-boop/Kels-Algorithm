import unittest
from src.crypto.aes_agile import AgileSymmetricCipher

class TestAgileCipher(unittest.TestCase):
    def test_512_bit_generation(self):
        key = AgileSymmetricCipher.generate_grover_resistant_key(512)
        self.assertEqual(len(key), 64) # 64 bytes = 512 bits
