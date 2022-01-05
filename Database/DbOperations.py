import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import Constants.Variables as Variables

# ŁĄCZENIE Z BAZĄ MYSQL W AZURE
def connect_to_db():
    load_dotenv()
    conn = mysql.connector.connect(user = os.environ.get('DBUSER'), password = os.environ.get("DBPASS"), host = os.environ.get('DBHOST'), port = 3306, database = os.environ.get('DBNAME'))
    return conn

# DODANIE NOWEJ LEKCJI
def add_lesson(lesson):
    inserted = ""
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO lessons (lesson_id, lesson_name, description) VALUES (%s, %s, %s)", 
                    (lesson.id, lesson.lesson_name, lesson.description))
        conn.commit()
        inserted = "Udało się"

    except Error as e:
        conn.rollback()
        print(e)
        inserted = "Nie udało się"

    finally:
        conn.close()

    return inserted

# DODANIE NOWEGO SŁOWA
def add_word(word):
    inserted = ""
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO words (word_id, lesson_id, english, polish) VALUES (%s, %s, %s, %s)", 
                    (word.word_id, word.lesson_id, word.english, word.polish))
        conn.commit()
        inserted = "Udało się"

    except Error as e:
        conn.rollback()
        print(e)
        inserted = "Nie udało się"

    finally:
        conn.close()

    return inserted

# AKTUALIZOWANIE OPISÓW KATEGORII
def update_description():
    inserted = ""

    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT lesson_name, description FROM lessons")

        for lesson in cur.fetchall():
            cur.execute("UPDATE lessons SET description = %s WHERE lesson_name = %s", 
                       (Variables.descriptions[str(lesson[0])], str(lesson[0])))

        conn.commit()
        inserted = "Udało się"

    except Error as e:
        conn.rollback()
        print(e)
        inserted = "Nie udało się"

    finally:
        conn.close()

    return inserted

# USUNIĘCIE "TO " Z CZASOWNIKÓW
def fix_actions():
    inserted = ""

    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT lesson_id, english FROM words")

        for word in cur.fetchall():
            # KATEGORIA "PHYSICAL ACTIVITY"
            if str(word[0]) == "15" and "to " in str(word[1]):
                cur.execute("UPDATE words SET english = %s WHERE english = %s", 
                       (str(word[1])[3:], str(word[1])))

                conn.commit()

            # KATEGORIA "ACTIONS"
            if str(word[0]) == "2" and "to " in str(word[1]):
                cur.execute("UPDATE words SET english = %s WHERE english = %s", 
                       (str(word[1])[3:], str(word[1])))

                conn.commit()
            
        inserted = "Udało się"

    except Error as e:
        conn.rollback()
        print(e)
        inserted = "Nie udało się"

    finally:
        conn.close()

    return inserted