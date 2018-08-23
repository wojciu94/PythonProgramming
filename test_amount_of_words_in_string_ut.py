import pytest


@pytest.fixture(scope='function')
def amount_of_words_in_string(sentence: str) -> int:

    length = len(sentence)

    if length == 0:
        return 0

    words = 1

    for letter in range(0, length-2):

        if sentence[letter].isalnum() and not sentence[letter + 1].isalnum():

            words += 1

    if not sentence[length - 1].isalnum() and not sentence[length - 2].isalnum():

        words -= 1

    return words


def test_amountOfWordsInString_sentence_returnTrue_ut():

    sentence = "Ala ma kota"

    assert amount_of_words_in_string(sentence) == 3


def test_amountOfWordsInString_word_returnTrue_ut():

    sentence = "Janusz"

    assert amount_of_words_in_string(sentence) == 1


def test_amountOfWordsInString_emptyString_returnTrue_ut():

    sentence = ""

    assert amount_of_words_in_string(sentence) == 0


def test_amountOfWordsInString_sentenceWithEnter_returnTrue_ut():

    sentence = "Ala ma kota                \n \n                 a kot ma Ale.                 \n"

    assert amount_of_words_in_string(sentence) == 7


def test_amountOfWordsInString_sentenceWithSpaceAtTheBeginning_returnTrue_ut():

    sentence = "        Ala ma kota"

    assert amount_of_words_in_string(sentence) == 3


def test_amountOfWordsInString_sentenceWithSpaceAtTheEnd_returnTrue_ut():

    sentence = "Ala ma kota          "

    assert amount_of_words_in_string(sentence) == 3


def test_amountOfWordsInString_sentenceWithDotAtTheEnd_returnTrue_ut():

    sentence = "Ala ma kota."

    assert amount_of_words_in_string(sentence) == 3


def test_amountOfWordsInString_sentenceOnlySpace_returnTrue_ut():

    sentence = "        "

    assert amount_of_words_in_string(sentence) == 0


def test_amountOfWordsInString_sentenceWithSpecialChar_returnTrue_ut():

    sentence = "Ala ma kota@#$ ()**& ^&% & "

    assert amount_of_words_in_string(sentence) == 3

def test_amountOfWordsInString_sentenceWithDotandSpaceAtTheEnd_returnTrue_ut():

    sentence = "Ala ma kota. "

    assert amount_of_words_in_string(sentence) == 3


def test_amountOfWordsInString_sentenceWithSpaceAndDotAtTheEnd_returnTrue_ut():

    sentence = "Ala ma kota ."

    assert amount_of_words_in_string(sentence) == 3