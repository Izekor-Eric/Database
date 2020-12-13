import sqlite3
#connect to database. You can connect without create the database file.
# when you save and run the connection, the database file will be created automatically.
connection = sqlite3.connect('books.db')

# creates a cursor.
connect = connection.cursor()
#createing the database table.
# note the data type after each column. sqlite3 datatype include,
#null - check whether a column exist or not
#text - text file
#blob - store things the way it is. Like images, and mp3 file.
#integer - whole numbers
#real - decimal numbers
connect.execute("CREATE TABLE books (book text, number integer)")
records = [('Matthew', 1),('Mark', 2),('Luke', 3),('John', 4),
            ('Acts', 5),('Romans', 6),('1 Corinthians', 7),('2 Corinthians', 8),
            ('Galatians', 9),('Ephesians', 10),('philippians', 11),('Colosians', 13),
            ('1 Thessalonians', 14),('2 Thessalonians', 15),('1 Timothy', 16),('2 Timothy', 17),
            ('Titus', 18),('Philemon', 19),('Hebrews', 20),('1 Peter', 21),
            ('2 Peter', 22),('1 John', 23),('2 John', 24),
            ('3 John', 25),('Jude', 26), ('Revelations', 27)]

connect.executemany("INSERT INTO scripture VALUES (?,?)", records)
connection.commit()
#commit command
connection.commit()

#close connection
connection.close()