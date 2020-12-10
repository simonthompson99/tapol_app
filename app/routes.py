from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

recordset = [
  {'id': 1021,
  'title': 'some stuff',
  'description': 'some other stuff'},
  {'id': 1022,
  'title': 'some different stuff',
  'description': None},  
]

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html',
    title = 'Home',
    user = {'username': 'Simon'},
    recordset = recordset)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)