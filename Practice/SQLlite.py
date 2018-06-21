import sqlite3
import sys

def printDB():

    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary, HireDate FROM Employees")

        for row in result:
            print()

db_conn = sqlite3.connect('test.db')

print("Database Created")

theCursor = db_conn.cursor()

db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't be created")

print("Table Created")

db_conn.execute(" INSERT INTO Employees (FName, LName, Age, Adress, Salary, HireDate) VALUES ('Derek', 'Banas', 41, '123 Main St', 500000, date('now'))))

db_conn.close()

print("Database Closed")