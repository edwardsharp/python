#!/usr/bin/python

#edward@edwardsharp.net
#needs python 2.7+

from collections import defaultdict
import pprint

def lazy(): return defaultdict(lazy)

foo = lazy()

foo['hey']['hey']['my']['my'] = 'rock and roll can never die'

foo['out']['of']['the']['blue']
foo['and']['into']['the']['black']

foo[666]['FOO'][True][808, True, "f00", 666.666] = [6,6,6]

print "\n"
print "foo['hey']['hey']['my']['my']"
print foo['hey']['hey']['my']['my']


#print "\n"

#print "foo[666]['FOO']"
#print foo[666]['FOO'] 

#and back to a regulardict with some items() magic!
#pprint seems more useful with a plain old dict

pp = pprint.PrettyPrinter(indent=2)

def regular_dict(d):
    if isinstance(d, defaultdict):
        return dict((k, regular_dict(v)) for k, v in d.items())
    return d

regular_foo = regular_dict(foo)

print "\n"

#for k in regular_foo:
	#print foo[k]
	#print "\n"

pp.pprint(regular_foo)


