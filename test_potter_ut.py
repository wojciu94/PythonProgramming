from potter import Book
from Basket import Basket
import pytest

# data,
# price = None    # type: float
# title = None    # type: str


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

@pytest.mark.skip
def test_basket_addBook_addTwoBooks_TwoBooksInBasket_ut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter1", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)

    assert len(basket) == 2


def test_basket_countTotalPrice_buyTwoThisSameBooks_noDiscount_ut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter1", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)

    assert basket.countTotalPrice() == 16.0


@pytest.mark.skip
def test_basket_countTotalPrice_buyTwoDifferentBooks_fivePercentOfDiscount_ut():
    first_book = Book("Potter1", 8.0)
    second_book = Book("Potter2", 8.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)

    assert basket.countTotalPrice() == 15.2


@pytest.mark.skip
def test_basket_countTotalPrice_buyThreeDifferentBooks_tenPercentOfDiscountut():
    first_book = Book("Potter1", 10.0)
    second_book = Book("Potter2", 10.0)
    third_book = Book("Potter3", 10.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)
    basket.addBook(third_book)

    assert 27.0 == basket.countTotalPrice()


def test_basket_countTotalPrice_buyFiveDifferentBooks_25PercentOfDiscountut():
    first_book = Book("Potter1", 10.0)
    second_book = Book("Potter2", 10.0)
    third_book = Book("Potter3", 10.0)
    fourth_book = Book("Potter2", 10.0)
    fifth_book = Book("Potter3", 10.0)

    basket = Basket()
    basket.addBook(first_book)
    basket.addBook(second_book)
    basket.addBook(third_book)
    basket.addBook(fourth_book)
    basket.addBook(fifth_book)

    assert 37.5 == basket.countTotalPrice()