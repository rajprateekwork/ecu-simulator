import time
import argparse
from utils.can_interface import CANInterface

can_if = CANInterface()

def read_speed():
    can_if.send(0x100, [0x22, 0x01])
    time.sleep(0.1)
    msg = can_if.receive()
    if msg is None:
        print("❌ No response from ECU")
        return
    print("Speed:", msg.data[2])

def read_battery():
    can_if.send(0x100, [0x22, 0x02])
    time.sleep(0.1)
    msg = can_if.receive()
    if msg is None:
        print("❌ No response from ECU")
        return
    print("Battery:", msg.data[2])

def read_errors():
    can_if.send(0x100, [0x19])
    time.sleep(0.1)
    msg = can_if.receive()
    if msg is None:
        print("❌ No response from ECU")
        return
    print("Errors:", list(msg.data[1:]))

parser = argparse.ArgumentParser()

parser.add_argument("--read-speed", action="store_true")
parser.add_argument("--read-battery", action="store_true")
parser.add_argument("--read-errors", action="store_true")

args = parser.parse_args()

if args.read_speed:
    read_speed()

elif args.read_battery:
    read_battery()

elif args.read_errors:
    read_errors()