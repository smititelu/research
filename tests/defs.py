#!/usr/bin/python

'''
    GENERAL
'''
RTP_SERVER_IF = "eth1"
SIP_SERVER_IF = "eth1"
SIP_CLIENT0_IF = "wlan0"
SIP_CLIENT1_IF = "wlan1"

SIP_CLIENT0_ID = "0"
SIP_CLIENT1_ID = "1"

SIP_PROTO= "sip"
SIPS_PROTO= "sips"

'''
    3pcc
'''
SIP_3PCC_TWIN_PORT = "9999"

RTP_3PCC_SERVER0_IF = "eth1"
RTP_3PCC_SERVER0_PORT = "40000"
SIP_3PCC_SERVER0_IF = "eth1"
SIP_3PCC_SERVER0_PORT = "10000"
SIP_3PCC_SERVER0_ID = "0"

RTP_3PCC_SERVER1_IF = "eth1"
RTP_3PCC_SERVER1_PORT = "50000"
SIP_3PCC_SERVER1_IF = "eth1"
SIP_3PCC_SERVER1_PORT = "20000"
SIP_3PCC_SERVER1_ID = "1"

RTP_3PCC_CLIENT0_IF = "wlan0"
RTP_3PCC_CLIENT0_PORT = "44444"
SIP_3PCC_CLIENT0_IF = "wlan0"
SIP_3PCC_CLIENT0_PORT = "11111"
SIP_3PCC_CLIENT0_ID = "0"

RTP_3PCC_CLIENT1_IF = "wlan1"
RTP_3PCC_CLIENT1_PORT = "55555"
SIP_3PCC_CLIENT1_IF = "wlan1"
SIP_3PCC_CLIENT1_PORT = "22222"
SIP_3PCC_CLIENT1_ID = "1"

SIP_3PCC_CLIENT0_USER = "client0"
SIP_3PCC_CLIENT1_USER = "client1"
SIP_3PCC_SERVER0_USER = "server0"
SIP_3PCC_SERVER1_USER = "server1"

SIPP_3PCC_CLIENT0_FILE = "0-3pcc-uac.xml"
SIPP_3PCC_CLIENT1_FILE = "1-3pcc-uac.xml"
SIPP_3PCC_SERVER0_FILE = "0-3pcc-uas.xml"
SIPP_3PCC_SERVER1_FILE = "1-3pcc-uas.xml"
SIPP_3PCC_BASE_DIR = "xml/"


'''
    SIPP related
'''
SIPP_BASE_DIR       = "xml/"


'''
    SIPP UAC related
'''
#UAC_IF_CONNECT = INTERFACE0
#UAC_HW_CONNECT = helps.get_hw_addr(UAC_IF_CONNECT)
#UAC_IP_CONNECT = helps.get_ip_addr(UAC_IF_CONNECT)

UAC_PORT_CONNECT = 5060
UAC_PORT_CONTROL = 8889

UAC_MSG_NR          = 1000      # total calls
UAC_MSG_RATE        = 100       # calls per
UAC_MSG_RATEP       = 1000      # milisecond

UAC_INVITE_FILE     = "uac_invite.xml"
UAC_REINVITE_FILE   = "uac_reinvite.xml"
UAC_BYE_FILE        = "uac_bye.xml"
UAC_REFER_FILE      = "uac_refer.xml"


'''
    SIPP UAS related
'''
#UAS_IF_CONNECT = INTERFACE1
#UAS_HW_CONNECT = helps.get_hw_addr(UAS_IF_CONNECT)
#UAS_IP_CONNECT = helps.get_ip_addr(UAS_IF_CONNECT)

UAS_PORT_CONNECT = 5060
UAS_PORT_CONTROL = 8888

UAS_FILE = "uas.xml"


'''
    SIPSAK related
'''
SIPSAK_BASE_CALLS       = 100       # total of 1000 calls
SIPSAK_BASE_PORT        = 9999      # starting port
SIPSAK_BASE_NUMBER      = "number"  # user name used for appending

SIPSAK_BASE_DIR         = "msg/"
SIPSAK_BYE_FILE         = "bye.msg"
SIPSAK_INVITE_FILE      = "invite.msg"
SIPSAK_REINVITE_FILE    = "reinvite.msg"
