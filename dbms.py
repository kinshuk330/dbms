# Importing the libaries 
from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap
import os
# get the current working directory
template_dir = os.getcwd()

app=Flask(__name__,static_folder='static')

# Definding the functions
Bootstrap(app)
@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/handle_data',methods=['GET'])
def handle_data():
	if 'client' in str(request):
		print("client selected")
		return redirect(url_for('LoginClient'))

	
	return redirect(url_for('index'))

	print(request)
@app.route('/client',methods=['GET','POST'])
def LoginClient():
	return ("Client")
	# elif request.form['submit'] == 'judges':
	# 	return redirect(url_for('index'))
	return 
# The main function
if __name__ == '__main__':
	app.run(debug=True)
