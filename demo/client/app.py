from flask import Flask, request, jsonify
import requests
import json
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/get_cmd_execute', methods=['POST'])
def get_cmd_execute():
    if request.is_json:
        json_data=request.get_json()
        dynamic_ip = json_data.get('ip_address')
        if dynamic_ip is None:
            response_data = {'status':'Invalid JSON'}
            return jsonify(response_data), 404
        print(dynamic_ip)
        dynamic_cmd = json_data.get('cmd')
        some_metadata = json_data.get('some_metadata')
        target_url = "http://" + str(dynamic_ip) + ":9805/cmd_execute"
        response=requests.request("POST", target_url, data=json_data)
        response_data = {'status':'ok'}
        return jsonify(response_data), 200
    else:
        
        response_data = {'status':'Invalid JSON'}
        return jsonify(response_data), 404 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

