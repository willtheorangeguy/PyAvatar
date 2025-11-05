"""Tests for PyAvatar/links.py module."""

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


class TestLinksModule(unittest.TestCase):
    """Test the links module."""

    def test_module_imports(self):
        """Test that the links module can be imported."""
        try:
            import links

            self.assertTrue(True)
        except ImportError:
            self.fail("links module could not be imported")

    def test_module_docstring(self):
        """Test that the links module has proper documentation."""
        import links

        self.assertIsNotNone(links.__doc__)
        # Check for either 'link' or 'website' in docstring
        doc_lower = links.__doc__.lower()
        self.assertTrue(
            "link" in doc_lower or "website" in doc_lower or "avatar" in doc_lower
        )


if __name__ == "__main__":
    unittest.main()
