import Constants.Variables as Variables

class Word:
    def __init__(self, polish, english, lesson_id, word_id):
        self.polish = polish
        self.english = english
        self.lesson_id = lesson_id
        self.word_id = word_id

    def __str__(self):
        return "word " + str(self.word_id) + ": " +  self.polish + " - " + self.english + ", id kategorii: " + str(self.lesson_id)

    # SPRAWDZENIE CZY SŁÓWKO NIE ZOSTAŁO JUŻ DODANE DO LISTY
    def check_if_word_in_list(word):
        for w in Variables.words_list:
            if str(word.english) == str(w.english) or str(word.polish) == str(w.polish) or str(word.english) + "s" == str(w.english) or str(word.english) == str(w.english) + "s":
                return True

            if int(w.word_id) == len(Variables.words_list) - 1:
                return False

