from flask import Flask, render_template
from random import randint
import json

app = Flask(__name__)

# Route to serve the HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Route to provide random data
@app.route('/data')
def data():
    # Generate a random number between 0 and 10
    random_number = randint(0, 10)
    # Convert the number to JSON format
    json_data = json.dumps({'data': random_number})
    return json_data

if __name__ == '__main__':
    app.run(debug=True)