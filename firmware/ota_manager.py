class OTAManager:
    def __init__(self):
        self.version = "1.0.0"

    def update(self, version):
        self.version = version
        return {"status":"success","version":version}