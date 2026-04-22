from ecu.ecu_simulator import ECUSimulator
from tester.tester_cli import read_speed
import threading
import time

# Start ECU in background thread
def start_ecu():
    ecu = ECUSimulator()
    ecu.run()

ecu_thread = threading.Thread(target=start_ecu, daemon=True)
ecu_thread.start()

# Give ECU time to start
time.sleep(1)

# Run tester
read_speed()