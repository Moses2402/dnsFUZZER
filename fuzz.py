#!/usr/bin/python

from scapy.all import *

send(IP(dst="8.8.8.8")/UDP()/fuzz(DNS()),loop=1)
