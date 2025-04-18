import time, random, json

def generate_telemetry(counter=0):
    telemetry = {
        "temp": round(22.5 + random.uniform(-0.5, 0.5), 2),
        "volt": round(3.7 + random.uniform(-0.05, 0.05), 2),
        "gyro": [
            round(random.uniform(-0.02, 0.02), 3),
            round(random.uniform(-0.02, 0.02), 3),
            round(random.uniform(-0.02, 0.02), 3)
        ],
        "counter": counter,
        "timestamp": int(time.time())
    }
    return json.dumps(telemetry)
