from flask import Flask, render_template, request, url_for, redirect, session
from src import app
import sqlite3
from src.models import user_logic

# USERS ROUTES
@app.route('/user_new', methods=['POST', 'GET'])
def user_new():
    if request.method == 'POST':
        # Retrieve HTML Form values
        _code = request.form['code']
        _first_name = request.form['first_name']
        _last_name = request.form['last_name']
        _email = request.form['email']
        _password = request.form['password']
        _password2 = request.form['password2']

        if request.form['active'] == 'on':
            _active = 1
        else:
            _active = 0

        # Validate password
        if _password == _password2:
            # Insert User
            user_logic.insert(_code, _first_name, _last_name,
                              _email, _password, _active)
            return render_template('index.html')
        else:
            return render_template('masters/user_new.html')
    else:
        return render_template('masters/user_new.html')


""" @app.route('/user_list')
def user_list():
    if 'usercode' in session:
        cnn = sqlite3.connect('src/database/inventory.db')
        cnn.row_factory = sqlite3.Row

        cur = cnn.cursor()
        cur.execute(
            'SELECT id, code, first_name, last_name, password, active FROM Users')
        users = cur.fetchall()

        return render_template('masters/user_list.html', users=users)
    else:
        return redirect(url_for('user_login')) """


@app.route('/user_list', methods=['POST', 'GET'])
def user_list():
    if request.method == 'POST':
        if 'usercode' in session:
            if request.form['code']:
                users = user_logic.getOne(request.form['code'])
            else:
                users = user_logic.getAll()
            return render_template('masters/user_list.html', users=users)
        else:
            return redirect(url_for('user_login'))
    else:
        users = user_logic.getAll()
        return render_template('masters/user_list.html', users=users)

@app.route('/user_login', methods=['POST', 'GET'])
def user_login():
    if request.method == "POST":
        try:
            # Retrieve form fields
            _code = request.form["code"]
            _password = request.form["password"]

            # SQL Connection
            cnn = sqlite3.connect("src/database/inventory.db")
            cnn.row_factory = sqlite3.Row
            cur = cnn.cursor()
            querystring = "SELECT id FROM Users WHERE code = ? AND password = ?"
            cur.execute(querystring, (_code, _password, ))
            user = cur.fetchone()
            if user:
                session['usercode'] = _code
                return redirect(url_for('user_list'))
            else:
                session['usercode'] = ''
                return redirect(url_for('user_login'))

        except sqlite3.Error as error:
            print("Failed to read single row from sqlite table", error)

        finally:
            print("*** The SQLite connection is closed ***")
            cnn.close()
    else:
        return render_template('process/user_login.html')


@app.route('/user_logout')
def user_logout():
    if 'usercode' in session:
        session['usercode']=''
    
    return render_template('process/user_login.html')


