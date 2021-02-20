from flask import Flask, render_template, request, redirect, url_for, session
from app import config
from . import login



@login.route('/Login/', methods=['GET', 'POST'])
def index():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = config.mysql.connection.cursor(config.MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        usuarios = cursor.fetchone()
        # If account exists in accounts table in out database
        if usuarios:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = usuarios['UserId']
            session['username'] = usuarios['Username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg) 
       
@login.route('/Login/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login.index'))
           
# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@login.route('/Login/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        Nombre = request.form['Nombre']
        Username = request.form['Username']
        Useremail = request.form['Useremail']
        NivelSecurity = request.form['NivelSecurity']
        NivelAdmin = request.form['NivelAdmin']
        Activo = request.form['Activo']
        CambioPass = request.form['CambioPass']
        IPControl = request.form['IPControl']
        PasswordOld = request.form['PasswordOld']
        Password = request.form['Password']
        TimeSeccion = request.form['TimeSeccion']
        Idioma = request.form['Idioma']
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)
