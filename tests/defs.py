#!/usr/bin/python

'''
    GENERAL
'''
RTP_SERVER = "eth1"
SIP_SERVER = "eth1"
SIP_CLIENT0 = "wlan0"
SIP_CLIENT1 = "wlan1"

SIP_PROTO= "sip"
SIPS_PROTO= "sips"


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
