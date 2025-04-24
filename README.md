# CubeSatSim-Lite

**A minimal LoRa-based CubeSat simulator and ground station setup using Heltec ESP32 and Raspberry Pi.**

---

## 📡 About This Project

CubeSatSim-Lite is an open-source project that mimics a CubeSat sending telemetry data to a ground station using LoRa communication. It aims to demonstrate real-time satellite-style data exchange using affordable and accessible hardware.

### 💡 Features
- Simulated CubeSat using a **Raspberry Pi with SX126x LoRa HAT**.
- Ground station using a **Heltec V3 ESP32** with **OLED display**.
- Transmission of encrypted telemetry: `GPS`, `altitude`, `temperature`, `voltage`, `sats`, and `timestamp`.
- Real-time display of telemetry with `RSSI` and `SNR`.
- MQTT integration for sending decoded packets to a telemetry dashboard.
- Node-RED flow for decoding and visualizing telemetry (supports InfluxDB + Grafana).

---

## 🧰 Tools & Technologies
- **Arduino/PlatformIO** (for ESP32 firmware)
- **Python** (for telemetry sending script)
- **Node-RED** (data flow & payload formatting)
- **MQTT** (communication protocol)
- **InfluxDB + Grafana** (telemetry storage and visualization)

---

## 🚀 Getting Started

### Ground Station (Heltec V3)
1. Flash the provided ESP32 firmware.
2. Connect to a Wi-Fi network and MQTT server.
3. The OLED will show GS ID, RSSI, SNR, and received telemetry.

### CubeSat Simulator (Raspberry Pi)
1. Connect SX126x LoRa HAT.
2. Run the Python script to generate and transmit telemetry.
3. Adjust encryption key and LoRa parameters if needed.

---

## 📅 Data Flow

```
Raspberry Pi (LoRa TX)  --->  Heltec V3 (LoRa RX + OLED + MQTT)  --->  Node-RED  --->  InfluxDB  --->  Grafana Dashboard
```

---

## 🚀 Telemetry Example
```
{"gs_id":"CubeSatSim-GS-001","lat":38.7169,"lon":-9.1399,"alt":100,
"board":"Heltec V3","rssi":-46,"snr":12,"time_received":39791,
"telemetry":CUBESATSIM,lat:-53.5865,lon:84.1745,alt:210.0,temp:27.71,
volt:3.55,sats:5,timestamp:1745106103}
```

---

## 📌 License
MIT License

---

## 👨‍💻 Author
**Tiago Cabrita** - [LinkedIn](https://www.linkedin.com/in/electricalengineer-tiago-cabrita)

