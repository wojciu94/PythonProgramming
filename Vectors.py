class VectorProtected:

    """
     Dwuwymiarowy wektor z dostępem protected
    """

    def __init__(self, a: float, b: float):

        self._x = a
        self._y = b

        # print("Wektor został utworzony")

    def length(self) -> float:

        """
        Zwraca długość wektora
        """
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def get_class_name(self) -> str:

        return self.__class__.__name__


class VectorPublic:

    """
     Dwuwymiarowy wektor z dostępem publicznym
    """

    def __init__(self, a: float, b: float):

        self.x = a
        self.y = b

        # print("Wektor został utworzony")

    def length(self) -> float:

        """
        Zwraca długość wektora
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5


    def get_class_name(self) -> str:

        return self.__class__.__name__


class VectorPrivate:

    """
     Dwuwymiarowy wektor z dostępem prywatnym
    """

    def __init__(self, a: float, b: float):

        self.__x = a
        self.__y = b

        # print("Wektor został utworzony")

    def length(self) -> float:

        """
        Zwraca długość wektora
        """
        return (self.__x ** 2 + self.__y ** 2) ** 0.5

    def get_Class_Name(self) -> str:

        return self.__class__.__name__

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, value: float):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, value: float):
        self.__y = value

    @y.deleter
    def y(self):
        del self.__y