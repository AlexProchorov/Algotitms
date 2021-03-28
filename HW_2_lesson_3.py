import hashlib
import os
import sqlite3


con = sqlite3.connect('users.db')
cursorObj = con.cursor()
try:
    cursorObj.execute("CREATE TABLE users(id integer PRIMARY KEY, username text, password_hash byte, salt byte)")
except sqlite3.OperationalError:
    print("Table already exists")

login = input("Enter your login: ")
query = "SELECT id, password_hash, salt FROM users WHERE username = ?"
cursorObj.execute(query, [login])
received_credentials = cursorObj.fetchone()

if received_credentials is None:
    password = input("It seems you're new here. Enter your NEW password: ")
    salt = os.urandom(32)  # Создаем соль для хеш функции
    original_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    print(f"Your password hash is: {original_key.hex()} (salt used: {salt.hex()})")

    password_confirmation = input("Confirm your NEW password: ")
    confirmation_key = hashlib.pbkdf2_hmac("sha256", password_confirmation.encode("utf-8"), salt, 100000)
    print(f"Your password confirmation hash is: {confirmation_key.hex()} (salt used: {salt.hex()})")

    if original_key == confirmation_key:  # сверка хешей паролей.
        print("Password has been confirmed")
        query = '''INSERT INTO users (username, password_hash, salt) VALUES (?,?,?)'''
        cursorObj.execute(query, (login, original_key, salt))
        con.commit()
    else:
        print("Password has NOT been confirmed!")
else:
    existing_salt = received_credentials[2]  # получение соли, с которой был захеширован пароль при создании учетки
    existing_password_hash = received_credentials[1]  # получение хеша пароля учетки
    password = input("You already have an account... Enter your password: ")
    entered_password_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), existing_salt, 100000)
    if entered_password_key == existing_password_hash:  # сверка хешей паролей.
        print("Access granted")
    else:
        print("Access denied")