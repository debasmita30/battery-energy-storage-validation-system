from battery.simulator import BatterySimulator

def test_battery():
    b = BatterySimulator()
    b.start()
    t = b.get_telemetry()
    assert "voltage" in t