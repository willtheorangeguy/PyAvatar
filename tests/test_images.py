"""Tests for PyAvatar/images.py module."""

# pylint: disable=import-error, wrong-import-position

import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "PyAvatar"
    ),
)


class TestImagesModule(unittest.TestCase):
    """Test the images module."""

    def test_module_imports(self):
        """Test that the images module can be imported."""
        try:
            import images

            self.assertTrue(True)
        except ImportError:
            self.fail("images module could not be imported")

    def test_module_docstring(self):
        """Test that the images module has proper documentation."""
        import images

        self.assertIsNotNone(images.__doc__)
        self.assertIn("avatar", images.__doc__.lower())


if __name__ == "__main__":
    unittest.main()
