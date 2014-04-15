#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

import subprocess, glob, os, commands

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()
lcd.backlight(lcd.ON)
# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.message("HELLO!\nMAKE SELECTION")

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT  , '' ),
       (lcd.UP    , '' ),
       (lcd.DOWN  , '' ),
       (lcd.RIGHT , '' ),
       (lcd.SELECT, '' ))

def mySleep(amt=0.5):
  sleep(amt)

LOCK_OFFSET = 0
SCROLL_LOCK = False
IS_FLASHING = False
BOX_IP = commands.getoutput("/home/pi/myip.sh")

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
FUNCTIONZ = [['lxterminal', 'open .sh filez'], 
             ['pure data', 'open .pd filez'],
             ['omxplayer', 'open .mov filez'], 
             ['txt\'r', 'show .txt filez'],
             ['shutdown', 'shutdown NOW'],
             ['ipconfig', BOX_IP]]

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
SUB_FUNCTIONZ00 = []
for root, dirs, files in os.walk('/home/pi'):
  for file in files:
    if file.endswith('.sh'):
      SUB_FUNCTIONZ00.append(['lxterminal -e', os.path.join(root, file)])

SUB_IDX01 = -1
SUB_FUNCTIONZ01 = []
for root, dirs, files in os.walk('/home/pi'):
  for file in files:
    if file.endswith('.pd'):
      SUB_FUNCTIONZ01.append(['pd', os.path.join(root, file)])

SUB_IDX02 = -1
SUB_FUNCTIONZ02 = []
for root, dirs, files in os.walk('/home/pi'):
  for file in files:
    if file.endswith('.mov'):
      SUB_FUNCTIONZ02.append(['omxplayer', os.path.join(root, file)])

SUB_IDX03 = -1
SUB_FUNCTIONZ03 = []
for root, dirs, files in os.walk('/home/pi'):
  for file in files:
    if file.endswith('.txt'):
      SUB_FUNCTIONZ03.append(os.path.join(root, file))

def setNextSubFuncUp():
  global IDX, \
         SUB_IDX00, SUB_FUNCTIONZ00, \
         SUB_IDX01, SUB_FUNCTIONZ01, \
         SUB_IDX02, SUB_FUNCTIONZ02, \
         SUB_IDX03, SUB_FUNCTIONZ03
  #TODO: consider FUNCTIONZ
  if IDX is 0:
    SUB_IDX00 = SUB_IDX00 + 1
    if SUB_IDX00 > len(SUB_FUNCTIONZ00) - 1:
      SUB_IDX00 = -1
    sub_string = SUB_FUNCTIONZ00[SUB_IDX00][0] + '\n' + SUB_FUNCTIONZ00[SUB_IDX00][1]
  elif IDX is 1:
    SUB_IDX01 = SUB_IDX01 + 1
    if SUB_IDX01 > len(SUB_FUNCTIONZ01) - 1:
      SUB_IDX01 = -1
    sub_string = SUB_FUNCTIONZ01[SUB_IDX01][0] + '\n' + SUB_FUNCTIONZ01[SUB_IDX01][1]
  elif IDX is 2:
    SUB_IDX02 = SUB_IDX02 + 1
    if SUB_IDX02 > len(SUB_FUNCTIONZ02) - 1:
      SUB_IDX02 = -1
    sub_string = SUB_FUNCTIONZ02[SUB_IDX02][0] + '\n' + SUB_FUNCTIONZ02[SUB_IDX02][1]
  elif IDX is 3:
    SUB_IDX03 = SUB_IDX03 + 1
    if SUB_IDX03 > len(SUB_FUNCTIONZ03) - 1:
      SUB_IDX03 = -1
    sub_string = SUB_FUNCTIONZ03[SUB_IDX03]
  elif IDX is 4:
    sub_string = 'shutdown -h now'
  return sub_string

def setNextSubFuncDown():
  global IDX, \
         SUB_IDX00, SUB_FUNCTIONZ00, \
         SUB_IDX01, SUB_FUNCTIONZ01, \
         SUB_IDX02, SUB_FUNCTIONZ02, \
         SUB_IDX03, SUB_FUNCTIONZ03
  #TODO: consider FUNCTIONZ
  if IDX is 0:
    SUB_IDX00 = SUB_IDX00 - 1
    if SUB_IDX00 < 0:
      SUB_IDX00 = len(SUB_FUNCTIONZ00) - 1
    sub_string = SUB_FUNCTIONZ00[SUB_IDX00][0] + '\n' + SUB_FUNCTIONZ00[SUB_IDX00][1]
  elif IDX is 1:
    SUB_IDX01 = SUB_IDX01 - 1
    if SUB_IDX01 < 0:
      SUB_IDX01 = len(SUB_FUNCTIONZ01) - 1
    sub_string = SUB_FUNCTIONZ01[SUB_IDX01][0] + '\n' + SUB_FUNCTIONZ01[SUB_IDX01][1]
  elif IDX is 2:
    SUB_IDX02 = SUB_IDX02 - 1
    if SUB_IDX02 < 0:
      SUB_IDX02 = len(SUB_FUNCTIONZ02) - 1
    sub_string = SUB_FUNCTIONZ02[SUB_IDX02][0] + '\n' + SUB_FUNCTIONZ02[SUB_IDX02][1]
  elif IDX is 3:
    SUB_IDX03 = SUB_IDX03 - 1
    if SUB_IDX03 < 0:
      SUB_IDX03 = len(SUB_FUNCTIONZ03) - 1
    sub_string = SUB_FUNCTIONZ03[SUB_IDX03]
  elif IDX is 4:
    sub_string = 'shutdown -h now'
  return sub_string  

def getCurrentSubFunc():
  global IDX, \
         SUB_IDX00, SUB_FUNCTIONZ00, \
         SUB_IDX01, SUB_FUNCTIONZ01, \
         SUB_IDX02, SUB_FUNCTIONZ02, \
         SUB_IDX03, SUB_FUNCTIONZ03
  if IDX is 0:
    sub_string = SUB_FUNCTIONZ00[SUB_IDX00][0] + ' ' + SUB_FUNCTIONZ00[SUB_IDX00][1]
  elif IDX is 1:
    sub_string = SUB_FUNCTIONZ01[SUB_IDX01][0] + ' ' + SUB_FUNCTIONZ01[SUB_IDX01][1] +' &'
  elif IDX is 2:
    sub_string = SUB_FUNCTIONZ02[SUB_IDX02][0] + ' ' + SUB_FUNCTIONZ02[SUB_IDX02][1]
  elif IDX is 3:
    sub_string = SUB_FUNCTIONZ03[SUB_IDX03]
  elif IDX is 4:
    sub_string = 'shutdown -h now'
  return sub_string

def showFile(fname):
  with open(fname) as f:
    while True:
      #kindof sloppy arg passed here...
      if lcd.buttonPressed(0):
        break
      c = f.read(32)
      top, bottom = c[:16], c[16:]
      lcd.clear()
      lcd.message(top+'\n'+bottom)
      mySleep(6)

""" SELECT BUTTON """
def makeSelection(button):
  global lcd, prev, IDX, \
         SUB_IDX00, SUB_FUNCTIONZ00, \
         SUB_IDX01, SUB_FUNCTIONZ01, \
         SUB_IDX02, SUB_FUNCTIONZ02, \
         SUB_IDX03, SUB_FUNCTIONZ03
  lcd.clear()
  lcd.message(prev[1])
  mySleep(0.1)
  lcd.clear()
  mySleep(0.1)
  lcd.message(prev[1])
  mySleep(0.1)
  lcd.clear()
  mySleep(0.1)
  lcd.message(prev[1])
  #end flash
  lcd.clear()
  lcd.message(getCurrentFunc()+'\n'+getCurrentSubFunc())
  print getCurrentSubFunc()
  
  if IDX is 3:
    showFile(getCurrentSubFunc())
  else:
    #shell=True enables this function to accept stringz
    subprocess.call(getCurrentSubFunc(), shell=True)
  lcd.clear()
  lcd.message('called:\n'+getCurrentSubFunc())
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
        lcd.clear()
        lcd.message(setNextSubFuncDown())
        prev = b
        mySleep()
        break
      elif b[0] is 3:
        #UP
        lcd.clear()
        lcd.message(setNextSubFuncUp())
        prev = b
        mySleep()
        break
