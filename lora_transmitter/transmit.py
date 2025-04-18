# File: lora_transmitter/transmit.py

import os, sys
import time
from lora_transmitter.telemetry import generate_telemetry
from LoRaRF import SX126x

# Setup
busId = 0; csId = 0 
resetPin = 18; busyPin = 20; irqPin = 16; txenPin = 6; rxenPin = -1
LoRa = SX126x()
print("[LoRa] Initializing transmitter...")

if not LoRa.begin(busId, csId, resetPin, busyPin, irqPin, txenPin, rxenPin):
    raise Exception("Failed to init LoRa module.")

LoRa.setDio2RfSwitch()
LoRa.setFrequency(868000000)
LoRa.setTxPower(22, LoRa.TX_POWER_SX1262)

LoRa.setLoRaModulation(sf=7, bw=125000, cr=5)
LoRa.setLoRaPacket(headerType=LoRa.HEADER_EXPLICIT, preambleLength=12, payloadLength=64, crcType=True)
# LoRa.setSyncWord(0x3444)

counter = 0

while True:
    telemetry = generate_telemetry()
    message = f"{telemetry}|{counter}"
    print(f"Sending: {message}")

    message_bytes = [ord(c) for c in message]
    LoRa.beginPacket()
    LoRa.write(message_bytes, len(message_bytes))
    LoRa.endPacket()
    LoRa.wait()

    print(f"[SENT] #{counter} | RSSI: {LoRa.packetRssi()} | Rate: {LoRa.dataRate():.2f} B/s")
    counter = (counter + 1) % 256
    time.sleep(5)
