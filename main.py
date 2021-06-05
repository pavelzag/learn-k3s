from flask import Flask, Response
import json
app = Flask(__name__)
JSON_RESPONSE = {
    "message": "all good"
}


@app.route("/")
def hello():
    return "Hello from Python!"


@app.route("/json")
def jsond():
    return Response(json.dumps(JSON_RESPONSE), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)