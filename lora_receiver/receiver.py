import os, sys
import time
from LoRaRF import SX126x

# Setup
busId = 0
csId = 0
resetPin = 18
busyPin = 20
irqPin = 16
txenPin = 6
rxenPin = -1

LoRa = SX126x()
print("[LoRa] Initializing receiver...")

if not LoRa.begin(busId, csId, resetPin, busyPin, irqPin, txenPin, rxenPin):
    raise Exception("Failed to init LoRa module.")

LoRa.setDio2RfSwitch()
LoRa.setFrequency(868000000)  # 868 MHz
LoRa.setRxGain(LoRa.RX_GAIN_BOOSTED)
LoRa.setLoRaModulation(sf=7, bw=125000, cr=5)
LoRa.setLoRaPacket(headerType=LoRa.HEADER_EXPLICIT, preambleLength=12, payloadLength=0xFF, crcType=True)
# LoRa.setSyncWord(0x3444)

print("[LoRa] RX mode ON. Listening...\n")

while True:
    LoRa.request()  # Put in RX mode
    if LoRa.wait(5000):  # Wait for a packet with timeout
        if LoRa.available():
            length = LoRa.available()
            payload = LoRa.read(length)
            rssi = LoRa.packetRssi()
            snr = LoRa.snr()
            data = ''.join([chr(c) if 32 <= c <= 126 else '.' for c in payload])  # printable ASCII
            print(f"[RECEIVED] {data.strip()} | RSSI: {rssi} dBm | SNR: {snr} dB")
        else:
            print("[WARN] Packet detected but empty or failed to decode.")
    else:
        print("[INFO] No packet received in 5 seconds.")
