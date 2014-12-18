import os
import sqlite3
from datetime import datetime
from flask import (
    Flask, request, session, g, redirect, url_for,
    abort, render_template, render_template_string, flash
)
app = Flask(__name__)

ips = []

def reset_db():
    with con:
        cur = con.cursor()  
        #cur.execute("DROP TABLE IF EXISTS Posts")
        cur.execute("CREATE TABLE IF NOT EXISTS Posts(Id INTEGER PRIMARY KEY, Content TEXT, Datetime DATETIME);")
    return cur

def get_all_posts(cur):
    if request.method == 'GET':
        with con:
            cur.execute("SELECT * FROM (SELECT * FROM Posts ORDER BY Id DESC LIMIT 20) ORDER BY Id ASC;")
            content = [dict(id=row[0], content=row[1], date=row[2]) for row in cur.fetchall()]
        return content

def save_to_db(request):
    if request.method == 'POST':
        date = datetime.now()
        text = request.form['content']
        with con:
            text = 'INSERT INTO Posts(Content, Datetime) VALUES("{}", "{}");'.format(text, date)
            cur.execute(text)

@app.route('/', methods = ['POST', 'GET'])
def main():
    save_to_db(request)
    content = get_all_posts(cur)
    render = render_template('chatroom.html', content=content, header_data="test")
    return render

@app.route('/top', methods = ['GET'])
def top_frame():
    content = get_all_posts(cur)
    return render_template('top.html', content=content)

@app.route('/main', methods = ['GET', 'POST'])
def main_frame():
    save_to_db(request)
    content = get_all_posts(cur)
    return render_template('main.html', content=content)

@app.route('/left', methods = ['GET'])
def left_frame():
    content = get_all_posts(cur)
    global ips
    if request.remote_addr not in ips:
        ips.append(request.remote_addr)
    print(ips)
    users_online = len(ips)
    return render_template('left.html', content=content, users_online = users_online)
    
if __name__ == '__main__':
    con = sqlite3.connect('posts.db', check_same_thread=False)
    cur = reset_db()
   
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)