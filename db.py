import sqlite3
import random

def rows_in_table():
    conn = sqlite3.connect('jlpt.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) from jlpt")
    total = c.fetchone()
    return total[-1]

def jlpt_data():
    conn = sqlite3.connect('jlpt.db')
    c = conn.cursor()
    total = rows_in_table() # Get the number of rows in the table.
    number = random.randint(1, total)
    c.execute("SELECT * FROM jlpt WHERE rowid = (?)", (number,))
    data_with_questions = c.fetchone()
    conn.commit()
    conn.close()
    return data_with_questions

def add_question(phrase, ans_a, ans_b, ans_c, ans_d, answer):
    conn = sqlite3.connect('jlpt.db')
    c = conn.cursor()
    c.execute("INSERT INTO jlpt VALUES (?,?,?,?,?,?", (phrase, ans_a, ans_b, ans_c, ans_d, answer))
    conn.commit()
    conn.close()

def add_questions(questions):
    """ Insert questions to the data base.
    questions = [("ずっと好調だったのに、最後の試合で敗れてしまった", "たおれて", "やぶれて", "みだれて", "つぶれて", "やぶれて"),
                ("この仕事には高い語学力が要求される", "ようきゅ", "よっきゅう", "ようきゅう", "よっきゅ", "ようきゅう"),
                ("友達の合格をみんなで祝った", "いわった", "いのった", "うらなった", "ねがった", "いわった"),
                ("寒かったら、エアコンの温度を調節してください", "ちょうさい", "ちょうせい", "ちょうさつ", "ちょうせつ", "ちょうせつ"),
                ("この書類を至急コピーしてきてください", "しっきゅう", "ちっきゅう", "しきゅう", "ちきゅう", "しきゅう"),]
    """
    conn = sqlite3.connect('jlpt.db')
    c = conn.cursor()
    c.executemany("INSERT INTO jlpt VALUES (?,?,?,?,?,?)", questions)
    conn.commit()
    conn.close()

def create_table():
    conn = sqlite3.connect('jlpt.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE jlpt (
            phrase TEXT,
            ans_a TEXT,
            ans_b TEXT,
            ans_c TEXT,
            ans_d TEXT,
            answer TEXT
             )""")
    conn.commit()
    conn.close()

