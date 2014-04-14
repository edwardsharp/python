#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()
lcd.backlight(lcd.ON)
# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.message("HELLO!\nMAKE SELECTION")

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT  , 'LEFT 4'  ),
       (lcd.UP    , 'UP 3'    ),
       (lcd.DOWN  , 'DOWN 2'  ),
       (lcd.RIGHT , 'RIGHT 1' ),
       (lcd.SELECT, 'SELECT 0'))

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

""" MAIN FUNCTIONZ """
IDX = 0
FUNCTIONZ = [['NameTop0', 'SubFunc00'], 
             ['NameTop1', 'SubFunc01'], 
             ['NameTop2', 'SubFunc02']]
def setNextFunc():
  global IDX, FUNCTIONZ
  IDX = IDX + 1
  if IDX > len(FUNCTIONZ) - 1:
    IDX = 0
  return FUNCTIONZ[IDX][0] + '\n' + FUNCTIONZ[IDX][1]

def getCurrentFunc():
  global IDX, FUNCTIONZ
  return FUNCTIONZ[IDX][0] + ' ' + FUNCTIONZ[IDX][1]

""" SUB FUNCTIONZ """
SUB_IDX00 = -1
SUB_FUNCTIONZ00 = [['name0', 'cmd0'], 
                 ['name1', 'cmd1'], 
                 ['name2', 'cmd2'], 
                 ['name3', 'cmd3'], 
                 ['name4', 'cmd4']]

def setNextSubFuncUp():
  global IDX, SUB_IDX00, SUB_FUNCTIONZ00
  #TODO: consider FUNCTIONZ
  if IDX is 0:
    SUB_IDX00 = SUB_IDX00 + 1
    if SUB_IDX00 > len(SUB_FUNCTIONZ00) - 1:
      SUB_IDX00 = -1
    sub_string = SUB_FUNCTIONZ00[SUB_IDX00][0] + '\n' + SUB_FUNCTIONZ00[SUB_IDX00][1]
  elif IDX is 1:
    sub_string = 'WAIT!'
  elif IDX is 2:
    sub_string = '2 WAIT!'
  return sub_string

def setNextSubFuncDown():
  global IDX, SUB_IDX00, SUB_FUNCTIONZ00
  #TODO: consider FUNCTIONZ
  if IDX is 0:
    SUB_IDX00 = SUB_IDX00 - 1
    if SUB_IDX00 < 0:
      SUB_IDX00 = len(SUB_FUNCTIONZ00) - 1
    sub_string = SUB_FUNCTIONZ00[SUB_IDX00][0] + '\n' + SUB_FUNCTIONZ00[SUB_IDX00][1]
  elif IDX is 1:
    sub_string = 'WAIT!'
  elif IDX is 2:
    sub_string = '2 WAIT!'
  return sub_string  

def getCurrentSubFunc():
  global IDX, SUB_IDX00, SUB_FUNCTIONZ00
  if IDX is 0:
    sub_string = SUB_FUNCTIONZ00[SUB_IDX00][0] + ' ' + SUB_FUNCTIONZ00[SUB_IDX00][1]
  elif IDX is 1:
    sub_string = 'WAIT!'
  elif IDX is 2:
    sub_string = '2 WAIT!'
  return sub_string

def makeSelection(button):
  global lcd, prev
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
  lcd.message(getCurrentFunc()+'\n'+getCurrentSubFunc())
  # mySleep(2)
  # lcd.clear()
  # lcd.message('DONE PROCESSING\nMAKE SELECTION')
  prev = -1

mySleep(1)

prev = -1
while True:
  for b in btn:
    # try:
    if lcd.buttonPressed(b[0]):
      if b[0] is 0:
        #SELECT
        if (prev is not -1):
          if prev[0] is not 0 or 1 or 4:
            makeSelection(b[0])
            break
      elif b[0] is 1:
        #RIGHT
        myScrollDisplayLeft()
        mySleep(0.1)
        break
      elif b[0] is 4:
        #LEFT BUTTON CHANGES FUNCTION 
        lcd.clear()
        lcd.message(setNextFunc())
        mySleep()
        break
      elif b[0] is 2: 
        #DOWN
        print "DONW"
        print SUB_IDX00
        lcd.clear()
        lcd.message(setNextSubFuncDown())
        prev = b
        mySleep()
        print SUB_IDX00
        break
      elif b[0] is 3:
        #UP
        print "UP"
        print SUB_IDX00
        lcd.clear()
        lcd.message(setNextSubFuncUp())
        prev = b
        mySleep()
        print SUB_IDX00
        break
      #this is mostly useless now...  
      # elif b is not prev:
      #   lcd.clear()
      #   lcd.message(b[1])
      #   lcd.backlight(b[2])
      #   prev = b
      #   print b[0]
      #   mySleep
      #   break
    # except TypeError:
    #   print "ARRRRRG! TYPE ERROR!"
    #   mySleep()
