import sqlite3
import json

with open('src\config\conf.json', 'r') as bot_conf:
    conf = json.loads(bot_conf.read())

db_path = conf["db_path"]
con = sqlite3.connect(db_path,  check_same_thread=False)
cur = con.cursor()



def existence_check(book):
    res = cur.execute(f"""SELECT id FROM books 
                WHERE 
                    title = "{book['title']}" AND
                    author = "{book['author']}" AND
                    publish_date = "{book['publish_date']}"; """)
    if len(res.fetchall()) == 0:
        return True
    else:
        return False
     

def add(book):
    if existence_check(book):
        cur.execute(f"""INSERT INTO books (title, author, publish_date)
                    VALUES ("{book['title']}", "{book['author']}", {book['publish_date']});""")
        con.commit()
        return True
    else:
        return False


book_example = {'title' : "Test",
                'author': "Test",
                'publish_date': "2023"}
def main():
    add(book_example)


if __name__ == "__main__":
    main()