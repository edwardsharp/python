#!/usr/bin/env python
# -*- coding: utf-8 -*-

#prereq: sudo apt-get install python-liblo ffmpeg

from liblo import *
import sys, os, subprocess, re, datetime, time, argparse

class OscPiVideoServer(ServerThread):
    target_addr = '224.0.0.1'
    target = Address(target_addr,9000)
    def __init__(self):
        ServerThread.__init__(self, 8000)
        self.osc_grid = OscFileGrid()
        self.labels = OscTxtLabels()
        OscTxtLabels.initP2Labels(self.labels)
        OscTxtLabels.initP1Labels(self.labels)
        self.bg_toggle_state = False
        #aaargz
        parser = argparse.ArgumentParser(prog='PROG')
        parser.add_argument('--host', default='Host1', help='Remote OSC host lable to update. Use Host1, Host2, Host3, or Host4. Default: Host1')
        args = vars(parser.parse_args())
        self.hostarg = args['host']
        print(args['host'])

    def play_video(self, f):
        subprocess.Popen(['sudo', 'omxplayer', f])
        OscTxtLabels.setLabel(self.labels, self.hostarg, 'play: '+datetime.datetime.now().strftime("%H:%M:%S"))


    @make_method('/1', None)
    def p1_callback(self, path, args):
        OscFileGrid.initGrid(self.osc_grid)
        OscTxtLabels.initP1Labels(self.labels)
        print "ON PAGE ONE!"
    
    # 4x4 multipush grid of toggle buttons
    #ROW 1
    @make_method('/1/multipush1/1/1', None)
    def l1_callback(self, path, args):
        if args == [1.0]:
            f=OscFileGrid.getGridItemKeysAtOffset(self.osc_grid, 0)[0]
            self.play_video(f)
            print "label1 GOT A ONE: %s" % f

    @make_method('/1/multipush1/2/1', None)
    def l2_callback(self, path, args):
        if args == [1.0]:
            f=OscFileGrid.getGridItemKeysAtOffset(self.osc_grid, 0)[1]
            self.play_video(f)
            print "label2 GOT A ONE!"

    @make_method('/1/multipush1/3/1', None)
    def l3_callback(self, path, args):
        if args == [1.0]:
            f=OscFileGrid.getGridItemKeysAtOffset(self.osc_grid, 0)[2]
            self.play_video(f)
            print "label3 GOT A ONE!"

    @make_method('/1/multipush1/4/1', None)
    def l4_callback(self, path, args):
        if args == [1.0]:
            f=OscFileGrid.getGridItemKeysAtOffset(self.osc_grid, 0)[3]
            self.play_video(f)
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
            print "BG GOT A ONE!"
            if self.bg_toggle_state:
                subprocess.Popen('DISPLAY=:0 pcmanfm --wallpaper-mode=color', shell=True)
            else:
                subprocess.Popen('DISPLAY=:0 pcmanfm --wallpaper-mode=fit', shell=True)
            self.bg_toggle_state = not self.bg_toggle_state

    #start
    @make_method('/1/multipush3/2/1', None)
    def start_callback(self, path, args):
        if args == [1.0]:
            print "PING!"
            #OscTxtLabels.initP1Labels(self.labels)
            OscTxtLabels.setLabel(self.labels, self.hostarg, 'PING '+self.hostarg+': '+datetime.datetime.now().strftime("%H:%M:%S"))

    #PAGE 2
    @make_method('/2', None)
    def p2_callback(self, path, args):
        #OscFileGrid.initPage2(self.osc_grid)
        OscTxtLabels.initP1Labels()
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
    total_grid_seconds = 0

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
            a = time.strptime(match.group(), '%H:%M:%S')
            x = datetime.timedelta(hours=a.tm_hour, minutes=a.tm_min, seconds=a.tm_sec).seconds
            OscFileGrid.total_grid_seconds += x
        else:
            x = 0
        return x

    def searchFiles(self):
        #TODO: switch that will walk mounted media
        #look for videos in home DIR!
        for root, dirs, files in os.walk('/home/pi/video'):
            for file in files:
                if file.endswith(self.extensions):
                    self.found_files.update({ os.path.join(root, file) : os.path.splitext(file)[0] })
                    
                    self.found_file_times.update({ os.path.splitext(file)[0] : OscFileGrid.getVideoLength(self, os.path.join(root, file)) })

    def getGridItemValuesAtOffset(self, offset):
        return self.found_files.values()[ offset : (offset + self.grid_size) ]
    
    def getGridItemKeysAtOffset(self, offset):
        return self.found_files.keys()[ offset : (offset + self.grid_size) ]

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
            send( OscPiVideoServer.target, label, str(datetime.timedelta(seconds=self.found_file_times[filename])) )
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

        labelValz = [44, 'Current', 'Total', 41, 42, 84, 'Loop', 'StartStop', 'Host1', 'Host2', 'Host3', 'Host4']
        for label in labelValz:
            if label == 44:
                OscTxtLabels.setLabel(self, label, '')
            elif label == 'Current':
                OscTxtLabels.setLabel(self, label, '0:00')
            elif label == 'Total':
                OscTxtLabels.setLabel(self, label, str(datetime.timedelta(seconds=OscFileGrid.total_grid_seconds)) )
            elif label == 41 or label == 42 or label == 84:
                OscTxtLabels.setLabel(self, label, '')
            elif label == 'Host1' or label == 'Host2' or label == 'Host3' or label == 'Host4':
                OscTxtLabels.setLabel(self, label, '')
            elif label == 'Loop':
                OscTxtLabels.setLabel(self, label, "BG TOGG")
            elif label == 'StartStop':
                OscTxtLabels.setLabel(self, label, 'PING')


    def initP2Labels(self):

        labelValz = [85, 81]
        for label in labelValz:
            if label == 85:
                OscTxtLabels.setLabel(self, label, '/home/pi/video', 2)
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