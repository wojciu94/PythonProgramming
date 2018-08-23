import pytest


@pytest.fixture(scope='function')
def is_palindrom(word: str) -> bool:

    new_word = ""
    for index in range(0, len(word)):

        if word[index].isalnum():
            new_word += word[index].upper()

    length = len(new_word)

    if length == 0:

        return False

    else:

        for index in range(0, int(length/2)):

            if new_word[index] != new_word[-(index+1)]:
                return False

    return True


def test_isPalindrom_givePalindrom_returnTrue_ut():

    assert is_palindrom("ala")


def test_isPalindrom_givePalindromSentence_returnTrue_ut():

    assert is_palindrom("kobyla ma maly bok")


def test_isPalindrom_givePalindromWithUpperAndLowerLetter_returnTrue_ut():

    assert is_palindrom("KajAk")


def test_isPalindrom_giveNoPalindrom_returnFalse_ut():

     assert not is_palindrom("palindrom")


def test_isPalindrom_giveEmptyString_returnFalse_ut():

    assert not is_palindrom("")

def test_isPalindrom_giveOnlySpace_returnFalse_ut():

    assert not is_palindrom("      ")
