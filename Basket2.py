
from potter import Book
from typing import List, Set


class Basket:

    def __init__(self):
        self.__books = []   # type: List[Book]

    def addBook(self, book: Book):
        self.__books.append(book)

    def sort_collection_of_books(self):
        list_of_book_sets = []

        for book in self.__books:
            is_book_added = False

            for book_set in list_of_book_sets:
                if book not in book_set:
                    book_set.add(book)
                    is_book_added = True
                    break

            if not is_book_added:
                list_of_book_sets.append(set([book]))

    def __len__(self) -> int:
        return len(self.__books)



