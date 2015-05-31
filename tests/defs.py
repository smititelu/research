#!/usr/bin/python

import helps

'''
    GENERAL
'''
INTERFACE0 = "wlan0"
INTERFACE1 = "wlan1"

SIP_PROTO= "sip"
SIPS_PROTO= "sips"

BASE_CALLS = 100
BASE_PORT = 9999
BASE_NUMBER = "number"


'''
    SIPP UAC related
'''
UAC_FILE = "uac.xml"
UAC_IF_CONNECT = INTERFACE0
UAC_HW_CONNECT = helps.get_hw_addr(UAC_IF_CONNECT)
UAC_IP_CONNECT = helps.get_ip_addr(UAC_IF_CONNECT)
UAC_PORT_CONNECT = 5060
UAC_PORT_CONTROL = 8889


'''
    SIPP UAS related
'''
UAS_FILE = "uas.xml"
UAS_IF_CONNECT = INTERFACE1
UAS_HW_CONNECT = helps.get_hw_addr(UAS_IF_CONNECT)
UAS_IP_CONNECT = helps.get_ip_addr(UAS_IF_CONNECT)
UAS_PORT_CONNECT = 5060
UAS_PORT_CONTROL = 8888


'''
    SIPP related
'''
BASE_DIR_SIPP = "xml/"


'''
    SIPSAK related
'''
BASE_DIR_SIPSAK = "msg/"
BASE_BYE_FILE       = "bye.msg"
BASE_INVITE_FILE    = "invite.msg"
BASE_REINVITE_FILE  = "reinvite.msg"
