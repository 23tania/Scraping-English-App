import Constants.Variables as Variables

class Lesson:
    def __init__(self, id, lesson_name, description):
        self.id = id
        self.lesson_name = lesson_name
        self.description = description

    def __str__(self):
        return "lesson id: " + str(self.id) + ": " + self.lesson_name + ", " + self.description

    # SZUKANIE NAZWY LEKCJI PO ID
    def find_lesson_id_by_name(lesson_name):
        id = -1
        for lesson in Variables.lessons_list:
            if lesson.lesson_name == lesson_name:
                id = lesson.id

        return id

    # SPRAWDZENIE CZY KATEGORIA NIE ZOSTAŁA JUŻ DODANA DO LISTY
    def check_if_lesson_in_list(lesson):
        for les in Variables.lessons_list:
            if str(lesson.lesson_name) == str(les.lesson_name) or str(lesson.lesson_name) in Variables.double_lessons.keys():
                return True
                
            if int(les.id) == len(Variables.lessons_list) - 1:
                return False




