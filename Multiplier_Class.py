from abc import ABCMeta, abstractmethod
from typing import Union, Iterable


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


# polimorfozm statyczny
class Multiplier:

    def __init__(self, type_: type):
        self.__type = type_

    def __call__(self, *args, **kwargs: dict):

        self.__checkTypes(args)
        self.__checkTypes(kwargs.values())

        return multiply(*args, **kwargs)

    def __checkTypes(self, arguments: Iterable):

        for arg in arguments:

            if not isinstance(arg, self.__type):
                raise TypeError("Argument {} has incorrect type".format(arg))


# polimorfizm dynamiczny
class MultiplierBase:

    def multiply(self, a, b):
        self._checkTypes(a, b)
        return a * b

    # metoda wirtualna
    def _checkTypes(self, a, b):
        pass


class IntMultiplier(MultiplierBase):

    def _checkTypes(self, a, b):

        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError()


class FloatMultiplier(MultiplierBase):

    def _checkTypes(self, a, b):

        if not isinstance(a, float) or not isinstance(b, float):
            raise TypeError()


int_multiplier = IntMultiplier()
print(int_multiplier.multiply(1, 3))

float_multiplier = FloatMultiplier()
print(float_multiplier.multiply(1.0, 2.3))


# class as interface
class MultiplierInterface(metaclass=ABCMeta):

    # metoda czysto wirtualna
    @abstractmethod
    def multiply(self, a, b):
        pass


# nie można stworzyć obiektu klasy abstrakcyjnej / Interfejsu
# multiplier = MultiplierInterface()

class IntMultiplierImplementation(MultiplierInterface):

    def __init__(self):
        super().__init__()

    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError()
        return a * b


multiplier = IntMultiplierImplementation()
print(multiplier.multiply(2, 5))
