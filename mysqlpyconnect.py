# Import the MySQL Connector - Python
import mysql.connector


# Define main function to handle all user inputs, etc...
def main():
    # First get username and password for database connection from user
    username = str(input("User: "))
    password = str(input("Password: "))

    # Create connection to database
    db = mysql.connector.connect(
        host="localhost",
        user=f"{username}",
        password=f"{password}",
        database="bank"
    )

    choice = -1
    while (choice != 0):
        print("Welcome to Python Bank!")
        print("0. Quit Program")
        print("1. Add customer")
        print("2. Delete customer")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display customers")
        choice = int(input("Enter your choice: "))
        print()

        if (choice == 1):
            # Gets client information from user
            fname = str(input("First name: "))
            lname = str(input("Last name: "))
            bal = float(input("Starting balance: "))
            phone = str(input("Phone number: "))
            print()

            # Initialize the cursor
            cursor = db.cursor()

            # Insert information into customer table
            sql = "INSERT INTO customer (first_name, last_name, balance, phone_number) VALUES (%s, %s, %s, %s)"
            values = (fname, lname, bal, phone)
            cursor.execute(sql, values)

            # Changes made to the actual table
            db.commit()
            print(cursor.rowcount, "record inserted.")
            print()

        elif (choice == 2):
            # Get first and last name of person to delete
            fname = str(input("First name of client to delete: "))
            lname = str(input("Last name of client to delete: "))
            print()

            # Initialize cursor
            cursor = db.cursor()

            # Delete customer that matches first and last name
            sql = "DELETE FROM customer WHERE first_name = %s AND last_name = %s"
            names = (fname, lname)
            cursor.execute(sql, names)

            # Commit changes to database
            db.commit()
            print(cursor.rowcount, "record deleted.")
            print()

        elif (choice == 3):
            # Get first and last name of the account being altered
            fname = str(input("First name of account to deposit in: "))
            lname = str(input("Last name of account to deposit in: "))
            dep = float(input("Enter amount to deposit: "))

            #Initialize cursor
            cursor = db.cursor()

            # Update balance column for user that matches the first name and last name
            sql = "UPDATE customer SET balance = balance + %s WHERE first_name = %s AND last_name = %s"
            names = (dep, fname, lname)
            cursor.execute(sql, names)

            # Commit changes to database
            db.commit()
            print(cursor.rowcount, "record changed.")
            print()

        elif (choice == 4):
            # Get first and last name of account being altered
            fname = str(input("First name of account to withdraw from: "))
            lname = str(input("Last name of account to withdraw from: "))
            withdraw = float(input("Enter amount to withdraw: "))

            # initialize cursor
            cursor = db.cursor()

            # Update balance column for user that matches the first and last name
            sql = "UPDATE customer SET balance = balance - %s WHERE first_name = %s AND last_name = %s"
            names = (withdraw, fname, lname)
            cursor.execute(sql, names) 

            # Commit changes to database
            db.commit()
            print(cursor.rowcount, "record changed.")
            print()

        elif (choice == 5):
            # Display all customers and format to look readable

            # Initialize cursor
            cursor = db.cursor()

            # Select all customers/columns
            sql = "SELECT first_name, last_name, balance, phone_number FROM customer"
            cursor.execute(sql)

            # Format results into an output
            for (first_name, last_name, balance, phone_number) in cursor:
                print("Name: {} {}  Balance: ${:.2f}  Phone: {}".format(first_name, last_name, balance, phone_number))
            print()




if __name__ == "__main__":
    main()