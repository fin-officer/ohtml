import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before each test
    yield
    # Code that will run after each test
    pass
