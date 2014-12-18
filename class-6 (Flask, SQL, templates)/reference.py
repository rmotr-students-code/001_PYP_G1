import os

import sqlite3
from flask import (
    Flask, request, session, g, redirect, url_for,
    abort, render_template, render_template_string, flash
)

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('example.db')


@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/hello_world')
def hello_world():
    """Simplest template string rendering"""
    html = """
        <html>
            <h1>Hello world!</h1>
        </html>
    """
    return html


@app.route('/hello')
def say_me_hello():
    """Rendering with context variables"""
    my_name = "Martin"
    html = """
        <html>
            <h1>Hello {{my_name}}!</h1>
        </html>
    """
    return render_template_string(html, my_name=my_name)


@app.route('/authors')
def list_of_authors():
    """Getting data from the database"""
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    # it will look like this:
    # [
    #   {'id': 1, 'name': 'Some author name'},
    #   {'id': 2, 'name': 'Other author name'},
    #   ...
    # ]
    html = """
        <html>
            <h1>This is the list of authors:</h1>
            <ul>
                <li>{{authors[0]['id']}}: {{authors[0]['name']}}</li>
                <li>{{authors[1]['id']}}: {{authors[1]['name']}}</li>
                <li>{{authors[2]['id']}}: {{authors[2]['name']}}</li>
                <li>{{authors[3]['id']}}: {{authors[3]['name']}}</li>
            </ul>
        </html>
    """
    return render_template_string(html, authors=authors)


@app.route('/authors_with_template')
def list_of_authors_with_template():
    """Moving the HTML code out of python modules"""
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('authors.html', authors=authors)


@app.route('/authors_with_template_engine')
def list_of_authors_with_template_engine():
    """First approach to template engines"""
    # check this out http://jinja.pocoo.org/docs/dev/templates/#for
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('authors_with_engine.html', authors=authors)    
    
    
@app.route('/authors_with_conditional')
def list_of_authors_with_conditional():
    """First approach to template engines"""
    # check this out http://jinja.pocoo.org/docs/dev/templates/#if
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('authors_with_conditional.html', authors=authors)    
    
    
@app.route('/authors_with_inheritance')
def list_of_authors_with_inheritance():
    """First approach to template inheritance"""
    # check this out http://jinja.pocoo.org/docs/dev/templates/#template-inheritance
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('authors_with_inheritance.html', authors=authors)
    

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)