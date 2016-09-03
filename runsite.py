from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<page>')
def section(page=None):
    if page in shortcuts.keys():
    	return redirect(shortcuts[page], code=302)
    else:
	    return render_template('{0}.html'.format(page), page=page)

@app.route('/writing/<titleslug>')
def blog(titleslug=None):
    return render_template('/writing/{0}.html'.format(titleslug), page="writing")

shortcuts = {
		"research-irrational-world": "/writing/research-irrational-world"
	}