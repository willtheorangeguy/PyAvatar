# PyAvatar Test Suite

This document describes the comprehensive test suite for the PyAvatar project.

## Overview

The test suite provides comprehensive coverage of the PyAvatar codebase with 23 tests achieving 86% code coverage.

## Test Structure

The test suite is organized into the following test modules:

### `tests/test_avatars.py`
Tests for the main avatars functionality:
- Window creation and initialization
- Title label creation
- Account frame creation
- Link/webbrowser functionality
- Global variable initialization

### `tests/test_images.py`
Tests for the `PyAvatar/images.py` module:
- Module import validation
- Documentation verification

### `tests/test_links.py`
Tests for the `PyAvatar/links.py` module:
- Module import validation
- Documentation verification

### `tests/test_integration.py`
Integration tests for the full application:
- Main module imports
- Avatars function existence
- Application initialization
- Package structure validation
- PyAvatar package imports

### `tests/test_main_pytest.py`
Pytest-style tests for main.py:
- Window creation
- Mainloop execution
- Variable existence checks
- Function callability
- Webbrowser integration
- Module structure

### `tests/conftest.py`
Pytest configuration and shared fixtures:
- Tkinter mocking for headless testing
- Shared fixtures for tests

## Running Tests

### Run all tests:
```bash
pytest
```

### Run with verbose output:
```bash
pytest -v
```

### Run with coverage:
```bash
pytest --cov=. --cov-report=term-missing
```

### Run specific test file:
```bash
pytest tests/test_avatars.py
```

### Run specific test:
```bash
pytest tests/test_avatars.py::TestAvatarsFunction::test_avatars_window_creation
```

## GitHub Actions Integration

The test suite is integrated with GitHub Actions through `.github/workflows/pytest.yml`:

### Features:
- **Matrix Testing**: Tests run across multiple Python versions (3.9, 3.10, 3.11, 3.12)
- **Multi-OS Testing**: Tests run on Ubuntu, Windows, and macOS
- **Coverage Reporting**: Automatic coverage reports generated
- **Artifacts**: Coverage reports uploaded as GitHub Actions artifacts
- **Summary**: Coverage summary displayed in GitHub Actions summary

### Workflow Triggers:
- Push to any branch
- Pull requests

## Test Configuration

### `pytest.ini`
Configuration for pytest:
- Test discovery patterns
- Coverage settings
- Output formatting
- Test markers

### Test Markers
- `unit`: Unit tests
- `integration`: Integration tests  
- `slow`: Slow running tests

## Requirements

Test dependencies are listed in `requirements.txt`:
- `pytest`: Test framework
- `pytest-cov`: Coverage plugin
- `pytest-mock`: Mocking utilities

## Coverage Goals

Current coverage: 86%

Areas with high coverage:
- main.py: 94%
- test files: 82-100%

## Notes

- The test suite uses mocked tkinter to allow headless testing (no GUI required)
- Tests are designed to be fast and not require external dependencies
- Integration tests validate the full application flow
- Unit tests focus on individual components

## Contributing

When adding new features:
1. Write tests for new functionality
2. Ensure existing tests still pass
3. Aim to maintain or improve coverage percentage
4. Follow existing test patterns and naming conventions
