import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="todo_app"
)

cursor = db.cursor()

print("Connected to database successfully!")
