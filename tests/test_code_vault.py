import unittest
from src.crypto.code_vault import GoppaVault

class TestGoppaVault(unittest.TestCase):
    def test_chaff_injection(self):
        vault = GoppaVault()
        encrypted = vault.encrypt_with_chaff(b"secret_archive_data")
        self.assertEqual(len(encrypted["chaff_layers"]), 5)
      
