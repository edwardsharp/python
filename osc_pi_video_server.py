#!/usr/bin/env python
# -*- coding: utf-8 -*-

from liblo import *
import sys, os, subprocess, re

class OscPiVideoServer(ServerThread):
    target_addr = '192.168.1.2'
    target = Address(target_addr,9000)
    def __init__(self):
        ServerThread.__init__(self, 8000)
        self.osc_grid = OscFileGrid()
        self.labels = OscTxtLabels()
        OscTxtLabels.initP2Labels(self.labels)
        OscTxtLabels.initP1Labels(self.labels)


    @make_method('/1', None)
    def p1_callback(self, path, args):
        OscFileGrid.initGrid(self.osc_grid)
        print "ON PAGE ONE!"
    
    # 4x4 multipush grid of toggle buttons
    #ROW 1
    @make_method('/1/multipush1/1/1', None)
    def l1_callback(self, path, args):
        if args == [1.0]:
            print "label1 GOT A ONE!"

    @make_method('/1/multipush1/2/1', None)
    def l2_callback(self, path, args):
        if args == [1.0]:
            print "label2 GOT A ONE!"

    @make_method('/1/multipush1/3/1', None)
    def l3_callback(self, path, args):
        if args == [1.0]:
            print "label3 GOT A ONE!"

    @make_method('/1/multipush1/4/1', None)
    def l4_callback(self, path, args):
        if args == [1.0]:
            print "label4 GOT A ONE!"
    
    #ROW 2
    @make_method('/1/multipush1/1/2', None)
    def l5_callback(self, path, args):
        if args == [1.0]:
            print "label5 GOT A ONE!"

    @make_method('/1/multipush1/2/2', None)
    def l6_callback(self, path, args):
        if args == [1.0]:
            print "label6 GOT A ONE!"

    @make_method('/1/multipush1/3/2', None)
    def l7_callback(self, path, args):
        if args == [1.0]:
            print "label7 GOT A ONE!"

    @make_method('/1/multipush1/4/2', None)
    def l8_callback(self, path, args):
        if args == [1.0]:
            print "label8 GOT A ONE!"
    
    #ROW 3
    @make_method('/1/multipush1/1/3', None)
    def l9_callback(self, path, args):
        if args == [1.0]:
            print "label9 GOT A ONE!"

    @make_method('/1/multipush1/2/3', None)
    def l10_callback(self, path, args):
        if args == [1.0]:
            print "label10 GOT A ONE!"

    @make_method('/1/multipush1/3/3', None)
    def l11_callback(self, path, args):
        if args == [1.0]:
            print "label11 GOT A ONE!"

    @make_method('/1/multipush1/4/3', None)
    def l12_callback(self, path, args):
        if args == [1.0]:
            print "label12 GOT A ONE!"
    
    #ROW 4
    @make_method('/1/multipush1/1/4', None)
    def l13_callback(self, path, args):
        if args == [1.0]:
            print "label13 GOT A ONE!"

    @make_method('/1/multipush1/2/4', None)
    def l14_callback(self, path, args):
        if args == [1.0]:
            print "label14 GOT A ONE!"

    @make_method('/1/multipush1/3/4', None)
    def l15_callback(self, path, args):
        if args == [1.0]:
            print "label15 GOT A ONE!"

    @make_method('/1/multipush1/4/4', None)
    def l16_callback(self, path, args):
        if args == [1.0]:
            print "label16 GOT A ONE!"

    # UP!
    @make_method('/1/multipush2/1/1', None)
    def up_callback(self, path, args):
        if args == [1.0]:
            print "UP GOT A ONE!"
    #DOWN!
    @make_method('/1/multipush2/1/2', None)
    def down_callback(self, path, args):
        if args == [1.0]:
            print "DOWN GOT A ONE!"


    #loop
    @make_method('/1/multipush3/1/1', None)
    def loop_callback(self, path, args):
        if args == [1.0]:
            print "LOOP GOT A ONE!"

    #start
    @make_method('/1/multipush3/2/1', None)
    def start_callback(self, path, args):
        if args == [1.0]:
            print "START GOT A ONE!"

    #PAGE 2
    @make_method('/2', None)
    def p2_callback(self, path, args):
        #OscFileGrid.initPage2(self.osc_grid)
        OscTxtLabels.initP1Labels(self.labels)
        print "ON PAGE TWO!"

    @make_method('/2/toggle3', None)
    def toggle3_callback(self, path, args):
        if args == [1.0]:
            print "TOGG ON!"
        else: 
            print "TOGG OFF!"

    #/home/pi/videos
    #/2/label85

    @make_method('/2/push4', None)
    def push4_callback(self, path, args):
        if args == [1.0]:
            print "COPZ GONNA SHUT IT DOWN!"

    #shutdown -h now
    #/2/label81

    #DEFAULT
    @make_method(None, None)
    def fallback(self, path, args, types, src, data):
        print "caught unknown message path: %s args: %s src: %s data: %s" % (path, args, src.get_hostname(), data)

"""
OscFileGrid class
"""
class OscFileGrid():
    def __init__(self):
        self.extensions = ('.mov')
        self.grid_size = 16
        self.total_pages = 1
        self.current_page = 1
        self.index = 0
        self.found_files = {}
        self.found_file_times = {}
        OscFileGrid.searchFiles(self)
        OscFileGrid.initGrid(self)

    # def __iter__(self):
    #     return self

    # def next(self):
    #     if self.index == len(self.found_files):
    #         raise StopIteration
    #     self.index = self.index + 1
    #     return self.found_files[self.index]

    # def prev(self):
    #     if self.index == 0:
    #         raise StopIteration
    #     self.index = self.index - 1
    #     return self.found_files[self.index]


    def getVideoLength(self, file):
        p = subprocess.Popen(['ffmpeg', '-i', file],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        #pattern = re.compile(r'Stream.*Video.*([0-9]{3,})x([0-9]{3,})')
        pattern = re.compile('(?<=Duration: ).*?(?=\.)')
        match = pattern.search(stderr)
        print match.group()
        if match:
            x = match.group()
        else:
            x = 0
        return x

    def searchFiles(self):
        #TODO: switch that will walk mounted media
        #look for videos in home DIR!
        for root, dirs, files in os.walk('/home/'):
            for file in files:
                if file.endswith(self.extensions):
                    self.found_files.update({ os.path.join(root, file) : os.path.splitext(file)[0] })
                    
                    self.found_file_times.update({ os.path.splitext(file)[0] : OscFileGrid.getVideoLength(self, os.path.join(root, file)) })

    def getGridItemValuesAtOffset(self, offset):
        return self.found_files.values()[ offset : (offset + self.grid_size) ]

    def initGrid(self):
        labelVal = 0
        for x in range(32):
            labelVal = labelVal + 1
            label = "/1/label" + str(labelVal)
            if labelVal % 2 == 0:
                send(OscPiVideoServer.target, label, '')
            else:
                send(OscPiVideoServer.target, label, '')
            
        labelVal = 0
        for filename in self.getGridItemValuesAtOffset(0):
            labelVal = labelVal + 1
            label = "/1/label" + str(labelVal)
            send(OscPiVideoServer.target, label, filename)
            labelVal = labelVal + 1
            label = "/1/label" + str(labelVal)
            send(OscPiVideoServer.target, label, self.found_file_times[filename])

            print "%s filename: %s" % (label, filename)

"""
OscTxtLabels class
"""
class OscTxtLabels():
    def __init__(self):
        self.foo = ''
        OscTxtLabels.initP1Labels(self)

    def initP1Labels(self):
        #ln0 012345678901234567
        #/1/label44

        #66:66
        #/1/labelCurrent

        #66:66
        #/1/labelTotal

        #ln1 01234567890123456789012345678901234567890123456789012
        #/1/label41

        #ln2
        #/1/label42

        #ln3
        #/1/label84

        labelValz = [44, 'Current', 'Total', 41, 42, 84, 'Loop', 'StartStop']
        for label in labelValz:
            if label == 44:
                OscTxtLabels.setLabel(self, label, '###### ######')
            elif label == 'Current' or label == 'Total':
                OscTxtLabels.setLabel(self, label, '0:00')
            elif label == 41 or label == 42 or label == 84:
                OscTxtLabels.setLabel(self, label, '')
            elif label == 'Loop':
                OscTxtLabels.setLabel(self, label, "LOOP OFF")
            elif label == 'StartStop':
                OscTxtLabels.setLabel(self, label, 'PLAY')


    def initP2Labels(self):

        labelValz = [85, 81]
        for label in labelValz:
            if label == 85:
                OscTxtLabels.setLabel(self, label, '/home/', 2)
            elif label == 81:
                l = OscPiVideoServer.target_addr + '$ shutdown -h now'
                OscTxtLabels.setLabel(self, label, l, 2)
            

    def setLabel(self, whichLabel, val='', whichPage=1):
        send(OscPiVideoServer.target, '/'+str(whichPage)+'/label'+str(whichLabel), val)
        #print "%s filename: %s" % (label, filename)


"""
OKAY, BLAST OFF!
"""
try:
    server = OscPiVideoServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()
raw_input("press enter to quit...\n")