from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap
import Home
import os
USERNAME=""
di={"mode":"officer","username":"dushyant"}
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
		if username =='dush' and password !='panch':
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
	 


# Lawyer Routes

@app.route('/FileFIR',methods=["GET","POST"])
def FileFIR():
	global di
	if request.method=="POST":
		pass 	#Read data here using request.form.get('name of entry')
	"""	FIRno
		FilingNo
		InspectorName
		Description
	"""
	return render_template('FileFIR.html',di=di)

@app.route('/SetHearing',methods=["GET","POST"])
def SetHearing():
	global di
	if request.method=="POST":
		pass 	#Read data here using request.form.get('name of entry')
	"""	Date
		CNRno
		Prev_Date
		Purpose
	"""
	return render_template('SetHearing.html',di=di)


@app.route('/ScheduleOfficer')
def ScheduleOfficer():
	global di
	schedule=[] # all cols of active cases
	return render_template('ScheduleOfficer.html',di=di,schedule=schedule)


@app.route('/DocUploadStatus',methods=["GET","POST"])
def DocUploadStatus():
	global di
	if request.method=="POST":
		DocID="empty"
		pass 	#Read data here using request.form.get('name of entry')
	"""DocID
	"""
	status="notverify"
	DocID={"ClientID":"12233","FilingNo":300000,"Document":"33333333","DocID":1222}
	return render_template('DocUploadStatus.html', di=di,DOCS=DocID,status=status)

@app.route('/VerifyUploadedDocs')
def VerifyUploadedDocs():
	global di
	return render_template('VerifyUploadedDocs.html', di=di)

                                                             




if __name__ == '__main__':
	app.run(debug=True)


	