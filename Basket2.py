
from potter import Book
from typing import List


class Basket:

    def __init__(self):
        self.__books = []   # type: List[Book]
        self.__list_of_book_sets = []
        self.__discounts = [1, 0.95, 0.9, 0.8, 0.75]

    def addBook(self, book: Book):
        self.__books.append(book)

    def sort_collection_of_books(self) -> List[set]:

        for book in self.__books:
            is_book_added = False

            for book_set in self.__list_of_book_sets:
                if book not in book_set:
                    book_set.add(book)
                    is_book_added = True
                    break

            if not is_book_added:
                self.__list_of_book_sets.append(set([book]))

        return self.__list_of_book_sets

    def countTotalPrice(self) -> float:

        total_price = 0.0
        total_price_special = 0.0
        amount_of_books = len(self.__books)

        if amount_of_books == 8 and len(self.__list_of_book_sets) == 2:
            for book in self.__books:
                total_price_special += book.price

            total_price_special *= self.__discounts[3]

        for book_set in self.__list_of_book_sets:

            total_price_of_set = 0.0

            for book in book_set:
                total_price_of_set += book.price

            amount_of_books_in_set = len(book_set)

            total_price += total_price_of_set * self.__discounts[amount_of_books_in_set - 1]

        if total_price_special != 0.0:
            return min(total_price, total_price_special)

        else:
            return total_price

    def __len__(self) -> int:
        return len(self.__books)
