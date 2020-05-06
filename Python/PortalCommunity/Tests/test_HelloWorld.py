import pytest
from Code import HelloWorld

def test_answer():
    assert HelloWorld.func("World") == "Hello World"