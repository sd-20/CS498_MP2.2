import socket
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def serve():
    if request.method == 'POST':
        script_path = 'stress_cpu.py'
        process = subprocess.Popen(['python3', script_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return jsonify({"message": "cpu stress test initiated"}), 200
    else:
        return jsonify({"private_ip":socket.gethostname()}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
