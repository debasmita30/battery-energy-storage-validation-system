import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("battery.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS telemetry(
                voltage REAL,
                current REAL,
                temperature REAL,
                soc REAL,
                soh REAL
            )
            '''
        )

        self.conn.commit()

    def insert_telemetry(self, t):
        self.cursor.execute(
            'INSERT INTO telemetry VALUES(?,?,?,?,?)',
            (
                t["voltage"],
                t["current"],
                t["temperature"],
                t["soc"],
                t["soh"]
            )
        )
        self.conn.commit()