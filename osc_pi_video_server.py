#!/usr/bin/env python

from liblo import *
import sys, os

class OscPiVideoServer(ServerThread):
    def __init__(self):
        ServerThread.__init__(self, 8000)

    @make_method('/1/multipush1/1/1', '1')
    #my_callback(path, args[, types[, src[, user_data]]])
    def l1_callback(self, path, args):
        # i, f, s = args
        # print "parsed label1 message '%s' with arguments: %d, %f, %s" % (path, i, f, s)

        print "received message '%s' with arguments" % path
        print self
        print args

    @make_method('/1/multipush2/1/1', '1')
    def up_callback(self, path, args):
        print "received UP message '%s' with arguments" % path
        print self
        print args

    @make_method('/1/multipush2/1/2', '1')
    def down_callback(self, path, args):
        print "received DOWN message '%s' with arguments" % path
        print self
        print args

    @make_method(None, None)
    def fallback(self, path, args):
        print "caught unknown message '%s'" % path
        print args

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
        self.target = Address('192.168.1.2',9000)
        OscFileGrid.searchFiles(self)
        OscFileGrid.initGrid(self)

    def __iter__(self):
        return self

    def next(self):
        if self.index == len(self.found_files):
            raise StopIteration
        self.index = self.index + 1
        return self.found_files[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.found_files[self.index]

    def searchFiles(self):
        #TODO: switch that will walk mounted media
        #look for videos in home DIR!
        for root, dirs, files in os.walk('/home/'):
            for file in files:
                if file.endswith(self.extensions):
                     self.found_files.update({ os.path.join(root, file) : os.path.splitext(file)[0] })

    def getGridItemValuesAtOffset(self, offset):
        return self.found_files.values()[ offset : (offset + self.grid_size) ]

    def initGrid(self):
        labelVal = 0
        for x in range(32):
            labelVal = labelVal + 1
            label = "/1/label" + str(labelVal)
            if labelVal % 2 == 0:
                send(self.target, label, '')
            else:
                send(self.target, label, '')
            
        labelVal = 0
        for filename in self.getGridItemValuesAtOffset(0):
            labelVal = labelVal + 1
            label = "/1/label" + str(labelVal)
            send(self.target, label, filename)
            labelVal = labelVal + 1
            label = "/1/label" + str(labelVal)
            send(self.target, label, '0:00')

            print "%s filename: %s" % (label, filename)
 

"""
OKAY, BLAST OFF!
"""
try:
    server = OscPiVideoServer()
except ServerError, err:
    print str(err)
    sys.exit()

osc_grid = OscFileGrid()

server.start()
raw_input("press enter to quit...\n")