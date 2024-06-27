from flask import Flask
import random


rnd=str(random.randint(10000,99999))
# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL of the web application
@app.route('/')
def hello_world():
    st=f"Container ID: "+rnd
    return st

# Run the application if this file is run directly
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)
