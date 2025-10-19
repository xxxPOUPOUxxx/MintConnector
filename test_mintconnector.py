# test_mintconnector.py
"""
Tests for MintConnector module.
"""

import unittest
from mintconnector import MintConnector

class TestMintConnector(unittest.TestCase):
    """Test cases for MintConnector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintConnector()
        self.assertIsInstance(instance, MintConnector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintConnector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
