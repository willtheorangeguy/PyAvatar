"""Pytest configuration and shared fixtures."""
# pylint: disable=import-error

import sys
import os
import pytest
from unittest.mock import MagicMock, Mock

# Create a more robust tkinter mock
class MockTkinter:
    """Mock tkinter module."""
    
    class MockWidget:
        """Base mock widget."""
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            
        def pack(self, *args, **kwargs):
            """Mock pack."""
            pass
            
        def grid(self, *args, **kwargs):
            """Mock grid."""
            pass
            
        def bind(self, *args, **kwargs):
            """Mock bind."""
            pass
    
    class Tk(MockWidget):
        """Mock Tk."""
        def title(self, text):
            """Mock title."""
            self._title = text
            
        def mainloop(self):
            """Mock mainloop."""
            pass
    
    class Frame(MockWidget):
        """Mock Frame."""
        pass
    
    class Label(MockWidget):
        """Mock Label."""
        pass
    
    class PhotoImage:
        """Mock PhotoImage."""
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
    
    TOP = 'top'
    BOTTOM = 'bottom'

# Mock tkinter before any imports
sys.modules['tkinter'] = MockTkinter()

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_tk_window():
    """Fixture for mocked Tkinter window."""
    mock_window = MagicMock()
    mock_window.title = MagicMock()
    mock_window.mainloop = MagicMock()
    mock_window.grid = MagicMock()
    return mock_window


@pytest.fixture
def mock_photo_image():
    """Fixture for mocked PhotoImage."""
    mock_image = MagicMock()
    return mock_image


@pytest.fixture
def mock_label():
    """Fixture for mocked Label widget."""
    mock_lbl = MagicMock()
    mock_lbl.pack = MagicMock()
    mock_lbl.grid = MagicMock()
    mock_lbl.bind = MagicMock()
    return mock_lbl


@pytest.fixture
def mock_frame():
    """Fixture for mocked Frame widget."""
    mock_frm = MagicMock()
    mock_frm.grid = MagicMock()
    mock_frm.pack = MagicMock()
    return mock_frm
