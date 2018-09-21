from potter import Book
from typing import List, Tuple, Dict


class Basket:

    def __init__(self):
        self.__books = {}  # type: Dict[Tuple[str, float]]
        self.__how_many_books = 0

    def addBook(self, book: Book):

        book_in_basket = (book.title, book.price)

        if self.__books.get(book_in_basket, None):
            self.__books[book_in_basket] += 1
        else:
            self.__books[book_in_basket] = 1

        self.__how_many_books += 1

    def __len__(self) -> int:
        return len(self.__books)

    def countTotalPrice(self) -> float:

        total_price = 0.0

        if len(self.__books.keys()) == 5:
            for book_in_basket in self.__books.keys():
                total_price += book_in_basket[1] * (1.0 - 0.25)
                self.__books[book_in_basket] -= 1
                if self.__books[book_in_basket] == 0:
                    self.__books.pop(book_in_basket)

        # for book_in_basket in self.__books.keys():
        #   total_price += book_in_basket[1] * self.__books[book_in_basket]

        return total_price

    """
            first_book = self.__books[0]
            total_price = first_book.price
            discount_value = 0.0

            for i in range(1, len(self.__books)):
                next_book = self.__books[i]

                if first_book.title != next_book.title:
                    discount_value = 0.05

                total_price += next_book.price
                    return total_price * (1.0 - discount_value)
    """


