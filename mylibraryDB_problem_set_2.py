#!/usr/bin/python

import mysql.connector as mariadb

"""mariadb_connection = mariadb.connect(host='localhost', user='root', password='godman')

cursor = mariadb_connection.cursor()

cursor.execute("CREATE DATABASE mylibrary")
mariadb_connection.commit()"""

"""comment out the above code after creating the database"""

mariadb_connection = mariadb.connect(host='localhost', user='root', password='godman', database='mylibrary')

cursor = mariadb_connection.cursor()

cursor.execute("CREATE TABLE books (BookID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(100) NOT NULL,SeriesID INT, AuthorID INT)")

cursor.execute("CREATE TABLE authors (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(255))")

cursor.execute("CREATE TABLE series (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT)")


sql = "INSERT INTO books (Title,SeriesID,AuthorID) VALUES (%s, %s, %s)"
val = [
  ('Lord of The Rings', '1', '1'),
  ('Fellowship of The Rings', '2', '1'),
  ('The Hobbit', '4', '1'),
  ('Things Fall Apart', '1', '2')
]

cursor.executemany(sql, val)

mariadb_connection.commit()
