from flask import Flask

app= Flask(__name__)

@app.route('/sum/<int:sum_a>/<int:sum_b>')
def sum_a_b(sum_a, sum_b):
	t=a*b
	return '%d' %t

if __name__=='__main__':
	app.run()
