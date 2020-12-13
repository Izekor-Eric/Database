import sqlite3
#connect to database. You can connect without create the database file.
# when you save and run the connection, the database file will be created automatically.
connection = sqlite3.connect('customers.db')

# creates a cursor.
connect = connection.cursor()
choice = None
while choice != "5":
    print("1) Display Customers")
    print("2) Add Customer")
    print("3) Update Customer Pay")
    print("4) Delete Customer")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display customers
        connect.execute("SELECT * FROM customers")
        print("{:<10}  {:^15}  {:^15} {:>15}".format("firstName", "lastName", "Email", "Phone"))
        print('='*65)
        for record in connect.fetchall():
            print("{:<10}  {:^15}  {:^15} {:>15}".format(record[0], record[1], record[2], record[3]))
    elif choice == "2":
        # Add New customers or Insert
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        customer = (firstName,lastName, email, phone)
        connect.execute("INSERT INTO customers VALUES (?,?,?,?)", customer)
        print("Customer succesfully added.")
        connection.commit()
    elif choice == "3":
        # Update customers email and phone
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        email = input("New Email: ")
        phone = input("New Phone: ")
        customer = ( email, phone, firstName, lastName) # Make sure order is correct
        connect.execute("UPDATE customers SET email = ?, phone = ? WHERE firstName = ? AND lastName = ?", customer)
        print("Customer informations succesfully updated")
        connection.commit()
    elif choice == "4":
        # Delete customers
        firstName = input("First Name: ")
        lastName = input("Last Name")
        customer = (firstName,lastName )
        connect.execute("DELETE FROM customers WHERE firstName = ? AND lastName = ?", customer)
        print(f'{firstName} {lastName} has been succesfully deleted from the database.')
        connection.commit()
    print()

#commit command
connection.commit()

#close connection
connection.close()