from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html') 
@app.route('/about')
def about():
	return "this is about"

@app.route('/myprojects')
def myprojects():
	return "this is myprojects"
@app.route('/contact')
def contact():
	return "this is contact"

if (__name__=="__main__"):
	app.run (debug=True)