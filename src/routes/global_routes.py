from flask import Flask, render_template, url_for, session,redirect, session
from src import app


@app.route('/')
def index():
    if 'usercode' in session:     
        return redirect(url_for('user_list'))
    else:
        return redirect(url_for('user_login'))

