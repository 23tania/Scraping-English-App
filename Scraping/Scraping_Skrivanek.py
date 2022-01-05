from bs4 import BeautifulSoup
import requests

from Database.DbOperations import add_word
import Constants.Variables as Variables
from Classes.Lesson import *
from Classes.Word import *

# ŁĄCZENIE Z BEAUTIFUL SOUP
page = requests.get("https://skrivanek.pl/przedmioty-szkolne-po-angielsku/")
soup = BeautifulSoup(page.content, 'html.parser')

words = soup.select('.wpb_wrapper li')

def scrape_school_subjects():
    lesson_id = len(Variables.lessons_list)
    word_id = len(Variables.words_list)

    for word in words:
        polish = word.text.split(" – ",1)[1].rstrip().lstrip()
        english = word.text.split(" – ",1)[0].split(" [")[0].lower().rstrip().lstrip()
        
        if english == "pe": english = "physical education"

        lesson = Lesson(lesson_id, "school", "school description")
        
        if not Lesson.check_if_lesson_in_list(lesson):
            Variables.lessons_list.append(lesson)
            # add_lesson(lesson) # DODANIE KATEGORII DO BAZY
        else:
            lesson_id = Lesson.find_lesson_id_by_name("school")

        word = Word(polish, english, lesson_id, word_id)

        # TWORZENIE LISTY SŁÓWEK
        if not Word.check_if_word_in_list(word):
            word_id+=1
            Variables.words_list.append(word)
            # add_word(word) # DODANIE SŁÓWEK DO BAZY