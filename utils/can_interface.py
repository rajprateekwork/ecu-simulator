import can

class CANInterface:
    def __init__(self, channel='virtual_channel', bustype='virtual'):
        self.bus = can.interface.Bus(
            channel=channel,
            bustype=bustype
        )

    def send(self, arbitration_id, data):
        msg = can.Message(
            arbitration_id=arbitration_id,
            data=data,
            is_extended_id=False
        )
        self.bus.send(msg)

    def receive(self, timeout=1.0):
        return self.bus.recv(timeout)