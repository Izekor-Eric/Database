import sqlite3
#connect to database. You can connect without create the database file.
# when you save and run the connection, the database file will be created automatically.
connection = sqlite3.connect('customers.db')

# creates a cursor.
connect = connection.cursor()
#createing the database table.
# note the data type after each column. sqlite3 datatype include,
#null - check whether a column exist or not
#text - text file
#blob - store things the way it is. Like images, and mp3 file.
#integer - whole numbers
#real - decimal numbers
connect.execute("""CREATE TABLE customers (
        firstName text,
        lastName text,
        email text,
        phone integer
    )""")

#commit command
connection.commit()

#close connection
connection.close()