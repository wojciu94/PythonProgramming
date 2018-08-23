import pytest


@pytest.fixture(scope='function')
def reverse_function(sentence: str) -> str:

    length = len(sentence)

    if length == 0:
        return sentence

    reverse_sentence = ""

    for i in range(0, length):

        reverse_sentence += sentence[-(i + 1)]

    return reverse_sentence


def test_reverseFunction_sentence_returnTrue_ut():

    sentence = "Ala ma kota"

    assert sentence[::-1] == reverse_function(sentence)


def test_reverseFunction_word_returnTrue_ut():

    sentence = "Tramwaj"

    assert sentence[::-1] == reverse_function(sentence)


def test_reverseFunction_sentenceWithEnter_returnTrue_ut():

    sentence = "Ala na kota                \n \n                 a kot ma Ale.\n"

    assert sentence[::-1] == reverse_function(sentence)


def test_reverseFunction_sentenceWithSpaceAtTheBeginning_returnTrue_ut():

    sentence = "        Ala na kota"

    assert sentence[::-1] == reverse_function(sentence)


def test_reverseFunction_sentenceWithSpaceAtTheEnd_returnTrue_ut():

    sentence = "Ala na kota          "

    assert sentence[::-1] == reverse_function(sentence)


def test_reverseFunction_sentenceWithSpecialChars_returnTrue_ut():

    sentence = "a  b  c  d e f....j  12345     !@#$%^&*()_+|}{?</.,;'][                 a.........................12   "

    assert sentence[::-1] == reverse_function(sentence)


def test_reverseFunction_emptyString_returnTrue_ut():

    sentence = ""

    assert sentence[::-1] == reverse_function(sentence)
