from flask import Blueprint, request, jsonify, current_app, flash, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from .config import BaseConfig


auth = Blueprint('auth', __name__)

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Create a list of users
users = []

@auth.route('/login', methods=['GET', 'POST'])
def login():

    # Access the configuration values within the application context
    username_config = current_app.config['USERNAME']
    password_config = current_app.config['SECRET_KEY']

    # Populate the users list with the configuration values
    users.append(User(id=1, username=username_config, password=password_config))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user.username == username and user.password == password:
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('upload.upload_file'))
        flash('Invalid username or password.')
        return redirect(url_for('auth.login'))
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))