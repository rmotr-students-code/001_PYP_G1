# coding=utf-8
from flask import Flask
import sqlite3
from flask import render_template
import os
app = Flask(__name__)

def connect_db():
    return sqlite3.connect('library.db')


@app.route('/')
def main():
    rows = connect_db().execute("SELECT * FROM author").fetchall()
    authors = [[name] for id, country_id, name in rows]
    return render_template('page.html', authors = authors)


if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 1234)))