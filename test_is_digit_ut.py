
import pytest


@pytest.fixture(scope='function')
def digit() -> str:
    return "123"


@pytest.fixture(scope="function")
def no_Digit() -> str:
    return "abc"


def test_isDigit_passDigit_returnValueTrue_ut(digit: str):
    """
    Test checks if text/string is a digit.
    """
    assert digit.isdigit()


def test_isNoDigit_passDigit_returnValueTrue_ut(no_Digit: str):
    """
    Test checks if text/string is not a digit.
    """
    assert not no_Digit.isdigit()
