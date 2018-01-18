import Tkinter as tk
import tkMessageBox
from ScrolledText import ScrolledText
import time
from subprocess import call
from tkFileDialog import askopenfilename

class App(object):

  def __init__(self):
    self.window = tk.Tk()
    self.window.attributes("-fullscreen",True)
    self.window.minsize(width=320, height=240)
    self.window.maxsize(width=320, height=240)

    self.buttonFrame = tk.Frame(self.window)

    self.printButton=tk.Button(self.buttonFrame, text='PRINT!', height=2, command=self.printTxt)
    self.printButton.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)

    self.loadButton=tk.Button(self.buttonFrame, text='LOAD', height=2, command=self.load)
    self.loadButton.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

    self.exitButton=tk.Button(self.buttonFrame, text='EXIT', height=2, command=self.exitWin)
    self.exitButton.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=1)

    self.buttonFrame.pack(side=tk.TOP)

    self.filename = '/home/pi/Desktop/fly.txt'

    self.txt = ScrolledText(self.window)
    self.txt.vbar.config(width=18)
    self.txt.pack(expand=True, fill=tk.BOTH)

    self.loadFile()

    self.poll()

  def poll(self):
    if(float(self.txt.vbar.get()[1])==1):
      self.txt.see(1.0) #goto top
    else:
      self.txt.yview(tk.SCROLL,1,tk.UNITS)
    self.window.after(1000, self.poll)

  def load(self):
    self.filename = askopenfilename(initialdir="/home/pi/Desktop", title="SELECT TXT", filetypes=(("txt files","*.txt"),("all files","*.*")) )
    self.loadFile()

  def loadFile(self):
    self.txt.delete(1.0,tk.END)
    fly = open(self.filename,'r')
    self.txt.insert(1.0, fly.read())
    fly.close()

  def printTxt(self):
    call(["lp", self.filename])
    tkMessageBox.showinfo("PRINT", "it's printing!")

  def exitWin(self):
    result = tkMessageBox.askquestion("EXIT?!", "zomg, u sure?", icon='warning')
    if result == 'yes':
      self.window.quit()

app = App()
app.window.mainloop() 
