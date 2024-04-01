from flask import Flask,jsonify
import random
import sys

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello, World!"

@app.route('/random', methods = ["POST"])

def random_function():
    response = {
        "version":"2.0",
        "template":{
            "outputs":[
                {
                    "simpleText":{
                        "text":str(random.randint(1,10))
                        }
                    }
                ]
            }
        }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000, debug = True)