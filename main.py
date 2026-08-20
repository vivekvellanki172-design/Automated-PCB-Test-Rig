import machine
import time
import sys

# Mapped precisely to your Wokwi workspace wiring
ROW_PINS = [2, 3, 4, 5]
COL_PINS = [6, 7, 8, 9]

KEYPAD_MAP = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Configure hardware Row Outputs
row_objects = [machine.Pin(pin, machine.Pin.OUT) for pin in ROW_PINS]
for row in row_objects:
    row.value(0)

# Configure hardware Column Inputs with internal Pull-Downs
col_objects = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in COL_PINS]

print("[WOKWI CORE] Pico Automated Test Rig Listener Active...")

while True:
    for row_idx, row_pin in enumerate(row_objects):
        row_pin.value(1) # Power current row
        
        for col_idx, col_pin in enumerate(col_objects):
            if col_pin.value() == 1:
                key = KEYPAD_MAP[row_idx][col_idx]
                
                # Print output token directly to the virtual terminal
                print(f"KEY:{key}")
                
                # Debounce: wait until button is released
                while col_pin.value() == 1:
                    time.sleep(0.05)
                    
        row_pin.value(0) # Reset row
    time.sleep(0.02)
