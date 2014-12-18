#!/usr/bin/python
# -*- coding: utf-8 -*-

# Andy: Just trying out the sqlite3 lib using this tutorial:
# http://zetcode.com/db/sqlitepythontutorial/
# Feel free to add more!

import sqlite3 as lite
import sys

con = sqlite3.connect('books.db')

with con:
    
    cur = con.cursor()  
    
    cur.execute("DROP TABLE IF EXISTS Books")
    cur.execute("DROP TABLE IF EXISTS Authors")
    
    cur.execute("CREATE TABLE Books(Id INT, Name TEXT, AuthorId INT)")
    cur.execute("INSERT INTO Books VALUES(1,'Bridget Jones''s Diary', 1)")
    cur.execute("INSERT INTO Books VALUES(2,'Pride and Prejudice (Dover Thrift Editions)',2)")
    cur.execute("INSERT INTO Books VALUES(3,'The Martian Chronicles',3)")
    
    cur.execute("CREATE TABLE Authors(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Authors VALUES(1,'Helen Fielding')")
    cur.execute("INSERT INTO Authors VALUES(2,'Jane Austen')")
    cur.execute("INSERT INTO Authors VALUES(3,'Ray Bradbury')")
    
    cur.execute("SELECT Books.Name, Authors.Name FROM Books, Authors WHERE Books.AuthorId = Authors.Id")
    
    
    rows = cur.fetchall()

    for row in rows:
        print row