#!/usr/bin/env python

from ctypes import *
from ctypes.util import find_library
import sys
import os

libpostfix = '.dll' if os.name == 'nt' else '.so.1' #support both windows and linux
stemmer = CDLL(os.path.join(os.path.dirname(__file__),'./porter'+libpostfix))

def fillprototype(f, restype, argtypes): 
	f.restype = restype
	f.argtypes = argtypes

fillprototype(stemmer.trim, c_int, [c_char_p])

def stem(word):
	return word[:stemmer.trim(word.encode('utf-8'))]
