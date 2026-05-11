import threading
import random
import time

class BatterySimulator:
    def __init__(self):
        self.running = False
        self.telemetry = {
            "voltage": 48.0,
            "current": 12.0,
            "temperature": 29.0,
            "soc": 92,
            "soh": 98
        }

    def start(self):
        self.running = True
        threading.Thread(target=self.loop, daemon=True).start()

    def loop(self):
        while self.running:
            self.telemetry["voltage"] += random.uniform(-0.2, 0.2)
            self.telemetry["current"] += random.uniform(-1, 1)
            self.telemetry["temperature"] += random.uniform(-0.5, 0.5)
            self.telemetry["soc"] -= random.uniform(0, 0.1)
            time.sleep(1)

    def get_telemetry(self):
        return self.telemetry