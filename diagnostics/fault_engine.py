class FaultEngine:
    def __init__(self, battery):
        self.battery = battery
        self.active_faults = []

    def evaluate(self):
        t = self.battery.get_telemetry()

        self.active_faults.clear()

        if t["temperature"] > 45:
            self.active_faults.append("OVERHEAT")

        if t["voltage"] > 54:
            self.active_faults.append("OVERVOLTAGE")

        return self.active_faults