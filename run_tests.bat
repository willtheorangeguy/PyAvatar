@echo off
REM Test runner script with coverage reporting for Windows

echo ===================================
echo PyAvatar Test Suite Runner
echo ===================================
echo.

REM Run tests with coverage
echo Running tests with coverage...
pytest --cov=. --cov-report=term-missing --cov-report=html --cov-report=xml -v

REM Display summary
echo.
echo ===================================
echo Test Summary
echo ===================================
echo.
echo Coverage reports generated:
echo   - Terminal: See above
echo   - HTML: htmlcov\index.html
echo   - XML: coverage.xml
echo.
echo To view HTML coverage report:
echo   python -m http.server --directory htmlcov
echo.
pause
