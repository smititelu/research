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


'''
    SIP API
'''

'''
    Create a user specific SIP msg fname given the path of the base fname
'''
def msg_file_create(index, fin, fout):
    subprocess.call("cat " + fin                                + " | " +
                    "sed s/call_id/call_id" + str(index) + "/"  + " > " +
                    fout, shell=True)
#                   "sed s/service/" + number + str(index)          + "/"   +  " > " +


'''
    Delete a fname given the path
'''
def msg_file_delete(fin):
    subprocess.call("rm " + fin, shell=True)


'''
    Call bebore msg_file_send to prepare the files from a given base fname
'''
def msg_file_pre(index, dname, fname):
    fin  = dname + fname
    fout = dname + fname + str(index)
    msg_file_create(index, fin, fout)

def msg_files_pre(calls, dname, fname):
    for index in range(1, calls):
        msg_file_pre(index, dname, fname)


'''
    Call after msg_file_send to remove the files derived from a given base fname
'''
def msg_file_pos(index, dname, fname):
    fin = dname + fname + str(index)
    if os.path.isfile(fin):
        msg_file_delete(fin)

def msg_files_pos(calls, dname, fname):
    for index in range(1, calls):
        msg_file_pos(index, dname, fname)


'''
    Send a SIP message using sipsak from a given base fname
'''
def msg_file_send(index, dname, fname, uname, sport):
    port    = str(sport) + str(index)
    number  = str(uname) + str(index)
    fin     = dname + fname + str(index)
    subprocess.call([
                    "sipsak",
#                    "-vv",
                    "-l", port,
                    "-s", "sip:" + number + "@" + "127.0.1.1",
                    "-f", fin
                    ])

def msg_files_send(calls, dname, fname, uname, sport):
    for index in range(1, calls):
        msg_file_send(index, dname, fname, uname, sport)
