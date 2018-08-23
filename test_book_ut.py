from class_book import *
import pytest


def test_init_CreateNewBook_noSideEffect_ut():

    book = BookWithAutor("Tytuł Książki")
    assert book.title == "Tytuł Książki"


def test_init_contentIsEmpty_returnTrue_ut():

    book = BookWithAutor("Tytuł Książki")
    assert len(book.content) == 0


def test_addTitleAndContentOfChapter_addEmptyTitleOfChapter_TitleOfChapterIsEmpty_ut():

    book = BookWithAutor("Tytuł Książki")
    book.add_title_and_content_of_chapter("", ["Text"])

    assert book.content[""] == ["Text"]


def test_addTitleAndContentOfChapter_addEmptyContentOfChapter_ContentOfChapterIsEmpty_ut():

    book = BookWithAutor("Tytuł Książki")
    book.add_title_and_content_of_chapter("Chapter", [""])

    assert book.content["Chapter"] == [""]


def test_addTitleAndContentOfChapter_addEmptyTitleAndContentOfChapter_TitleAndContentOfChapterAreEmpty_ut():

    book = BookWithAutor("Tytuł Książki")
    book.add_title_and_content_of_chapter("", [""])

    assert book.content[""] == [""]


def test_addTitleAndContentOfChapter_addTitleAndContentOfChapter_CorrectContent_ut():

    book = BookWithAutor("Tytuł Książki")
    book.add_title_and_content_of_chapter("Chapter1", ["Text TExt TExt"])

    assert book.content["Chapter1"] == ["Text TExt TExt"]


def test_showTableOfContent_emptyContent_returnEmptyContent_ut():

    book = BookWithAutor("Tytuł Książki")
    assert book.show_table_of_content() == "table_of_contents: {}"


def test_showTableOfContent_OneElement_returnThisElement_ut():

    book = BookWithAutor("Tytuł Książki")
    book.add_title_and_content_of_chapter("Chapter1", ["Text TExt TExt"])
    assert book.show_table_of_content() == "table_of_contents: {'Chapter1': ['Text TExt TExt']}"


def test_showTableOfContent_TwoElements_returnTheseElements_ut():

    book = BookWithAutor("Tytuł Książki")
    book.add_title_and_content_of_chapter("Chapter1", ["Text TExt TExt"])
    book.add_title_and_content_of_chapter("Chapter2", ["Text2 TExt2 TExt2"])
    assert book.show_table_of_content() == "table_of_contents: {'Chapter1': ['Text TExt TExt'], 'Chapter2': ['Text2 TExt2 TExt2']}"


def test_getPageContent_emptyContent_raiseKeyErrorExeption_ut():

    with pytest.raises(KeyError):
        book = BookWithAutor("Tytuł Książki")
        book.get_page_content("Chapter1", 1)


def test_getPageContent_wrongKey_raiseKeyErrorExeption_ut():

    with pytest.raises(KeyError):
        book = BookWithAutor("Tytuł Książki")
        book.add_title_and_content_of_chapter("Chapter1", ["Text TExt TExt"])
        book.get_page_content("Chapter12", 1)


def test_getPageContent_correctKeyAndPage_returnContentOfPage_ut():

        book = BookWithAutor("Tytuł Książki")
        book.add_title_and_content_of_chapter("Chapter1", ["Text TExt TExt", "ACS"])

        assert book.get_page_content('Chapter1', 1) == "Text TExt TExt"


def test_getPageContent_correctKeyAndWrongPage_raiseIndexError_ut():

    with pytest.raises(IndexError):
        book = BookWithAutor("Tytuł Książki")
        book.add_title_and_content_of_chapter("Chapter1", ["Text TExt TExt", "ACS"])
        book.get_page_content('Chapter1', 3)
