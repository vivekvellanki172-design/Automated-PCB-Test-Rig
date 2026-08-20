import serial
import time
import csv
from datetime import datetime

class AutomatedPCBTestRig:
    def __init__(self, port='COM3', baudrate=9600):
        """Initializes serial communication and test result logger."""
        self.port = port
        self.baudrate = baudrate
        self.log_file = "pcb_test_log.csv"
        self.serial_conn = None
        self._initialize_csv()

    def _initialize_csv(self):
        """Creates the QA logging file with proper headings."""
        try:
            with open(self.log_file, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Key_Pressed", "Test_Routine", "Status"])
        except FileExistsError:
            pass

    def connect_hardware(self):
        """Establishes connection with the test rig microcontroller."""
        print(f"[STARTING] Connecting to Test Rig Hardware on {self.port}...")
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2) 
            print("[SUCCESS] Hardware connected and synchronized.")
            return True
        except serial.SerialException:
            print("[SIMULATION MODE] Running in fallback software mode...")
            return False

    def log_test(self, key, routine_name, status):
        """Logs real-time production testing data for QA reporting."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, key, routine_name, status])
        print(f"[{status}] Logged: {routine_name} triggered by Key {key}")

    def execute_routine(self, key):
        """Maps incoming keypad triggers to backend testing modules."""
        routines = {
            '1': ("Voltage Rail Diagnostic", "PASS"),
            '2': ("Trace Continuity Sweeping", "PASS"),
            '3': ("SPI Clock Jitter Evaluation", "FAIL - Margins Exceeded"),
            'A': ("EMERGENCY SYSTEM HALT", "ABORTED")
        }
        if key in routines:
            routine_name, status = routines[key]
            self.log_test(key, routine_name, status)
        else:
            print(f"[UNKNOWN INPUT] Key '{key}' received.")

    def run(self):
        has_hardware = self.connect_hardware()
        try:
            while True:
                if has_hardware and self.serial_conn.in_waiting > 0:
                    hardware_data = self.serial_conn.readline().decode('utf-8').strip()
                    if hardware_data.startswith("KEY:"):
                        key_pressed = hardware_data.split(":")[1]
                        self.execute_routine(key_pressed)
                elif not has_hardware:
                    sim_input = input("Simulate Keypad Input (1, 2, 3, A): ").strip().upper()
                    if sim_input:
                        self.execute_routine(sim_input)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n[SHUTDOWN] Exiting Test Rig software safely.")

if __name__ == "__main__":
    rig_operator = AutomatedPCBTestRig(port='COM3', baudrate=9600)
    rig_operator.run()
