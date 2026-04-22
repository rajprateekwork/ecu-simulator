import time
from utils.can_interface import CANInterface

can_if = CANInterface()

def test_read_speed():
    can_if.send(0x100, [0x22, 0x01])
    time.sleep(0.5)

    msg = can_if.receive(timeout=2)

    assert msg is not None
    assert msg.arbitration_id == 0x200
    assert msg.data[0] == 0x62
    assert msg.data[1] == 0x01

def test_read_battery():
    can_if.send(0x100, [0x22, 0x02])
    time.sleep(0.5)

    msg = can_if.receive(timeout=2)

    assert msg is not None
    assert msg.data[0] == 0x62
    assert msg.data[1] == 0x02

def test_invalid_service():
    can_if.send(0x100, [0x99, 0x01])  # unsupported service
    time.sleep(0.5)

    msg = can_if.receive(timeout=2)

    assert msg is not None
    assert msg.data[0] == 0x7F

def test_invalid_format():
    can_if.send(0x100, [0x22])  # missing data
    time.sleep(0.5)

    msg = can_if.receive(timeout=2)

    assert msg is not None
    assert msg.data[2] == 0x13  # invalid format error

