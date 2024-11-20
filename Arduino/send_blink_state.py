import serial
import time

# Set the correct serial port and baud rate
SERIAL_PORT = 'COM3'  # Change this to your actual serial port (e.g., /dev/ttyACM0 or /dev/ttyUSB0 on Linux)
BAUD_RATE = 9600

def send_blink_signal(blink: int):
    try:
        # Open the serial port
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Sending blink signal: {blink}")

            # Send the blink signal (1 or 0)
            if blink == 1:
                ser.write(b'1 \n')  # Send '1' to Arduino to turn on LED
            else:
                ser.write(b'0 \n')  # Send '0' to Arduino to turn off LED

            time.sleep(1)  # Wait a second before sending the next signal

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

if __name__ == '__main__':
    while True:
        send_blink_signal(1)  # Turn the LED on (send '1')
        time.sleep(2)  # Wait for 2 seconds
        send_blink_signal(0)  # Turn the LED off (send '0')
        time.sleep(2)  # Wait for 2 seconds
