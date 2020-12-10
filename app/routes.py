from app import app
from flask import render_template

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