import pytest
from main import perfect_oz_checker as oz


def test_smoke_zero():
    assert oz() == 'FizzBuzzJuzz'
    assert oz(12, [2, 5], ['Fizz', 'Buzz']) == 'Fizz'
    assert oz(10, [2, 5], ['Fizz', 'Buzz']) == 'Fizz'