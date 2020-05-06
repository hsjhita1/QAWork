import pytest
from Code import PoliteProgram

def test_func():
    assert PoliteProgram.polite("John", "Doe") == "Hello John Doe"