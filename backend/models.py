import sqlite3
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    """
    Detects anomalies in the logs using the Isolation Forest model.
    """
    conn = sqlite3.connect('log190.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, log_level, message FROM logs")
    data = cursor.fetchall()
    conn.close()

    if not data:
        return []

    # Feature engineering: Log length and severity level as features
    features = np.array([[len(row[2]), row[1] == 'ERROR'] for row in data])
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(features)
    anomalies = model.predict(features)
    return [data[i] for i in range(len(data)) if anomalies[i] == -1]
