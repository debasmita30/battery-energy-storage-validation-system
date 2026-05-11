from fastapi import FastAPI
from battery.simulator import BatterySimulator

app = FastAPI()

battery = BatterySimulator()
battery.start()

@app.get("/telemetry")
def telemetry():
    return battery.get_telemetry()