import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.can_interface import CANInterface
import logging

logging.basicConfig(level=logging.INFO)

class ECUSimulator:
    def __init__(self):
        self.can = CANInterface()

        # Simulated data
        self.speed = 60
        self.battery = 85
        self.error_codes = [1, 2]

    def process_request(self, msg):
        if msg.arbitration_id != 0x100:
            return None

        if len(msg.data) < 2:
            return [0x7F, 0x00, 0x13]  # invalid format

        service_id = msg.data[0]

        if service_id == 0x22:
            return self.handle_read_data(msg.data)

        if service_id == 0x19:
            return self.handle_read_dtc()

        return [0x7F, service_id, 0x11]  # unsupported service

    def handle_read_data(self, data):
        identifier = data[1]

        if identifier == 0x01:
            return [0x62, 0x01, self.speed & 0xFF]

        elif identifier == 0x02:
            return [0x62, 0x02, self.battery & 0xFF]
        
    def handle_read_dtc(self):
        return [0x59] + self.error_codes

    def run(self):
        print("ECU running...")
        while True:
            msg = self.can.receive()

            if msg:
            
                logging.info(f"📩 ECU RECEIVED: ID={msg.arbitration_id}, DATA={list(msg.data)}")

                response = self.process_request(msg)

                if response:
                    logging.info(f"Sending: {response}")
                    self.can.send(0x200, response)


if __name__ == "__main__":
    ecu = ECUSimulator()
    ecu.run()