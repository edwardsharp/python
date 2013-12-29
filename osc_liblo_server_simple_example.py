#!/usr/bin/env python

from liblo import *
import sys

class MyServer(ServerThread):
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

try:
    server = MyServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()
raw_input("press enter to quit...\n")