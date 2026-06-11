# test_blockring.py
"""
Tests for BlockRing module.
"""

import unittest
from blockring import BlockRing

class TestBlockRing(unittest.TestCase):
    """Test cases for BlockRing class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockRing()
        self.assertIsInstance(instance, BlockRing)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockRing()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
