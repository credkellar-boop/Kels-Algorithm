import unittest
from crypto.binding import NonLinearBinder

class TestCryptoBinding(unittest.TestCase):
    def test_successful_binding(self):
        classical = b"super_secret_classical_key_ecc_x25519"
        quantum = b"super_secret_quantum_lattice_key_ml_kem_1024"
        
        # Derive a combined master bound key
        key_1 = NonLinearBinder.derive_bound_key(classical, quantum)
        key_2 = NonLinearBinder.derive_bound_key(classical, quantum, salt=b"fixed_salt_for_deterministic_test")
        
        self.assertEqual(len(key_1), 64)  # Ensure a full 512-bit key is generated
        self.assertEqual(len(key_2), 64)

    def test_tamper_resilience(self):
        classical = b"classical_secret"
        quantum = b"quantum_secret"
        
        # Altering a single bit of either component must yield a completely chaotic key
        key_original = NonLinearBinder.derive_bound_key(classical, quantum, salt=b"static_salt")
        key_tampered = NonLinearBinder.derive_bound_key(classical, b"quantum_secreT", salt=b"static_salt")
        
        self.assertNotEqual(key_original, key_tampered)

if __name__ == '__main__':
    unittest.main()
  
