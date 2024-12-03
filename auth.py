from flask import Blueprint, render_template, redirect, url_for, request
from models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')
