#!/bin/bash

# Activate virtual environment
source venv/bin/activate

clear
echo "==========================================="
echo "        🚀 CubeSat Control Interface       "
echo "==========================================="
echo " Select an operation mode:"
echo
echo "1) 🛰  Full Operations"
echo "2) 🔧 Testing"
echo "3) ✅ System Verification"
echo "4) 📡 Run Telemetry Transmitter"
echo "5) 📥 Run Receiver"
echo "6) 🔙 Exit"
echo

read -p "Enter your choice [1-6]: " choice

case $choice in
    1)
	echo "[Full Operations] Alternating telemetry TX/RX..."
	while true; do
        	echo "[TX] Transmitting telemetry packets..."
        	sudo python3 -m lora_transmitter.transmit.py &
        	TX_PID=$!
        	sleep 5
        	kill $TX_PID

		echo "[RX] Listening for responses..."
		timeout 10 sudo python3 -m lora_receiver.receiver.py

		echo ""
        	echo "[Cycle Complete] Press Ctrl+C to stop or wait for next round..."
        	sleep 2
    	done
        ;;
    2)
        echo "[Testing] Options:"
        echo " a) Test transmitter only"
        echo " b) Test receiver only"
        echo " c) Back to main menu"
        read -p "Choose a test option [a-c]: " test_choice
        case $test_choice in
            a)
                sudo python3 -m lora_transmitter.transmit.py
                ;;
            b)
                sudo python3 -m lora_receiver.receiver.py
                ;;
            c)
                exec ./run.sh
                ;;
            *)
                echo "Invalid option."
                ;;
        esac
        ;;
    3)
        echo "[System Verification]"
        echo " - Checking Python version..."
        python3 --version
        echo " - Checking LoRa module access..."
        lsmod | grep spi
        echo " - Checking dependencies..."
        pip list
        echo "Done."
        ;;
    4)
        sudo python3 -m lora_transmitter.transmit.py
        ;;
    5)
        sudo python3 -m lora_receiver.receiver.py
        ;;
    6)
        echo "Exiting CubeSat CLI. Goodbye!"
        deactivate
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run again."
        ;;
esac
