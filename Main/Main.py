import sys, os
sys.path.append(os.path.abspath(os.getcwd()))

from Scraping.Scraping_Ingless import scrape_lessons_ingless, scrape_words_ingless
from Scraping.Scraping_Lincoln import scrape_lessons_lincoln, scrape_words_lincoln
from Scraping.Scraping_Skrivanek import scrape_school_subjects
from Database.DbOperations import fix_actions, update_description
import Constants.Variables as Variables

def main():
    Variables.init()
    scrape_lessons_lincoln()
    scrape_words_lincoln()
    scrape_lessons_ingless()
    scrape_words_ingless()
    scrape_school_subjects()
    # update_description() # AKTUALIZACJA OPISÓW LEKCJI
    # fix_actions() # USUNIĘCIE "TO " Z CZASOWNIKÓW

main()