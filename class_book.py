import logging
import math


class Book:

    def __init__(self, title: str):

        self.title = title
        self.content = {}
        self.table_of_chapters = ""

    def add_title_and_content_of_chapter(self, chapter_title: str, chapter_content: list):

        self.content[chapter_title] = chapter_content

    def show_table_of_content(self):

        logging.critical('table_of_contents: {0}'.format(self.content))
        return 'table_of_contents: {0}'.format(self.content)

    def get_page_content(self, chapter_title: str, page_number: int) -> str:

        pages = self.content[chapter_title]
        logging.error(pages[page_number - 1])
        return pages[page_number - 1]


"""
book = Book("asd")

book.add_title_and_content_of_chapter("asd", ["qwer"])
book.add_title_and_content_of_chapter("asssad", ["qwewqewer"])
book.get_page_content("asd", 1)

"""


class BookWithAutor(Book):

    def __init__(self, title: str, writer: str):

        Book.__init__(self, title)
        self.writer = writer
        self.year_of_production = 0

    def add_year_of_production(self, year: int):

        if year > 0 and math.floor(year) == year:
            self.year_of_production = year




"""
book_with_autor = BookWithAutor("Pan Tadeusz", "Adam Mickiewicz")

book_with_autor.show_writer_of_book()
book_with_autor.add_title_and_content_of_chapter("Chapter1", ["Page1", "Page2", "Page3"])
book_with_autor.add_title_and_content_of_chapter("Chapter2", ["Page11", "Page22", "Page33"])
book_with_autor.get_page_content("Chapter1", 2)
book_with_autor.show_table_of_content()
"""
