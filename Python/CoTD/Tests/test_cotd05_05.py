import pytest
import math
from Code import CoTD05_05

def test_func():
    assert CoTD05_05.factorial(8) == math.factorial(8)

def test_negative():
    assert CoTD05_05.factorial(-2) == "Invalid number"