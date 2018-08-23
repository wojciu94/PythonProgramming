import random
import pytest


@pytest.fixture(scope='function')
def minimum_of_set(collection: set)-> int: # czasami zwracam bool, a czasami INT, pisać wtedy -> int albo -> bool?

    if len(collection) == 0:
        return False

    collection_minimum = 0

    for index in collection:
        collection_minimum = index
        break

    for index in collection:

        if type(index) is not int and type(index) is not float:
            return False

        if index < collection_minimum:
            collection_minimum = index

    return collection_minimum


def test_minimum_of_set_randomIntSet_returnTrue_ut():

    numbers = set()

    for number in range(0, 100):
        numbers.add(random.randint(0, 1000))

    minimum_of_collection = min(numbers)

    assert minimum_of_set(numbers) == minimum_of_collection


def test_minimum_of_set_emptySet_returnFalse_ut():

    numbers = set()

    assert not minimum_of_set(numbers)


def test_minimum_of_set_minusValues_returnTrue_ut():

    numbers = {1, 2, 3, 4, 5, 6, -9, -12, -14, -2, 0, 0, 0}

    minimum_of_collection = min(numbers)

    assert minimum_of_set(numbers) == minimum_of_collection


def test_minimum_of_set_notDigitsInSet_returnFalse_ut():

    numbers = {1, 2, 'a', 4, 5, ',', -9, '/', -14, -2, 0, 0, 0}

    assert not minimum_of_set(numbers)


def test_minimum_of_set_randomFloatSet_returnTrue_ut():

    numbers = set()

    for number in range(0, 100):
        numbers.add(random.uniform(0, 1000))

    minimum_of_collection = min(numbers)

    assert minimum_of_set(numbers) == minimum_of_collection