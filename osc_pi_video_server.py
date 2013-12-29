#!/usr/bin/env python

from liblo import *
import sys, os

class OscPiVideoServer(ServerThread):
    def __init__(self):
        ServerThread.__init__(self, 8000)

    @make_method('/1/multipush1/1/1', None)
    #my_callback(path, args[, types[, src[, user_data]]])
    def l1_callback(self, path, args):
        # i, f, s = args
        # print "parsed label1 message '%s' with arguments: %d, %f, %s" % (path, i, f, s)

        print "received message '%s' with arguments" % path
        print self
        print args

    @make_method(None, None)
    def fallback(self, path, args):
        print "caught unknown message '%s'" % path
        print args

"""
OSCGrid class
"""

class OscGrid():
    def __init__(self):
        self.extensions = ('.mov')
        self.grid_size = 16
        self.total_pages = 1
        self.current_page = 1
        self.index = 0
        self.found_files = []
        self.grid_files = []
        OscGrid.searchFiles(self)
        OscGrid.initGrid(self)

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
                     self.found_files.append(os.path.join(root, file))

    def initGrid(self):
        for x in range(0,self.grid_size):
            for filename in self.found_files:
                print filename


"""
OKAY, BLAST OFF!
"""
try:
    server = OscPiVideoServer()
except ServerError, err:
    print str(err)
    sys.exit()

osc_grid = OscGrid()

server.start()
raw_input("press enter to quit...\n")