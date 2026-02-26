from machine import Pin
import time

# Choose a GPIO pin you routed out to your headers (e.g., GPIO 15)
# If you connect an external LED (with a resistor) to this pin, it will blink.
test_pin = Pin(15, Pin.OUT)

print("Starting RP2040 Devboard Test...")

while True:
    # Toggle the pin state
    test_pin.toggle()
    
    # Print to the serial console over USB
    print("Tick! Devboard is running perfectly.")
    
    # Wait half a second
    time.sleep(0.5)