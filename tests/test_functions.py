import pytest
from solutions.functions import *

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(8, 2) == 4
    assert divide(8, 0) is None

def test_power():
    assert power(2, 3) == 8

def test_reverse_string():
    assert reverse_string("hello") == "olleh"


