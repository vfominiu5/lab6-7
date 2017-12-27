import MySQLdb


def insert(name,desc):
    c.execute("INSERT INTO books (name, description) VALUES (%s, %s);", (name, desc))
    db.commit()


def get_entries():
    c.execute("SELECT * FROM books;")
    return c.fetchall()


def truncate():
    c.execute("TRUNCATE books;")
    db.commit()

# Открываем соединение
db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)
db.set_character_set('utf8')
# Получаем курсор для работы с БД
c = db.cursor()


insert('Книга','Описание книги')
entries = get_entries()
for e in entries: print(e)
truncate()


c.close()   # Закрываем курсор
db.close()  # Закрываем соединение
