from Vectors import *
import pytest


def test_VectorProtected_Access_setXArgument_XChangedOnRequiredValue_ut():

    vector_protected = VectorProtected(2, 3)

    vector_protected.x = 4.0

    assert vector_protected.x == 4.0, "X changed"


def test_VectorPublic_Access_setXArgument_XChangedOnRequiredValue_ut():

    vector_public = VectorPublic(2, 3)

    vector_public._x = 4.0

    assert vector_public._x == 4.0, "X changed"


def test_VectorPrivate_Access_tryGetXArgument_raiseAttributeError_ut():

    vector_private = VectorPrivate(2, 3)

    with pytest.raises(AttributeError):

        # przechwyci wyjątek i jeśli jest tego typu co argument to test się powiedzie

        x = vector_private.__x


def test_getClassName_returnSameNameAsClass_ut():

    vector_private = VectorPrivate(1.0, 2.0)

    assert vector_private.get_Class_Name() == "VectorPrivate"


def test_get_x_property_returnValueSetByInitMethod_ut():

    vector2d = VectorPrivate(1.0, 2.0)
    assert vector2d.x == 1.0


@pytest.mark.skip
def test_get_x_trySetNewValue_raise_Exception_ut():

    with pytest.raises(AttributeError):
        vector2d = VectorPrivate(1.0, 2.0)
        vector2d.x = 3.0


def test_set_x_setNewValue_newValueIsSet_ut():

    vector2d = VectorPrivate(1.0, 2.0)
    vector2d.x = 3.0
    assert vector2d.x == 3.0


def test_del_x_xObjectRemovedLostAccess_raiseException_ut():

    with pytest.raises(AttributeError):
        vector2d = VectorPrivate(1.0, 2.0)
        del vector2d.x
        x = vector2d.x


def test_get_y_property_returnValueSetByInitMethod_ut():

    vector2d = VectorPrivate(1.0, 2.0)
    assert vector2d.y == 2.0

@pytest.mark.skip
def test_get_y_trySetNewValue_raise_Exception_ut():

    with pytest.raises(AttributeError):
        vector2d = VectorPrivate(1.0, 2.0)
        vector2d.y = 3.0


def test_set_y_setNewValue_newValueIsSet_ut():

    vector2d = VectorPrivate(1.0, 2.0)
    vector2d.y = 3.0
    assert vector2d.y == 3.0


def test_del_y_yObjectRemovedLostAccess_raiseException_ut():

    with pytest.raises(AttributeError):
        vector2d = VectorPrivate(1.0, 2.0)
        del vector2d.y
        y = vector2d.y