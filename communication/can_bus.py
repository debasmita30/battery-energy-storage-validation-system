import queue

class VirtualCANBus:
    def __init__(self):
        self.queue = queue.Queue()

    def start(self):
        pass

    def send(self, frame):
        self.queue.put(frame)

    def receive(self):
        if not self.queue.empty():
            return self.queue.get()