# Display DHT22 readings in 0.96 OLED display
# Programmer: Tikhala Katemecha

# Import the machine module to access the pins
import machine
# Import the time module for the intervals
import time

# OLED display initializations
import ssd1306
from machine import I2C, Pin
scl = machine.Pin(22, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(21, machine.Pin.OUT, machine.Pin.PULL_UP)
i2c = machine.I2C(scl=scl, sda=sda, freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# DHT sensor initializations
import dht
d = dht.DHT11(machine.Pin(14))
# If you will use DHT22, change it to:
# d = dht.DHT22(machine.Pin(14))

# Simple function for displaying the 
# humidity and temperature readings
# in the OLED display
def display_reads():
	# Get the DHT readings
    d.measure()
    t = d.temperature()
    h = d.humidity()
    
    # Clear the screen by populating the screen with black
    oled.fill(0)
    # Display the temperature
    oled.text('Temperature *C:', 10, 10)
    oled.text(str(t), 90, 20)
    # Display the humidity
    oled.text('Humidity %:', 10, 40)
    oled.text(str(h), 90, 50)
    # Update the screen display
    oled.show()
    
    # Or you may use the REPL
    print('Temperature:', t, '*C', ' ', 'Humidity', h, '%')


INTERVAL = 2000			# Sets the interval to 2 seconds
start = time.ticks_ms() # Records the current time
display_reads()			# Initial display	

# This is the main loop
while True:
	# This if statements will be true every
    # INTERVAL milliseconds, for this example,
    # it will trigger every 2 seconds since 
    # DHT22 samples every 2 seconds interval
    if time.ticks_ms() - start >= INTERVAL:
    	# Update the display
        display_reads()		
        # Record the new start time
        start = time.ticks_ms()