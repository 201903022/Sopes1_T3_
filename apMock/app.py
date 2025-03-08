from flask import Flask, jsonify
import json
import random
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Función para generar datos dinámicos
def generate_mock_data():
    current_time = datetime.utcnow()
    containers = []

    for i in range(5):  # Genera 5 contenedores con datos aleatorios
        timestamp = current_time - timedelta(minutes=i * 5)
        container = {
            "id": f"{random.randint(1000, 9999)}abcd",
            "name": f"stress_io_{timestamp.strftime('%d-%m-%Y_%H%M%S')}",
            "cpu": f"{random.uniform(10, 90):.2f}%",
            "mem_usage": f"{random.randint(10, 500)}MiB / 8GiB",
            "mem_perc": f"{random.uniform(0.1, 10):.2f}%",
            "block_io": f"{random.randint(0, 10)}MB / {random.randint(0, 5)}MB",
            "net_io": f"{random.randint(50, 500)}KB / {random.randint(50, 500)}KB"
        }
        containers.append(container)

    return {"docker_containers": containers}
@app.route('/', methods=['GET'])
def index():
    return "API para obtener datos de contenedores Docker"

@app.route('/metrics', methods=['GET'])
def get_data():
    return jsonify(generate_mock_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
