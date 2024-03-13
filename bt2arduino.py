import serial
import time

# Replace with your Bluetooth serial port
bluetooth_port = ''  # Example for macOS, may differ on other platforms

# Establish serial connection
ser = serial.Serial(bluetooth_port, 9600, timeout=1)

def send_data(data):
    ser.write(data.encode())

try:
    while True:
        # Your logic to determine the boolean value
        boolean_value = True  # Example boolean value

        # Convert boolean value to '1' or '0' and send
        send_data('1' if boolean_value else '0')

        time.sleep(1)  # Adjust delay as needed
except KeyboardInterrupt:
    ser.close()
