from potter import Book
from Basket2 import Basket


def test_book_canCreateBook_noSideEffects_ut():

    book = Book("Potter1", 8.0)
    assert book.title == "Potter1"
    assert book.price == 8.0


def test_canCreateBasket_noSideEffects_ut():
    basket = Basket()


def test_basket_addBook_addOneBook_OneBookInBasket_ut():
    book = Book("Potter1", 8.0)
    basket = Basket()
    basket.addBook(book)

    assert len(basket) == 1


def test_basket_addBook_addTwoBooks_TwoBooksInBasket_ut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter2", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)

    assert len(basket) == 2


def test_basket_sortCollectionOfBooks_TwoThisSameBooks_ut():
    first_book = Book("Potter1", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(first_book)

    sorted_list = [{first_book}, {first_book}]

    assert sorted_list == basket.sort_collection_of_books()


def test_basket_sortCollectionOfBooks_TwoDifferentBooks_ut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter2", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)

    sorted_list = [{first_book, second_book}]

    assert sorted_list == basket.sort_collection_of_books()


def test_basket_sortCollectionOfBooks_ThreeBooksTwoDifferentBooks_ut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter2", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(first_book)
    basket.addBook(second_book)

    sorted_list = [{first_book, second_book}, {first_book}]

    assert sorted_list == basket.sort_collection_of_books()


def test_basket_countTotalPrice_buyTwoThisSameBooks_noDiscount_ut():
    first_book = Book("Potter1", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(first_book)

    basket.sort_collection_of_books()

    assert basket.countTotalPrice() == 16.0



def test_basket_countTotalPrice_buyTwoDifferentBooks_fivePercentOfDiscount_ut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter2", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)

    basket.sort_collection_of_books()

    assert basket.countTotalPrice() == 15.2



def test_basket_countTotalPrice_buyThreeDifferentBooks_tenPercentOfDiscountut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter2", 8.0)
    third_book = Book("Potter3", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)
    basket.addBook(third_book)

    basket.sort_collection_of_books()

    assert 24.0 * 0.9 == basket.countTotalPrice()


def test_basket_countTotalPrice_buyFiveDifferentBooks_25PercentOfDiscount_ut():
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

    basket.sort_collection_of_books()

    assert 8.0 * 5 * 0.75 == basket.countTotalPrice()


def test_basket_countTotalPrice_buySomeBooks_ut():
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

    total = 5 * 8.0 * 0.75 + 4 * 8.0 * 0.8 + 1 * 8.0 * 1

    assert total == basket.countTotalPrice()


def test_basket_countTotalPrice_SpecialCase_ut():
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
    basket.addBook(third_book)

    basket.sort_collection_of_books()

    total = 4 * 8.0 * 0.8 + 4 * 8.0 * 0.8

    assert total == basket.countTotalPrice()


def test_basket_countTotalPrice_NoSpecialCase_ut():
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

    basket.addBook(second_book)

    basket.sort_collection_of_books()

    total = 5 * 8.0 * 0.75 + 2 * 8.0 * 0.95 + 1 * 8.0 * 1

    assert total == basket.countTotalPrice()


def test_basket_countTotalPrice_noBooks_ut():

    basket = Basket()
    basket.sort_collection_of_books()

    assert 0.0 == basket.countTotalPrice()


def test_basket_countTotalPrice_oneBooks_ut():

    basket = Basket()
    fifth_book = Book("Potter5", 8.0)
    basket.addBook(fifth_book)

    basket.sort_collection_of_books()

    assert 8.0 == basket.countTotalPrice()