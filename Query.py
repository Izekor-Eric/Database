import sqlite3

# Connect to the music database
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

# Display content of the books table
# The '*' means all columns
cursor.execute("SELECT * FROM books")
for record in cursor.fetchall():
    print(record)
print()

# Sort the content by books number
cursor.execute("SELECT * FROM books")
for record in cursor.fetchall():
    print(record)
print()

# Show only books that have the word 'John' and sort by books number
# The '%' means match anything before or after the word 'John'
cursor.execute("SELECT * FROM scripture WHERE books LIKE '%John%'")
for record in cursor.fetchall():
    print(record)
print()

# Only show the titles from the previous query
cursor.execute("SELECT books FROM scripture WHERE books LIKE '%John%'")
for record in cursor.fetchall():
    print(record)
print()

# Close the database connection before exiting
connection.close()