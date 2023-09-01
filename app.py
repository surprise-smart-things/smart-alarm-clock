from flask import Flask, render_template, Response
from datetime import datetime



app = Flask(__name__)

def start():
	return app

def get_alarm():
	alarm = datetime(2023, 9, 1, 15, 24)
	return alarm.strftime("%A, %d %B %Y | %H:%M")


def get_event():
	return ("31 August 2023 | 09:00")


def get_avg_sleep():
	return ("6.73 hours")


@app.route('/')
def index():
	condition = 3
	return render_template('home.html', alarm=get_alarm(), event = get_event(), avg_sleep = get_avg_sleep(), condition=condition)


@app.route('/time_feed')
def time_feed():
	def generate():
		yield datetime.now().strftime("%A, %d %B %Y | %H:%M:%S")  # return also will work
	return Response(generate(), mimetype='text')


@app.route('/alarm_feed')
def alarm_feed():
	def alarm():
		if get_alarm() == datetime.now().strftime("%A, %d %B %Y | %H:%M"):
			return "True"  # return also will work
		return "False"
	return Response(alarm(), mimetype='text')


if __name__ == '__main__':
	app.run(debug=True)
