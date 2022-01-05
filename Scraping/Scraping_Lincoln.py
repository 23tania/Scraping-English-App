from bs4 import BeautifulSoup
import requests

from Database.DbOperations import add_lesson, add_word
import Constants.Variables as Variables
from Classes.Lesson import *
from Classes.Word import *

# ŁĄCZENIE Z BEAUTIFUL SOUP
page = requests.get("https://lincoln.edu.pl/blog/przydatne-slowka-po-angielsku-poziom-a1/")
soup = BeautifulSoup(page.content, 'html.parser')

words = soup.select('li em')
lessons = soup.select('h2')

# SCRAPOWANIE I DODAWANIE LEKCJI DO TABELI LESSONS I WORDS
def scrape_lessons_lincoln():
    Variables.is_first_scraping = False
    lesson_id = len(Variables.lessons_list)
    word_id = len(Variables.words_list)

    for lesson in lessons:
        if "A1" not in lesson.text:
            polish = lesson.findChild("em").previous_sibling[32:]
            polish = polish[:len(polish) - 2]
            english = lesson.findChild("em").text

            if english=="lothes": english="clothes"

            lesson = Lesson(lesson_id, english, english)
            word = Word(polish, english, lesson_id, word_id)

            # TWORZENIE LISTY KATEGORII
            if not Lesson.check_if_lesson_in_list(lesson):
                lesson_id+=1
                Variables.lessons_list.append(lesson)
                # add_lesson(lesson) # DODANIE KATEGORII DO BAZY
            
            # TWORZENIE LISTY SŁÓWEK
            if not Word.check_if_word_in_list(word):
                word_id+=1
                Variables.words_list.append(word)
                # add_word(word) # DODANIE SŁÓWEK DO BAZY

# SCRAPOWANIE I DODAWANIE SŁÓW DO TABELI WORDS
def scrape_words_lincoln():
    word_id = len(Variables.words_list)

    for english in words:
        polish = english.next_sibling[2:].rstrip().lstrip()
        lesson = english.find_parent("ul").find_previous_sibling("h2").findChild("em").text
        english = english.text.rstrip().lstrip()

        lesson = fix_words_lincoln(lesson, polish)[0]
        polish = fix_words_lincoln(lesson, polish)[1]

        lesson_id = Lesson.find_lesson_id_by_name(lesson)
        word = Word(polish, english, lesson_id, word_id)

        # SPRAWDZENIE CZY SŁÓWKA JUŻ NIE MA W BAZIE
        if not Word.check_if_word_in_list(word):
            word_id+=1
            Variables.words_list.append(word)
            print(word)
            # add_word(word) # DODANIE SŁÓWEK DO BAZY

def fix_words_lincoln(lesson, polish):
    # POPRAWIANIE BŁĘDÓW Z NAZWĄ KATEGORII/SŁOWA
    if lesson=="lothes": lesson="clothes"

    # DEFINICJE ODDZIELONE ZNAKIEM "," i "/"
    for i in [',','/']:
        if i in polish:
            polish = polish.partition(i)[2].lstrip()

    # USUNIĘCIE NAWIASÓW
    for i in ['(',')']:
        if i in polish:
            polish = polish.replace(i, "")

    return lesson, polish