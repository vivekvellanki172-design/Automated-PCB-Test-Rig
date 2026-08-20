import time
import csv
import random
from datetime import datetime

class AutomatedPCBTestRigSimulator:
    def __init__(self):
        """Initializes the simulated hardware test rig environment."""
        self.log_file = "pcb_test_log.csv"
        self._initialize_csv()

    def _initialize_csv(self):
        """Creates the QA logging file with proper structural headings."""
        try:
            with open(self.log_file, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Key_Pressed", "Test_Routine", "Measured_Value", "Status"])
        except FileExistsError:
            pass

    def log_test_result(self, key, routine_name, value, status):
        """Logs simulated runtime telemetry metrics to the CSV file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, key, routine_name, value, status])
        print(f"\n[DATA LOGGED] -> {timestamp} | Key: {key} | {routine_name} | Value: {value} | Status: {status}")

    def run_voltage_test(self):
        print("\n[START] Running Voltage Rail Diagnostics...")
        time.sleep(0.8) # Simulate hardware settling delay
        measured_voltage = round(random.uniform(4.85, 5.15), 2) # Simulate live analog reading
        status = "PASS" if 4.90 <= measured_voltage <= 5.10 else "FAIL (Out of Tolerance)"
        self.log_test_result('1', "5V Voltage Rail Test", f"{measured_voltage}V", status)

    def run_continuity_test(self):
        print("\n[START] Sweeping Trace Continuity Multiplexer...")
        time.sleep(1.0)
        measured_resistance = round(random.uniform(0.1, 0.5), 2)
        self.log_test_result('2', "Trace Continuity Mapping", f"{measured_resistance} Ohms", "PASS")

    def run_signal_test(self):
        print("\n[START] Measuring SPI Clock Frequency & Jitter...")
        time.sleep(1.2)
        measured_frequency = round(random.uniform(7.8, 8.2), 2)
        status = "PASS" if 7.95 <= measured_frequency <= 8.05 else "WARN (High Jitter)"
        self.log_test_result('3', "SPI Clock Integrity", f"{measured_frequency} MHz", status)

    def emergency_halt(self):
        print("\n[!!!] EMERGENCY STOP SEQUENCE ACTIVATED [!!!]")
        print("Disengaging all automated relay arrays safely.")
        self.log_test_result('A', "EMERGENCY SYSTEM HALT", "0.0V / 0.0A", "ABORTED")

    def execute_routine(self, key):
        """Maps virtual matrix keypad selections to execution tracks."""
        actions = {
            '1': self.run_voltage_test,
            '2': self.run_continuity_test,
            '3': self.run_signal_test,
            'A': self.emergency_halt
        }
        if key in actions:
            actions[key]()
        else:
            print(f"\n[INPUT ERROR] Key '{key}' has no mapped diagnostic sequence.")

    def start_simulation(self):
        """Launches the user interactive terminal control loop."""
        print("="*60)
        print("    VIRTUAL AUTOMATED PCB TEST RIG CONTROLLER CORE ACTIVE    ")
        print("="*60)
        print("Mapped Keypad Inputs:")
        print("  [1] - 5V Voltage Rail Sweep       [2] - Trace Continuity Map")
        print("  [3] - SPI Signal Integrity Check   [A] - EMERGENCY RIG HALT")
        print("\n* Hardware Layer: Simulated Virtual Raspberry Pi Pico Core")
        print("Press Ctrl+C to terminate test simulation run safely.")
        
        try:
            while True:
                user_key = input("\nTrigger Virtual Keypad Input (1, 2, 3, A): ").strip().upper()
                if user_key:
                    self.execute_routine(user_key)
        except KeyboardInterrupt:
            print("\n\n[SHUTDOWN] Simulated Test Rig safely unmounted.")

if __name__ == "__main__":
    simulator = AutomatedPCBTestRigSimulator()
    simulator.start_simulation()
