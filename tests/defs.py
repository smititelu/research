#!/usr/bin/python

import helps

"""
    GENERAL
"""
INTERFACE0 = "wlan0"
INTERFACE1 = "wlan1"


"""
    UAC related
"""
UAC_IF_CONNECT = INTERFACE0
UAC_HW_CONNECT = helps.get_hw_addr(UAC_IF_CONNECT)
UAC_IP_CONNECT = helps.get_ip_addr(UAC_IF_CONNECT)
UAC_PORT_CONNECT = 5060
UAC_PORT_CONTROL = 8889


"""
    UAS related
"""
UAS_IF_CONNECT = INTERFACE1
UAS_HW_CONNECT = helps.get_hw_addr(UAS_IF_CONNECT)
UAS_IP_CONNECT = helps.get_ip_addr(UAS_IF_CONNECT)
UAS_PORT_CONNECT = 5060
UAS_PORT_CONTROL = 8888


"""
    SIPP related
"""

print UAC_IP_CONNECT + " " + UAS_IP_CONNECT
print UAC_HW_CONNECT + " " + UAS_HW_CONNECT
