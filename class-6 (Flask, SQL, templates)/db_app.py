# python-programming-course-c9-santiagobasulto_1.c9.io/
import os

import sqlite3
from flask import (
    Flask, request, session, g, redirect, url_for,
    abort, render_template, flash
)

app = Flask(__name__)
app.config.from_object('config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def list_countries_without_template():
    """Simplest template string rendering"""
    html = """
        <html>
            <h1>My authors!</h1>
            {countries}
        </html>
    """
    connection = connect_db()
    cursor = connection.execute('select id, name from country;')
    
    countries = ""

    for row in cursor.fetchall():
        _id = row[0]
        name = row[1]
        countries += "<br>{id} - {name}".format(id=_id, name=name)

    html = html.format(countries=countries)
    return html


@app.route('/countries-template')
def list_countries_with_template():
    """Simplest template string rendering"""
    connection = connect_db()
    cursor = connection.execute('select id, name from country;')
    
    countries = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('countries.html', countries=countries)


if __name__ == "__main__":
    app.debug = True

    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.logger.info("Starting flask app on %s:%s", host, port)
    app.logger.info("Database on: %s", app.config['DATABASE'])

    app.run(host=host, port=port)