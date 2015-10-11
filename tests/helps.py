#!/usr/bin/python

import netifaces
import subprocess
import os
import re

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
                    "-bg"  # start in background
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

def sipp_3pcc_uac_start(fname,
        client_ip, client_port,
        client_media_ip, client_media_port,
        server_ip, server_port,
	service,
        msg_nr="1", rate_nr="1", ratep_nr="1", T2="1"):
    return subprocess.Popen([
                    "sipp",
                    server_ip+":"+server_port,
                    "-sf", fname,
                    "-i", client_ip,
                    "-p", client_port,
                    "-mi", client_media_ip,
                    "-mp", client_media_port,
                    "-s", service,
                    "-m", msg_nr,
                    "-r", rate_nr,
                    "-rp", ratep_nr,
                    "-T2", T2,
                    "-cid_str", "%u@%s",
                    "-rtp_echo",
                    "-nd",
                    "-bind_local",
                    "-bg"  # start in background
                    ])

def sipp_3pcc_uas_start(fname,
        client_ip, client_port,
        server_ip, server_port,
        server_media_ip, server_media_port,
        twin_ip, twin_port,
	service,
        msg_nr="1", rate_nr="1", ratep_nr="1", T2="1"):
    return subprocess.Popen([
                    "sipp",
                    client_ip + ":" + client_port,
                    "-3pcc", twin_ip + ":" + twin_port,
                    "-sf", fname,
                    "-i", server_ip,
                    "-p", server_port,
                    "-mi", server_media_ip,
                    "-mp", server_media_port,
                    "-s", service,
                    "-m", msg_nr,
                    "-r", rate_nr,
                    "-rp", ratep_nr,
                    "-T2", T2,
                    "-cid_str", "%u@%s",
#                    "-rtp_echo",
                    "-nd",
                    "-bind_local",
                    "-bg"  # start in background
                    ])

def tcpdump_start(fname):
    return subprocess.Popen([
                   "tcpdump",
                    "-w", fname,
                    "-i", "any",
                    "-n",
                    "-q",
                    "-t",
                    ])

def tcpdump_stop():
    subprocess.call([
                    "killall",
                    "tcpdump"
                    ])

def result_start(fname, ftitle):
    return subprocess.Popen([
                    "./result.sh " + fname + " " + '"' + ftitle + '"',
                    ], shell=True, stderr=open("/dev/null"))

def flow_start(fname, ftitle):
    return subprocess.Popen([
                    "./flow.sh " + fname + " " + '"' + ftitle + '"',
                    ], shell=True, stderr=open("/dev/null"))

'''
    Stop all SIPp
'''
def sipp_stop():
    subprocess.call([
                    "killall",
                    "sipp"
                    ])

def process_is_running(process):
    s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True
    return False
