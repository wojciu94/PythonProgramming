from Multiplier_Class import *
import pytest


def test_multiplierInt_getInt_returnMultiplyOfArguments_ut():
    int_multiplier = Multiplier(int)
    return int_multiplier(1, 2) == 2


def test_multiplierInt_getFloat_raiseTypeError_ut():
    with pytest.raises(TypeError):
        int_multiplier = Multiplier(int)
        return int_multiplier(1.0, 2.5) == 2.5


def test_multiplierInt_getIntAndFloat_raiseTypeErrors_ut():
    with pytest.raises(TypeError):
        int_multiplier = Multiplier(int)
        return int_multiplier(1, 2.5) == 2.5


def test_multiplierInt_getString_raiseTypeError_ut():
    with pytest.raises(TypeError):
        int_multiplier = Multiplier(int)
        return int_multiplier("1", 2.5) == 2.5


def test_multiplierFloat_getFloat_returnMultiplyOfArguments_ut():
    float_multiplier = Multiplier(float)
    return float_multiplier(1.5, 2.0) == 3.0


def test_multiplierFloat_getInt_raiseTypeError_ut():
    with pytest.raises(TypeError):
        float_multiplier = Multiplier(float)
        return float_multiplier(1, 2) == 2


def test_multiplierFloat_getIntAndFloat_raiseTypeError_ut():
    with pytest.raises(TypeError):
        float_multiplier = Multiplier(float)
        return float_multiplier(1, 2.5) == 2.5


def test_multiplierFloat_getString_raiseTypeError_ut():
    with pytest.raises(TypeError):
        float_multiplier = Multiplier(float)
        return float_multiplier("1", 2.5) == 2.5
