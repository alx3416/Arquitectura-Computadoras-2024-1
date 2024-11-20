import serial
import time

# Set the correct serial port and baud rate (9600 is the default in this case)
SERIAL_PORT = 'COM3'  # Change this to your actual serial port (e.g., /dev/ttyACM0 or /dev/ttyUSB0 on Linux)
BAUD_RATE = 9600


def read_blink_signal():
    try:
        # Open the serial port
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print("Listening for blink signal...")

            while True:
                if ser.in_waiting > 0:
                    # Read data from the serial port
                    line = ser.readline().decode('utf-8').strip()

                    if line == "LED ON":
                        print("LED is ON")
                    elif line == "LED OFF":
                        print("LED is OFF")

                time.sleep(0.1)  # Small delay to avoid overwhelming the CPU

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == '__main__':
    read_blink_signal()
