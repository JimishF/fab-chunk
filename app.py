import base64

from time import sleep
from flask import Flask, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/')
def index():
	# render the template (below) that will use JavaScript to read the stream
	return render_template('index.html')

@app.route('/read')
def stream():
	def generate():
		for i in range(500):
			
			# retval, buffer = cv2.imencode('.jpg', image)
			# jpg_as_text = base64.b64encode(buffer)

			yield '{}\n'.format(i)
			# cap.release()

			sleep(0.004)

	return app.response_class(generate(), mimetype='text/plain')

app.run(debug=True)