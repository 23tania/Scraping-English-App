from bs4 import BeautifulSoup
import requests

from Database.DbOperations import add_lesson, add_word
import Constants.Variables as Variables
from Classes.Lesson import *
from Classes.Word import *

# ŁĄCZENIE Z BEAUTIFUL SOUP
page = requests.get("https://www.ingless.pl/artykul/slownictwo-na-poziomie-a1/")
soup = BeautifulSoup(page.content, 'html.parser')

# USUNIĘCIE PUSTYCH ZNACZNIKÓW NP. <p> </p>
clean_page = soup.findAll(lambda html: not html.contents or len(html.get_text(strip=True)) <= 0)
[html.extract() for html in clean_page]

start = soup.find('h2', text="1. Clothes (ubrania)")
find_words = start.find_all_next('p')
lessons = soup.select('h2')

# SCRAPOWANIE I DODAWANIE LEKCJI DO TABELI LESSONS I WORDS
def scrape_lessons_ingless():
    lesson_id = len(Variables.lessons_list)
    word_id = len(Variables.words_list)

    for lesson in lessons:
    
        # Wykluczenie pierwszego h2 - 'Słownictwo na poziomie A1 Breakthrough (Beginner/elementary) '
        if "A1" not in lesson.text:
            left = lesson.text.find("(")
            right = lesson.text.find(")")
            dot = lesson.text.find(".")
            polish = lesson.text[left + 1: right]
            english = lesson.text[dot + 2: left - 1].lower()
            polish = fix_lessons_ingless(polish)

            lesson = Lesson(lesson_id, english, english)
            word = Word(polish, english, lesson_id, word_id)

            # TWORZENIE LISTY KATEGORII
            if not Lesson.check_if_lesson_in_list(lesson) or Variables.is_first_scraping:
                lesson_id+=1
                Variables.lessons_list.append(lesson)
                print(lesson)
                # add_lesson(lesson) # DODANIE KATEGORII DO BAZY
            
            # TWORZENIE LISTY SŁÓWEK
            if not Word.check_if_word_in_list(word):
                word_id+=1
                Variables.words_list.append(word)
                print(word)
                # add_word(word) # DODANIE SŁÓWEK DO BAZY

# SCRAPOWANIE I DODAWANIE SŁÓW DO TABELI WORDS
def scrape_words_ingless():
    word_id = len(Variables.words_list)

    # SZUKA SŁÓWEK PO KATEGORIACH
    for words in find_words:
        if "Jeżeli opanowaliśmy" in words.text:
            break
        
        lesson = words.find_previous_sibling("h2")
        left = lesson.text.find("(")
        dot = lesson.text.find(".")
        lesson_name = lesson.text[dot + 2: left - 1].lower()

        # USUNIĘCIE ZBĘDNYCH DODATKOWYCH KATEGORII
        for key in Variables.double_lessons:
            if lesson_name == key:
                lesson_name = Variables.double_lessons[key]

        words = words.get_text(strip=True, separator='\n').splitlines()

        for word in words:
            if " - " in word:
                word = word.replace("-", "–")

            polish = word.split(" – ",1)[1].rstrip().lstrip()
            english = word.split(" – ",1)[0].rstrip().lstrip()
            polish = fix_words_ingless(polish)

            word = Word(polish, english, Lesson.find_lesson_id_by_name(lesson_name), word_id)

            # SPRAWDZENIE CZY SŁÓWKA JUŻ NIE MA W BAZIE
            if not Word.check_if_word_in_list(word):
                word_id+=1
                Variables.words_list.append(word)
                print(word)
                # add_word(word) # DODANIE SŁÓWEK DO BAZY

# POPRAWIENIE KATEGORII
def fix_lessons_ingless(polish):
    if "," in polish:
        polish = polish.partition(",")[2].lstrip()

    return polish

# POPRAWIENIE SŁÓWEK
def fix_words_ingless(polish):
    # DEFINICJE ODDZIELONE ZNAKIEM "," i "/"
    for i in [',','/']:
        if i in polish:
            polish = polish.partition(i)[0].lstrip().rstrip()

    # USUNIĘCIE NAWIASÓW
    for i in ['(',')']:
        if i in polish:
            polish = polish.replace(i, "")

    return polish