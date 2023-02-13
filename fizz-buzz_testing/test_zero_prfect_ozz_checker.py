import pytest
''' 
smoke zero message
smoke with message
    main breakable cases
smoke with tuple of message
list with one broken part
message length < dividers length
dividers like string
one divider 
'''

from main import perfect_oz_checker as oz


def test_smoke_zero():
    assert oz() == 'FizzBuzzJuzz'


@pytest.mark.parametrize(
    "num, div, result, msg",
    [
        pytest.param(
            12, [2, 5], ['Fizz', 'Buzz'], 'Fizz', id="smoke two div"
        ),
        pytest.param(
            10, 2, ['Fizz', 'Buzz'], 'FizzBuzz', id="smoke one div"
        )
    ],
)
def test_zero_with_param_fixture(num, div, result, msg):
    assert oz(num, div, result) == msg