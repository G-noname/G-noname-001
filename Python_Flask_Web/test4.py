from flask import Flask
app = Flask(__name__)

@app.route('/login',methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

if __name__=='__main__':
	app.run()
