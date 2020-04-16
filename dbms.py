from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap
import os
template_dir = os.getcwd()

app=Flask(__name__,static_folder='static')

Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')


@app.route('/Signupas',methods=['GET','POST'])

def Signupas():
	return render_template('Signupas.html')


@app.route('/Signup',methods=['GET'])

def Signup():
	if 'client' in str(request):
		message="Client"
	if 'judge' in str(request):
		message="Judge"
	if 'lawyer' in str(request):
		message="Lawyer"
	if 'firm' in str(request):
		message="Firm"
	return render_template('Signup.html',message=message)



@app.route('/Login',methods=['GET','POST'])
def Login():
	return (str(request))
	# elif request.form['submit'] == 'judges':
	# 	return redirect(url_for('index'))
	return 
if __name__ == '__main__':
	app.run(debug=True)
