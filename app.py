from flask import Flask, render_template, Response
from datetime import datetime
import main


app = Flask(__name__)


def start():
	data = main.output()
	return data

def get_alarm():
	return data[3]


def get_event():
	return data[0].strftime("%A, %d %B %Y | %H:%M")


def get_avg_sleep():
	return ("6.73 hours")


@app.route('/')
def index():
	condition = 3
	data = start()
	return render_template('home.html', alarm=get_alarm(), event = get_event(), avg_sleep = get_avg_sleep(), condition=condition, event_place = data[2])


@app.route('/time_feed')
def time_feed():
	def generate():
		yield datetime.now().strftime("%A, %d %B %Y | %H:%M:%S")  # return also will work
	return Response(generate(), mimetype='text')


@app.route('/alarm_feed')
def alarm_feed():
	def alarm():
		if get_alarm() == datetime.now().strftime("flask run --host=0.0.0.0%H:%M"):
			return "True"  # return also will work
		return "False"
	return Response(alarm(), mimetype='text')


data = start()

if __name__ == '__main__':
	# data = start()
	app.run(debug=False)
