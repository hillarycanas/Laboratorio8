from flask import Flask, render_template, request
from pymongo import *
 
app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

# MongoDB Connection with PyMongo
client = MongoClient()

db = client.test
superheroes = db.superheroes

# Routes Definition
@app.route('/')
def index():
	return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
	superhero = request.form['superhero']
	password  = request.form['pass']

	hero = superheroes.find_one({ "superhero": superhero })
	if hero["alter_ego"] == password:
		return render_template('hello.html', nombre = superhero)
	return render_template('nop.html')

if __name__ == '__main__':
	app.debug = True
	app.run()


