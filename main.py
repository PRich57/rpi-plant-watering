from gpiozero import InputDevice, OutputDevice
from time import sleep

# Set up devices
moisture_sensor = InputDevice(17)
water_pump = OutputDevice(18, initial_value=False)

def water_plants():
    print("Watering the plants...")
    water_pump.on()
    sleep(10) # Run the timer for 10 seconds
    water_pump.off()
    print("Done watering.")

# Main loop
threshold = 0.3 # Adjust after seeing my sensor's dry soil reading
while True:
    if moisture_sensor.value < threshold:
        water_plants()
    sleep(3600) # Check every hour