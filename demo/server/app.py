from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from the server container!'

@app.route('/getcmd', method=[''POST])
def get_cmd_and_fwd():
    if request.is_json:
        global json data=request.get_json()
        response_data= {'status':'Redirecting'}
        return jsonify(response_data), 200
    else:
        reponse_data = {'status':'Invalid Request'}
        return jsonify(response_data), 404

@app.route('', defaults)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

