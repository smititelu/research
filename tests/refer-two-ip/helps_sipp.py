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
def sipp_uac_start(fname, client, server, msg_nr, rate_nr, ratep_nr):
    return subprocess.Popen([
                    "sipp",
                    server,
                    "-sf", fname,
                    "-i", client,
                    "-p", "5060",
                    "-mi", client,
                    "-mp", "5000",
                    "-m", msg_nr,
                    "-r", rate_nr,
                    "-rp", ratep_nr,
                    "-cid_str", "callid-%u",
                    "-bind_local",
#                    "-bg"  # start in background
                    ])

'''
    Start SIPp server
'''
def sipp_uas_start(fname, server):
    subprocess.call([
                    "sipp",
                    "-sn", "uas",
                    "-sf", fname,
                    "-i", server,
                    "-p", "5060",
                    "-mi", server,
                    "-mp", "5000",
                    "-bind_local",
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
