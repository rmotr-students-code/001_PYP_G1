import os
import config
from flask import Flask, request

import sqlite3
import sys

app = Flask(__name__)
app.config.from_object('config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['POST', 'GET'])
def main():
    with open("page.html", "r") as page:
        page_data = page.read()
    connection = connect_db()
    if request.method == "POST":
        book = [request.form['author'], request.form['title'], request.form['isbn']]
        cursor = connection.execute("INSERT INTO book(author_id, title, isbn) VALUES({}, '{}', '{}')".format(*book))
        connection.commit()

    cursor = connection.execute("SELECT * FROM author")
    rows = cursor.fetchall()
    list_item_text = '\t\t\t\t<option value="{ID}">{AUTHOR}</option>'
    authors = []
    for row in rows:
        authors.append(list_item_text.format(ID=row[0], AUTHOR=row[2]))
    authors = '\n'.join(authors)
    page_data = page_data.format(AUTHORS=authors)
    page_data = list_books_without_template(connection, page_data)
    return page_data       


if __name__ == "__main__":
    app.debug = True

    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.logger.info("Starting flask app on %s:%s", host, port)

    app.run(host=host, port=port)