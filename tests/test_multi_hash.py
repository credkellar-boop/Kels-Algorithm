import unittest
from crypto.hashing import MultiHashChainer

class TestMultiHashChainer(unittest.TestCase):
    def test_hash_generation(self):
        data = b"transaction_data_block_001"
        salt = b"random_leaf_salt_value_256_bits"
        
        hash_output = MultiHashChainer.hash_leaf(data, salt)
        self.assertEqual(len(hash_output), 64)  # SHA-3-512 yields 64 bytes

    def test_node_combination(self):
        left = b"a" * 64
        right = b"b" * 64
        
        parent = MultiHashChainer.combine_nodes(left, right)
        self.assertEqual(len(parent), 64)

if __name__ == '__main__':
    unittest.main()
