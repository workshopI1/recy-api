import sqlite3
from flask import g, app

DATABASE =  'workshop.db'

db = sqlite3.connect("workshop.db")
db.execute("CREATE TABLE recycling (id INTEGER, name TEXT")
db.execute("CREATE TABLE waste (Id INTEGER, name TEXT);")
db.execute("INSERT INTO waste VALUES (1,'masque'),(2,'carton');")
db.close()

