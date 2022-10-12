# Overview

I wrote a program simulating what a bank may have to change on a database. It presents a user with different options such as, add a client, delete a client, deposit into an account, withdraw from an account, and display all accounts. Then it communicates and writes queries based on what the user inputs.

I have always wanted to learn more of integrating the two different ends of software development, the front-end and back-end. I created this project to play around with the ideas of integrating databases with basic user interaction.

[Software Demo Video](https://youtu.be/UT7EZR6TTaQ)

# Relational Database

I am using a MySQL Relational Database.

Currently, the database has one table to hold customer information. The columns include: first name, last name, balance, and contact information.

# Development Environment

I used VS Code, Git/GitHub, and the MySQL Connector for Python

I used Python and SQL (more specifically MySQL), and I used the MySQL Connector library.

# Useful Websites

* [W3Schools MySQL Python](https://www.w3schools.com/python/python_mysql_getstarted.asp)
* [MySQL Connector-Python](https://dev.mysql.com/doc/connector-python/en/)

# Future Work

* In the future, I can seperate off the contact information from the customer table and create its own table called 'contact' that could include phone number, email, etc...
* I could create another table called address to store the customer's address information.
* Another possibility is to make a 'search bar' of sorts for the python user to find a specific record/client.