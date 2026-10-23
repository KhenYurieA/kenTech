import mysql.connector
import mysql.connector
print("Success")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="todo_app"
)

cursor = db.cursor()

while True:
    print("\n=== TODO LIST ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":

        
        task = input("Enter task: ")

        sql = "INSERT INTO tasks (task) VALUES (%s)"
        cursor.execute(sql, (task,))
        db.commit()

        print("Task added!")

    elif choice == "2":
        cursor.execute("SELECT * FROM tasks")

        tasks = cursor.fetchall()

        print("\nTasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]}")

    elif choice == "3":
        break

    else:
        print("Invalid choice!")

cursor.close()
db.close()