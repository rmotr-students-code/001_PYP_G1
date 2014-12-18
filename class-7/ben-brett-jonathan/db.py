import os
from flask import (
    Flask, request, session, g, redirect, url_for,
    abort, render_template, render_template_string, flash
)
app = Flask(__name__)

@app.route('/')
def main():
    hello = 'hello'
    html = """
    <html>
        <head>
            {{hello}}
        </head>
    </html>    
    """
    response = render_template_string(html, hello=hello)
    return response
    


@app.route('/page')
def test():
    dictionary = [{'id': 1, 'name': 'Bob'}, {'id': 2, 'name': 'Jim'}]
    test = render_template('page.html', authors=dictionary)
    return test
    
if __name__ == '__main__':
    # http://python-programming-course-c9-santiagobasulto_1.c9.io/
    app.debug = True
    
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    
    app.run(host=host, port=port)
    
    
