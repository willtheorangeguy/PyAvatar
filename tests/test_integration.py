# pylint: skip-file

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestIntegration(unittest.TestCase):
    """Integration tests for the full application."""

    def test_main_module_imports(self):
        """Test that main module can be imported."""
        try:
            import main

            self.assertTrue(True)
        except ImportError:
            self.fail("main module could not be imported")

    def test_avatars_function_exists(self):
        """Test that avatars function exists in main module."""
        import main

        self.assertTrue(hasattr(main, "avatars"))
        self.assertTrue(callable(main.avatars))

    @patch("main.Tk")
    @patch("main.PhotoImage")
    def test_application_initialization(self, mock_photo, mock_tk):
        """Test that application can be initialized."""
        import main

        # Setup mocks
        mock_window = MagicMock()
        mock_tk.return_value = mock_window
        mock_window.mainloop = MagicMock()

        # Test initialization
        try:
            main.avatars()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Application initialization failed: {e}")

    def test_package_structure(self):
        """Test that package has proper structure."""
        import main

        # Check for required attributes
        self.assertTrue(hasattr(main, "row_count"))
        self.assertTrue(hasattr(main, "column_count"))
        self.assertTrue(hasattr(main, "avatars"))

    def test_pyavatar_package_imports(self):
        """Test that PyAvatar package modules can be imported."""
        try:
            sys.path.insert(
                0,
                os.path.join(
                    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "PyAvatar",
                ),
            )
            import images
            import links

            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"PyAvatar package modules could not be imported: {e}")


if __name__ == "__main__":
    unittest.main()
