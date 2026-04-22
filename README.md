# 🚗 ECU Simulator using Python CAN (UDS-like Diagnostic System)

## 📌 Overview

This project is a lightweight simulation of an automotive ECU (Electronic Control Unit) communication system using a virtual CAN bus in Python.

It demonstrates how a tester application communicates with an ECU using diagnostic services similar to UDS (Unified Diagnostic Services), including request/response handling, error management, and automated testing.

---

## 🎯 Key Features

- ⚡ Simulated ECU responding to diagnostic requests
- 🔌 CAN-based communication using `python-can`
- 📊 UDS-like service handling:
  - Read Data (0x22)
  - Read DTC (0x19)
- ⚠️ Error handling for invalid requests
- 🧪 Automated test suite using `pytest`
- 🔁 Multi-threaded ECU execution for simulation
- 📡 Virtual CAN bus communication

---

## 🏗️ Project Architecture
```
Tester (pytest / CLI)
↓
CAN Interface (python-can virtual bus)
↓
ECU Simulator (diagnostic logic)
↓
Response sent back over CAN
```

---

## 📁 Project Structure
```
ecu-simulator/
│
├── ecu/
│ └── ecu_simulator.py # ECU logic (request/response handling)
│
├── tester/
│ └── tester_cli.py # CLI tester for sending requests
│
├── utils/
│ └── can_interface.py # CAN communication wrapper
│
├── tests/
│ └── test_ecu.py # Automated test cases
│
├── conftest.py # pytest fixture (ECU startup)
├── main.py # Integration runner
└── README.md
```

---

## ⚙️ How It Works

1. Tester sends request
Example:
```
[0x22, 0x01]
```

2. ECU processes request
Identifies service ID
Reads internal simulated data (speed, battery, etc.)

3. ECU sends response
```
Example:
[0x62, 0x01, 60]
```
🚀 Supported Diagnostic Services

```
| Service | Description | Request Format | Response Format     |
| ------- | ----------- | -------------- | ------------------- |
| 0x22    | Read Data   | [0x22, DID]    | [0x62, DID, VALUE]  |
| 0x19    | Read DTC    | [0x19]         | [0x59, error codes] |
[0x62, 0x01, 60]
```

🧪 Running the Project

1. Install dependencies

```
pip install python-can pytest
```

2. Run tests
```
pytest -v
```

3. Run full simulation
```
python main.py
```

📊 Example Output
```
ECU running...
📩 ECU RECEIVED: ID=256, DATA=[34, 1]
Sending: [98, 1, 60]
Speed: 60
```

🧠 What I Learned
- CAN-based communication concepts
- ECU diagnostic request/response flow (UDS-like model)
- Python threading for system simulation
- pytest-based integration testing
- Debugging multi-process communication issues
- Structuring embedded-style software in Python

🔧 Future Improvements
- Add multiple ECUs (Engine, Battery, Gateway)
- Implement full UDS protocol simulation
- Add message routing layer
- Replace virtual bus with SocketCAN (Linux)
- Add logging dashboard for diagnostics

👨‍💻 Tech Stack
- Python 3.11
- python-can
- pytest
- threading (simulation)
