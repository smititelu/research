#!/usr/bin/python

import netifaces
import subprocess
import os

from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE

'''
    Interface API
'''
def get_hw_addr(ifname):
    try:
        hw = netifaces.ifaddresses(ifname)[AF_LINK][0]['addr']
    except StandardError, e:
#        print "Error: ", e
        hw = ""
    return hw

def get_ip_addr(ifname):
    try:
        ip = netifaces.ifaddresses(ifname)[AF_INET][0]['addr']
    except StandardError, e:
#        print "Error: ", e
        ip = ""
    return ip

'''
    Start SIPp client
'''
def sipp_uac_start(fname, host, msg_nr, rate_nr, ratep_nr):
    return subprocess.Popen([
                    "sipp",
                    "-sf", fname,
                    host,
                    "-m", msg_nr,
                    "-r", rate_nr,
                    "-rp", ratep_nr,
                    "-cid_str", "%u@%s",
#                    "-bg"  # start in background
                    ])

'''
    Start SIPp server
'''
def sipp_uas_start(fname):
    subprocess.call([
                    "sipp",
                    "-sn", "uas",
                    "-sf", fname,
                    "-bg"  # start in background
                    ])

'''
    Stop all SIPp
'''
def sipp_stop():
    subprocess.call([
                    "killall",
                    "sipp"
                    ])
