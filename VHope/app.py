from vhope import VHope
from src import Logger
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from functools import wraps

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'YOUR SECRET KEY HERE'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abcd1234'
app.config['MYSQL_DB'] = 'orsen_kb'
app.config['SECRET_KEY']

# Intialize MySQL
mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    status = True
    if request.method == 'POST':
        session['first'] = 0
        email = request.form["name"]
        pwd = request.form["upass"]
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("select * from users where name = %s and code = %s", (email, pwd))
        data = cur.fetchone()
        if data:
            session['logged_in'] = True
            session['id'] = data['iduser']
            session['username'] = data['name']
            session['first'] = data['first']
            session['history'] = ""
            session['move'] = ""
            session['past_utterance'] = ""

        else:
            flash('Invalid Login. Try Again', 'danger')

        if session['first'] == 1:
            cur.execute("UPDATE users SET first=0 WHERE iduser = %s", str(session['id']))
            mysql.connection.commit()
            cur.close()

        return redirect('chat')

    return render_template("login.html")

#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized. Please Login.', 'danger')
			return redirect(url_for('login'))
	return wrap

@app.route('/logout')
def logout():
    Logger.V_log("END: " + str(datetime.now()))
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('first', None)
    session.pop('history', None)
    session.pop('move', None)
    session.pop('past_utterance', None)

    return redirect(url_for('login'))

@app.route("/chat")
@is_logged_in
def chat():
    # Instantiate class
    V = VHope()
    welcome = V.welcome()
    return render_template("index.html", welcome = welcome)

@app.route("/get")
def get_bot_response():
    # userText = request.args.get('msg')
    # Instantiate class
    V = VHope()
    if session['move'] == "":
        return str(V.get_response())
    else:
        print("HISTORY: " + session['history'])

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE name = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, %s)', (username, password, '1',))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

if __name__ == "__main__":
    app.run(host = "0.0.0.0") # host="0.0.0.0" for running on own ip address