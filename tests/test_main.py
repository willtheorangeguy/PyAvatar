"""Test main.py."""
#pylint: disable=wrong-import-position, too-many-function-args

import sys
import os
import unittest
from tkinter import Tk, Frame, Label
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import avatars


class TestAccounts(unittest.TestCase):
    """Test the accounts function."""

    def setUp(self):
        """Set up the test environment."""
        self.window = Tk()
        self.name = "Test Name"
        self.hyperlink = "https://test.com"
        self.row_count = 0
        self.column_count = 0

    def test_avatars(self):
        """Test the avatars function."""
        with patch.object(Frame, "grid") as mock_grid:
            avatars(self.name, self.hyperlink)
            # Check if grid method was called
            self.assertTrue(mock_grid.called)

    def test_avatars_elements(self):
        """Test the avatars function for the correct elements."""
        avatars(self.name, self.hyperlink)
        # Check if the correct elements have been added
        self.assertEqual(len(self.window.children), 1)
        frame = next(iter(self.window.children.values()))
        self.assertIsInstance(frame, Frame)
        self.assertEqual(len(frame.children), 3)
        for widget in frame.children.values():
            self.assertIsInstance(widget, Label)


if __name__ == "__main__":
    unittest.main()
