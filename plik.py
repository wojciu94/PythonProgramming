from Basket2 import *


first_book = Book("Potter1", 8.0)
second_book = Book("Potter2", 8.0)
third_book = Book("Potter3", 8.0)
fourth_book = Book("Potter4", 8.0)
fifth_book = Book("Potter5", 8.0)


basket = Basket()
basket.addBook(first_book)
basket.addBook(second_book)
basket.addBook(third_book)
basket.addBook(fourth_book)
basket.addBook(fifth_book)

basket.addBook(first_book)
basket.addBook(second_book)
basket.addBook(fourth_book)
basket.addBook(fifth_book)

basket.addBook(second_book)

basket.sort_collection_of_books()

basket.print_sorted_collection_of_books()


