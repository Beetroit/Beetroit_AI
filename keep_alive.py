from flask import Flask, request, render_template, send_from_directory
from threading import Thread
import random, os, threading, signal, time

app = Flask('Beetroit')

@app.route('/')
def home():
		return render_template('alive.html')


@app.route('/webhook', methods=['POST'])
def webhook():
	global webhook_data
	webhook_data = request.get_json()
	if webhook_data:
		print(webhook_data)
	return 'OK', 200

images=[pic for pic in os.listdir("./images")]

@app.route('/images/',methods=['GET'])
def random_image():
	# select a random image URL
	print(images)
	image_url = random.choice(images)
	return send_from_directory('./images', image_url)

def run():
	app.run(host='0.0.0.0', port=8080)

def signal_handler(sig, frame):
	print('Terminating Flask app...')
	os.kill(os.getpid(), signal.SIGINT)

def keep_alive():
	t = threading.Thread(target=run)
	t.start()
	t.join()
	signal.signal(signal.SIGINT, signal_handler)