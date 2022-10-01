import unittest
import sys, os
from unittest.mock import patch, Mock

import builder

sys.path.append(os.getcwd())
from builder import *

class Furniture_Builder_Test(unittest.TestCase):
    @patch.object(builder.Furniture_Builder(), 'chair')
    def test_chair(self, mock_chair):
        mock_chair.return_value = None
        self.assertEqual(Furniture_Builder().chair(), None)
