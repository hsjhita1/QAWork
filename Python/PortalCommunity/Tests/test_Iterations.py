import pytest
from Code import Iterations

def testWhile():
    assert Iterations.whileLoop(0) == 5

def testFor():
    assert Iterations.forLoop(0) == 50

def testBreak():
    assert Iterations.breakLoop(0) == 20