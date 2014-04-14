#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.message("HELLO!\nMAKE SELECTION")


# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT  , 'LEFT\n4'  , lcd.ON),
       (lcd.UP    , 'UP\n3'    , lcd.ON),
       (lcd.DOWN  , 'DOWN\n2'  , lcd.ON),
       (lcd.RIGHT , 'RIGHT\n1' , lcd.ON),
       (lcd.SELECT, 'SELECT\n0', lcd.ON))

def mySleep(amt=0.5):
  sleep(amt)

LOCK_OFFSET = 0
SCROLL_LOCK = False
IS_FLASHING = False
def myScrollDisplayLeft():
  global SCROLL_LOCK, LOCK_OFFSET
  if SCROLL_LOCK:
    SCROLL_LOCK = False
    mySleep(1.5)
  else:
    lcd.scrollDisplayLeft()
    if LOCK_OFFSET > 38:
      SCROLL_LOCK = True
      LOCK_OFFSET = 0
    else:
      LOCK_OFFSET = LOCK_OFFSET + 1

IDX = -1
FUNCTIONZ = [0, ['Option 0', 'action0'], 
             1, ['Option 1', 'action1'], 
             2, ['Option 2', 'action2'], 
             3, ['Option 3', 'action3'], 
             4, ['Option 4', 'action4']]
def getNextFunc():
  global IDX, FUNCTIONZ
  IDX = IDX + 2
  if IDX > len(FUNCTIONZ) - 2:
    IDX=-1
  return FUNCTIONZ[IDX][0] + '\n' + FUNCTIONZ[IDX][1]

# def getNextSubFuncUp():

# def getNextSubFuncDown():





mySleep(1)

prev = -1
while True:
  for b in btn:
    try:
      if lcd.buttonPressed(b[0]):
        if b[0] is 0:
          if prev[0] is not 0 or 1:
            lcd.clear()
            mySleep(0.2)
            lcd.message(prev[1])
            mySleep(0.2)
            lcd.clear()
            lcd.message(prev[1])
            mySleep(0.2)
            lcd.clear()
            mySleep(0.2)
            lcd.message(prev[1])
            mySleep(0.2)
            lcd.message(prev[1])
            mySleep(0.2)
            lcd.clear()
            mySleep(0.2)
            lcd.message(prev[1])
            #end flash
            lcd.clear()
            lcd.message('PROCESSING...\n  '+prev[1])
            mySleep(2)
            lcd.clear()
            lcd.message('DONE PROCESSING\nMAKE SELECTION')
            prev = -1
            break
        elif b[0] is 1:
          #RIGHT
          myScrollDisplayLeft()
          mySleep(0.1)
          break
        elif b[0] is 4:
          #LEFT BUTTON CHANGES FUNCTION 
          lcd.clear()
          lcd.message(getNextFunc())
          mySleep()
          break
        elif b[0] is 2: 
          #DOWN
          print "DONW"
          lcd.clear()
          lcd.message(b[1])
          lcd.backlight(b[2])
          prev = b
          mySleep()
          break
        elif b[0] is 3:
          #UP
          print "UP"
          lcd.clear()
          lcd.message(b[1])
          lcd.backlight(b[2])
          prev = b
          mySleep()
          break
        #this is mostly useless now...  
        elif b is not prev:
          lcd.clear()
          lcd.message(b[1])
          lcd.backlight(b[2])
          prev = b
          print b[0]
          mySleep
          break
    except TypeError:
      print "NOTHING SELECTED YET!"
      mySleep()
