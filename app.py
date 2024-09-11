import sqlite3

# When a comment begins with (#), the number inside the parethesis is the step that section corresponds to on the assignment.

# (9) Set the Row Factory to return rows as dictionaries
connection = sqlite3.connect('example.db')
connection.row_factory = sqlite3.Row

# (2) Connect to a database (or create one if it doesn't exist)
#connection = connection.cursor()

# (2) Create a cursor object to interact with the database
cursor = connection.cursor()

# (3) Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS students
               (id INTEGER PRIMARY KEY, name TEXT, grade REAL)''')

# Clear previous queries from the Table
cursor.execute('DELETE FROM students')

# (3, 8) Insert Data into the table. Always insert data like below to avoid SQL injections attacks.
cursor.execute("INSERT INTO students (name, grade) VALUES (?,?)", ('Alice', 85.5))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Bob', 92.3))

# (4) Querying the database
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
#for row in rows:
#   print(row)

# (9) Row Factory
for row in rows:
    print(f"ID: {row['id']}, Name: {row['name']}, Grade: {row['grade']}")  # Accessing columns by name

# (7) Error Handling
try:
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")

# (5) Save/commit the changes 
connection.commit()

# (6) Closing the connection
connection.close()