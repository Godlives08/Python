from flask import Flask, render_template, request, redirect, url_for, session
from app import config
from . import login

@login.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home.html', msg=msg) 
    else:
        msg = 'Login'
    return render_template('index.html', msg=msg) 

@login.route('/Login/', methods=['GET', 'POST'])
def index():
    msg = ''
    if 'loggedin' in session:
        return render_template('home.html', msg=msg) 

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = config.mysql.connection.cursor(config.MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE username = %s AND password = %s', (username, password,))
        usuarios = cursor.fetchone()

        if usuarios:
            session['loggedin'] = True
            session['id'] = usuarios['UserId']
            session['username'] = usuarios['Username']
            return render_template('home.html', msg=msg) 
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg) 
       
@login.route('/Login/logout')
def logout():

   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)

   return redirect(url_for('login.index'))
           

@login.route('/Login/register', methods=['GET', 'POST'])
def register():

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

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
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)
