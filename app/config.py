from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'sklejdyriwkyfaioskdgfokdghfpiuyedpifsdhfpkj'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'python'
app.config['MYSQL_PASSWORD'] = 'python2021'
app.config['MYSQL_DATABASE_PORT'] = '3306'
app.config['MYSQL_DB'] = 'inventariopy_001'

mysql = MySQL(app)