# CubeSatSim Lite - Raspberry Pi Transmitter

This project simulates a CubeSat downlink using LoRa and a Raspberry Pi with an SX126x LoRa HAT.

## Features
- Periodic mock telemetry transmission (temp, voltage, gyro)
- LoRa configuration (SF, BW, CR, sync word)
- Compatible with SDR and Heltec V3-based ground stations

## Requirements
- Python 3.7+
- LoRaRF Python library (SX126x)
- Raspberry Pi with SX126x LoRa HAT

## Usage
```bash
bash run.sh
