import pytest


@pytest.fixture(scope='function')
def isdigit(text: str) -> bool:

    if len(text) == 0:
        return False

    else:
        zero_ascii = ord('0')
        nine_ascii = ord('9')

        for character in text:

            char_as_int = ord(character)

            if char_as_int < zero_ascii or char_as_int > nine_ascii:
                return False

    return True


def test_isDigit_passDigit_returnTrue_ut():

    assert isdigit("123")


def test_isDigit_passNoDigit_returnFalse_ut():

    assert not isdigit("abc")


def test_isDigit_passEmptyString_returnFalse_ut():

    assert not isdigit("")


def test_isDigit_passSpecialCharacters_returnFalse_ut():

    assert not isdigit("+-=12#$%^&")


def test_isDigit_passOnlySpace_returnFalse_ut():

    assert not isdigit("      ")
