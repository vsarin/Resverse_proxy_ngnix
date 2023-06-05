from flask import Flask, request, jsonify
import requests
import json
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/cmd_execute', methods=['POST'])
def get_cmd_execute():
    if request.is_json:
        json_data=request.get_json()
        dynamic_ip = json_data.get('ip_address')
        dynamic_cmd = json_data.get('cmd')
        print(dynamic_cmd)
        some_metadata = json_data.get('some_metadata')
        output = subprocess.run(dynamic_cmd, shell=True)
        x=output.returncode
        print(x)
        if x == 0:
            response_data = {'status':'ok'}
            return jsonify(response_data), 200
        else:
            response_data = {'status':'Command Failed'}
            return jsonify(response_data), 404 
    else:
        response_data = {'status':'Command Failed'}
        return jsonify(response_data), 404 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9805)

