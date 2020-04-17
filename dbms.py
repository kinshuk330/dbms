from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap
import os
template_dir = os.getcwd()

app=Flask(__name__)

Bootstrap(app)


@app.route('/')
def home():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
