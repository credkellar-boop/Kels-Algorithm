import unittest
from src.defensive.ip_blacklist import LocalBlacklist

class TestBlacklist(unittest.TestCase):
    def test_ip_banning(self):
        blacklist = LocalBlacklist()
        blacklist.add_ip("10.0.0.99")
        self.assertTrue(blacklist.is_banned("10.0.0.99"))
      
