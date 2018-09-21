

class Book:

    def __init__(self, title: str, price: float):
        self.__title = title
        self.__price = price

    @property  # sposób pokazania światu zmiennej prywatnej w kontrolowany sposób
    def title(self) -> str:
        return self.__title

    @property
    def price(self) -> float:
        return self.__price
