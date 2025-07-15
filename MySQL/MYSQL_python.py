import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="__Gavin__2005",
    database="college"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

# Insert a row
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("John", 21))
conn.commit()

#  Fetch and print
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()
