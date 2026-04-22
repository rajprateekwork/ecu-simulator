import pytest
import threading
import time
from ecu.ecu_simulator import ECUSimulator

@pytest.fixture(scope="session", autouse=True)
def start_ecu():
    ecu = ECUSimulator()

    thread = threading.Thread(target=ecu.run, daemon=True)
    thread.start()

    time.sleep(1)  # give ECU time to start

    yield

    # ECU stops automatically when tests end (daemon thread)