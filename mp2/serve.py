from flask import Flask, request, jsonify
import subprocess
import socket
from multiprocessing import Pool, cpu_count
import time

app = Flask(__name__)

PORT = 80

# Do intensive computation to stress the CPU
def stress_cpu(n):
    total = 0
    for i in range(n):
        total += i**2
    return total

# HTTP POST "/": Create a separate process for running "stress_cpu.py"
@app.route('/', methods=['POST'])
def stress_cpu_endpoint():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return jsonify({'message': 'Stressing CPU in a separate process'}), 200

# HTTP GET "/": Return the private IP address of the EC2 instance
@app.route('/', methods=['GET'])
def get_private_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    return jsonify({'private_ip': private_ip}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)