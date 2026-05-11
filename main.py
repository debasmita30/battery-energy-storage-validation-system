from battery.simulator import BatterySimulator
from communication.can_bus import VirtualCANBus
from diagnostics.fault_engine import FaultEngine
from database.db_manager import DatabaseManager
import time

db = DatabaseManager()
battery = BatterySimulator()
bus = VirtualCANBus()
faults = FaultEngine(battery)

battery.start()
bus.start()

while True:
    telemetry = battery.get_telemetry()
    db.insert_telemetry(telemetry)
    faults.evaluate()
    print(telemetry)
    time.sleep(1)