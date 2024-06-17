import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1', # localhost
    'database': 'test10'
}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

# cursor.execute("INSERT INTO `users`(`name`, `login`, `pass`) VALUES ('Вася','vasya@mail.ru','333')")
# conn.commit()
login = input("Введите логин: ")
password = input("Введите пароль: ")
data = (login, password)
cursor.execute("SELECT * FROM users WHERE login = %s AND pass = %s", data)
for row in cursor.fetchall():
    print( row )