import mysql.connector

# Connect to XAMPP MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="todo_app"
)

cursor = db.cursor()

print("=== TODO LIST ===")

name = input("Enter a task: ")

# Save task to database
sql = "INSERT INTO tasks (task) VALUES (%s)"
cursor.execute(sql, (name,))
db.commit()

print("✅ Task saved!")

# Display all tasks from database
cursor.execute("SELECT * FROM tasks")

print("\nTasks in Database:")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Task: {row[1]}")

cursor.close()
db.close()