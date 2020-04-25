from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap
import Home
import os
USERNAME=""
di={"mode":"judge","username":"kinshuk"}
civilian={"id":"19999","name":"kinshuk","dob":"30-30-30"}
app=Flask(__name__,static_folder='static')

Bootstrap(app)
@app.route('/',methods=['GET','POST'])
def index():
	# if request.method=='POST':

	return render_template('index.html')

@app.route('/Login',methods=['GET','POST'])
def Login():
	if request.method=='POST':
		result=request.form
		print(result.items())
		username=request.form.get('username')
		password=request.form.get('password')
		print(username+" "+str(password))
		if username =='k' and password !='kinshuk':
			message='wrongpass'
			redirect(url_for('Login'))
			return render_template('Login.html',message=message)
		else:
			USERNAME=username
			di["username"]=USERNAME

			return redirect(url_for('Home'))

	return render_template('Login.html')


@app.route('/Signupas',methods=['GET','POST'])

def Signupas():

	message=None
	
	if 'client' in str(request):
		message="Client"
	if 'judge' in str(request):
		message="Judge"
	if 'lawyer' in str(request):
		message="Lawyer"
	if 'firm' in str(request):
		message="Firm"
	print(str(message))
	if message!=None:
		return redirect(url_for('Signup',message=message))
	return render_template('Signupas.html')


@app.route('/Signup/<message>',methods=['GET','POST'])

def Signup(message):
	if request.method=='GET':
		pass
	else:

		username=request.form.get('username')
		password=request.form.get('password')
		message=request.form.get('message')
		result=request.form()
		if message=='Firm':
			firmname=request.form.get('firmname')
			est=request.form.get('est')
			areaspe=request.form.get('areaspe')
			ls=request.form.get('ls')
		else:
			firstname=request.form.get('firstname')
			lastname=request.form.get('lastname')
			if message=='Client':
				dob=request.form.get('dob')
			elif message=='Lawyer':
				ed=request.form.get('ed')
				specarea=request.form.get('specarea')
				AIBE=request.form.get('AIBE')
				lis=request.form.get('lis')
			else:
				src=request.form.get('src')	
				doa=request.form.get('doa')
			print(firstname +" "+lastname+" "+password+" "+username+" "+dob+" "+message )
		if username =='k':
			message1='enter again'
			redirect(url_for('Signup'))
			return render_template('Signup.html',message=message,message1=message1)
		else:
			return redirect(url_for('Home'))

	return render_template('Signup.html',message=message)



@app.route('/Home',methods=['GET','POST'])
def Home():
	#di gets updated from sql table
	global di 
	return render_template('Home.html', di=di)
	# elif request.form['submit'] == 'judges':
	# 	return redirect(url_for('index'))
	 
#judges Routes

@app.route('/JudgePreviousJudgements',methods=['GET','POST'])
def PreviousJudgements():
		global di 
		#lawyerrequests need to be passed
		if request.method=='POST':
			result=request.form
			print(result.items())
			option=request.form.get('Option')
			details=request.form.get('Details')
			print(option)
			print('hello')
			redirect(url_for('Result'))
			return render_template('result.html',di=di)
		return render_template('PreviousJudgements.html',di=di)


@app.route('/JudgeSchedule')
def JudgeSchedule():
		global di 
		#lawyerrequests need to be passed
		return render_template('JudgeSchedule.html',di=di)

@app.route('/TrackLawyer')
def TrackLawyer():
	#Acases to be added as argument for active cases
	#Pcases to be added as argument for pending cases
	return render_template('TrackLawyer.html',di=di)

@app.route('/Records',methods=['GET','POST'])
def Records():
	if request.method=='POST':
			result=request.form
			print(result.items())
			option=request.form.get('Option')
			details=request.form.get('Details')
			print(option)
			print('hello')
			redirect(url_for('Result'))
			global civilia
			return render_template('Track.html',di=di,civilian=civilian)

	return render_template('Records.html',di=di)


@app.route('/Track')
def Track():
		return render_template('Track.html',di=di)


@app.route('/FinalVerdict')
def FinalVerdict():
		return render_template('FinalVerdict.html',di=di)

@app.route('/Setnexthearing')
def Setnexthearing():
	#change the victim statement to withdrawal requested and then judge would see it and then only transfer it.
	CASE=[{"CNRno":1111,"FilingDate":11111,"FirstHearing":2222,"NextHearing":3333,"PrevHearing":444,"Stage":5,"CourtNo":6,"VictimID":8,"VictimStmnt":"balnk","AccusedID":10,"AccusedStmnt":"killed","Acts":111}]
	return render_template('nexthearing.html',di=di,Acases=CASE)

@app.route('/ApproveCases')
def ApproveCases():
	#change the victim statement to withdrawal requested and then judge would see it and then only transfer it.

		return render_template('ApproveCases.html',di=di)

@app.route('/Cases')
def Cases():
	#change the victim statement to withdrawal requested and then judge would see it and then only transfer it.

		return render_template('Cases.html',di=di)


@app.route('/Result')
def Result():
	#change the victim statement to withdrawal requested and then judge would see it and then only transfer it.

		return render_template('result.html',di=di)



if __name__ == '__main__':
	app.run(debug=True)


