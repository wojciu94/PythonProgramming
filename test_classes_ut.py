from classes import *
import pytest


def test_dummyOperation_getIntValues_returnTuple_ut():
    assert (calculate(dummy_operation, 1, 2)) == (1, 2)


def test_dummyOperation_getFloatValuse_returnTuple_ut():
    assert (calculate(dummy_operation, 1.0, 2.5)) == (1.0, 2.5)


def test_dummyOperation_getIntandFloatValues_returnTuple_ut():
    assert (calculate(dummy_operation, 1, 2.5)) == (1, 2.5)


def test_dummyOperation_getString_returnTupleWithString_ut():
    assert (calculate(dummy_operation, "1", "2.5")) == ("1", "2.5")


def test_multiply_getFloatsValues_returnMultiplyOfArguments_ut():
    assert (calculate(multiply, 1.0, 2.0)) == 2.0


def test_multiply_getIntValues_returnMultiplyOfArguments_ut():
    assert (calculate(multiply, 1, 2)) == 2


def test_multiply_getFloatAndIntValues_returnFloatTypeMultiplyOfArguments_ut():
    assert (calculate(multiply, 1.5, 3)) == 4.5


def test_multiply_getStringArguments_raiseTypeError_ut():
    with pytest.raises(TypeError):
        calculate(multiply, "1", "2")


def test_multiply_getStringAndIntArgument_raiseTypeError_ut():
    assert not (calculate(multiply, 3, "2")) == 6


