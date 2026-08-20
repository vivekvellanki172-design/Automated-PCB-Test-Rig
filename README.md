# Automated PCB Operational Test Rig (Raspberry Pi Pico)

An automated engineering test solution designed to optimize Quality Assurance (QA) workflows for custom PCB assemblies. This repository bridges hardware design and automated functional verification using a Raspberry Pi Pico microcontroller and a Python-driven host controller interface.

## 🛠️ Key Technical Highlights
- **Hardware Design Platform:** KiCad (Schematics, Multi-layer PCB Layout, and Signal Trace Optimization).
- **Core Processing Unit:** Raspberry Pi Pico (RP2040) configured for real-time GPIO hardware interfacing.
- **User Interface Module:** 4x4 Matrix Keypad scanning configuration mapped to dedicated hardware diagnostic routines.
- **Automation Software Engine:** Object-Oriented Python script utilizing serial communication protocols for real-time telemetry extraction.
- **Data Analytics:** Automatic logging of hardware execution status, voltage tolerances, and system timestamps into a local production-ready CSV engine.

## 📁 System Architecture & Operation
1. **Keypad Interface:** The operator presses a physical keypad input on the test rig matrix.
2. **Firmware Decoupling:** The Raspberry Pi Pico scans the matrix grid and translates the mechanical input into an unblocked serial character token (`KEY:X`).
3. **Python Host Engine:** The master Python script running on the host station processes the serial interrupt token, executes an automated validation logic track (Voltage Rail sweeps, Continuity maps, or Jitter analysis), and commits the metrics directly to a QA database.

## 🚀 Future Scope
- Integrating an automated I2C/SPI digital multimeter sensor suite for dynamic analog measurement collection.
- Deploying a physical graphical dashboard utilizing Python GUI libraries (Tkinter/PyQt).
-
