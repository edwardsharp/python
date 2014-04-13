#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.message("0123456789012345!@#$%^&*()_+~!@#\n!@#$%^&*()_+~!@")

sleep(1)

# # Cycle through backlight colors
# col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
#        lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)
# for c in col:
#     lcd.backlight(c)
#     sleep(.5)

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT  , 'PARTITION THE DRIVERZ\n#ASWEDRIVEBY'              , lcd.ON),
       (lcd.UP    , 'HEARTZ WILL MISTAKE\n#DEVILINTHEDETAILZ'     , lcd.ON),
       (lcd.DOWN  , '0123456789012345\n!@#$%^&*()_+~!@#'    , lcd.ON),
       (lcd.RIGHT , 'Purple mountainz\nrolling by', lcd.ON),
       (lcd.SELECT, 'SELECT'                    , lcd.ON))

prev = -1
while True:
    for b in btn:
        if lcd.buttonPressed(b[0]):

              if b is not prev:
                lcd.clear()
                lcd.message(b[1])
                lcd.backlight(b[2])
                prev = b
              break
