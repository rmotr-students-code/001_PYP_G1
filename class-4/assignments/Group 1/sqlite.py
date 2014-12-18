import sqlite3 as lite
import sys

cars = (
    (1, 'bob car', 52642, 1),
    (2, 'sam car', 57127, 1),
    (3, 'car car', 9000, 1),
    (4, 'super car', 29000, 1),
    (5, 'mega super car', 350000, 1),
    (6, 'car man', 41400, 1),
    (7, 'the car to end all cars', 21600, 2)
)
dealerships = (
    (1, "great dealer"),
    (2, "bad dealer")
)

con = lite.connect('test.db')

with con:
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Car")    
    cur.execute("DROP TABLE IF EXISTS Dealership")

    cur.execute("CREATE TABLE Dealership(Id INT, Name TEXT)")
    cur.execute("CREATE TABLE Car(Id INT, Name TEXT, Price INT, cardealership INT, FOREIGN KEY(cardealership) REFERENCES Dealership(Id))")
    cur.executemany("INSERT INTO Dealership VALUES(?, ?)", dealerships)
    cur.executemany("INSERT INTO Car VALUES(?, ?, ?, ?)", cars)
    
    cur.execute("SELECT * FROM Car WHERE cardealership = 1")

    rows = cur.fetchall()
    for row in rows:
        print row
        