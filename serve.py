from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_stress():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return str(1)

@app.route('/', methods=['GET'])
def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return str(ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
