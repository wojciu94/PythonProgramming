
#                           ćwiczenie 2 część 1
name = 'Wojciech Dudziec'
# print (name)

title = 'Tytuł książki'
# print (title)

chapter_1 = ['strona1', 'strona2', 'strona3']
chapter_2 = chapter_1 + ['strona4', 'strona5']
chapter_3 = chapter_2 + ['strona6', 'strona7']

pages_amount = len(chapter_1) + len(chapter_2) + len(chapter_3)
# print (pages_amount)
 
content = {'1': chapter_1, '2': chapter_2, '3': chapter_3}

# print (content)


#                           ćwiczenie 2 część 2
"""
second_chapter = content["2"]
# print (second_chapter)


trash = second_chapter.pop(2)
# print (trash)

length = len(trash)
end = round(0.7 * length)

# print (end)

less = trash[0:end]

# print (less)

second_chapter.append(less)
# print (second_chapter)

content['2'] = second_chapter

# print (content)
"""
#                           Ćwiczenie 3 część 1
"""
print ('Tytuł książki: ', title)
chapters = content.keys()
print ('Tytuły rozdziałów: ', chapters)
zero_ascii = ord('0')
nine_ascii = ord('9')

while True:

    chapter = input("Jaki rozdział chcesz przeczytać?\n")
    can_ask_for_page_number = False

    for key in chapters:
        if chapter == key:
            can_ask_for_page_number = True
            length1 = len(content[chapter])
            print(content[chapter])
            break

    if can_ask_for_page_number:

        while True:

            page = input("Jeśli chcesz przeczytać cały rozdział wybierz 0.\nJeśli chcesz przeczytać konkretną stronę wpisz tutaj jest numer.\n")

            if page.isdigit():
                page_int = int(page)

                if page_int == 0:
                    print(content [chapter])
                    break

                elif page_int < length1 + 1 or page_int < 0:
                    print(content [chapter][page_int - 1])
                    break
            else:
                print('W tym rozdziale nie ma takiej strony. Wpisz inną.')
        break

    else:
        print("Nie ma takiego rozdziału. Wpisz poprawny rozdział")

"""
#                              Ćwiczenie 3 część 2            #
"""
question = input("Czy chcesz napisać nowy rozdział?\n Wpisz TAK lub NIE\n")

if question in ['t', 'T', 'Tak', 'tak']:

    title1 = input("Podaj tytuł rozdziału\n")
    content_of_chapter = input("Podaj treść rozdziału\n")

    with open(title1, 'w') as file_write:

        file_write.write(content_of_chapter)
        file_write.close()

    with open(title1, 'r') as file_read:

        content = file_read.read()
        print(content)
        file_read.close()

else:
    print ('Koniec programu')

"""

########################################################################################


def show(table_of_contents: str, writer: str):

    print('table_of_contents: {0}, writer {1}'.format(table_of_contents, writer))


show("Content", name)


book = {'1': ["page1", "page2"]}


def get_page_content(chapter: str, page_number: int, content: str = "content") -> str:

    print(content)
    pages = book[chapter]   # type: List[str]
    return pages[page_number - 1]


print(get_page_content('1', 2))














