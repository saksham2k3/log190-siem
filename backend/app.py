from flask import Flask, request, jsonify
import sqlite3
from log_parser import parse_logs
from models import detect_anomalies

app = Flask(__name__)

# API Endpoint: Retrieve all logs
@app.route('/api/logs', methods=['GET'])
def get_logs():
    conn = sqlite3.connect('log190.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    conn.close()
    return jsonify(logs)

# API Endpoint: Parse and store logs
@app.route('/api/parse_logs', methods=['POST'])
def parse_and_store_logs():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    logs = parse_logs(file.read().decode('utf-8'))
    conn = sqlite3.connect('log190.db')
    cursor = conn.cursor()
    for log in logs:
        cursor.execute("INSERT INTO logs (timestamp, log_level, message) VALUES (?, ?, ?)", log)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Logs parsed and stored successfully'})

# API Endpoint: Detect anomalies in logs
@app.route('/api/anomalies', methods=['GET'])
def get_anomalies():
    anomalies = detect_anomalies()
    return jsonify(anomalies)

if __name__ == '__main__':
    app.run(debug=True)
