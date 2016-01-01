#!/usr/bin/python

import subprocess
import os
import re


'''
	Start SIPp client
'''
def start_sipp_uac (
	fname,
	client_ip, client_port,
	client_media_ip, client_media_port,
	server_ip, server_port,
	service,
	msg_nr="1", rate_nr="1", ratep_nr="1", T2="1"
):
	return subprocess.Popen ([
		"sipp_uac",
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

'''
	Start SIPp server
'''
def start_sipp_uas (
	fname,
	client_ip, client_port,
	server_ip, server_port,
	server_media_ip, server_media_port,
	service,
	msg_nr="1", rate_nr="1", ratep_nr="1", T2="1"
):
	return subprocess.Popen ([
		"sipp_uas",
		client_ip + ":" + client_port,
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
#		"-rtp_echo",
		"-nd",
		"-bind_local",
		"-bg"  # start in background
	])

'''
	Start SIPp 3pcc client
'''
def start_sipp_uac_3pcc (
	fname,
	client_ip, client_port,
	client_media_ip, client_media_port,
	server_ip, server_port,
	service,
	msg_nr="1", rate_nr="1", ratep_nr="1", T2="1"
):
	return subprocess.Popen ([
		"sipp_uac",
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

'''
	Start SIPp 3pcc server
'''
def start_sipp_uas_3pcc (
	fname,
	client_ip, client_port,
	server_ip, server_port,
	server_media_ip, server_media_port,
	twin_ip, twin_port,
	service,
	msg_nr="1", rate_nr="1", ratep_nr="1", T2="1"
):
	return subprocess.Popen ([
		"sipp_uas",
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
#		"-rtp_echo",
		"-nd",
		"-bind_local",
		"-bg"  # start in background
	])

'''
	Stop all SIPp
'''
def stop_sipp():
	subprocess.call ([
		"killall",
		"sipp"
	])

'''
	Other script stuff
'''
def start_tcpdump(fname):
	return subprocess.Popen ([
		"tcpdump",
		"-w", fname,
		"-i", "any",
		"-n",
		"-q",
		"-t",
	])

def stop_tcpdump():
	subprocess.call ([
		"killall",
		"tcpdump"
	])

def start_callresult(fname, ftitle):
	return subprocess.Popen ([
		"./result.sh " + fname + " " + '"' + ftitle + '"',
	], shell=True, stderr=open("/dev/null"))

def start_callflow(fname, ftitle):
	return subprocess.Popen ([
		"./flow.sh " + fname + " " + '"' + ftitle + '"',
	], shell=True, stderr=open("/dev/null"))


def is_process_running(process):
	s = subprocess.Popen ([
		"ps", "aux"
	], stdout=subprocess.PIPE)
	for x in s.stdout:
		if re.search(process, x):
			return True
	return False
