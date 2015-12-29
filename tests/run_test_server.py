import sys
import helps
import defs
import os
import time
import re


test_list = ['refer-3pcc', 'reinvite-3pcc', 'reinvite-proactive-3pcc', 'reinvite-proactive-extension-3pcc', 'join-3pcc', 'reinvite-uac', 'reinvite-uas']

# check if given number of calls is given as argument
if len(sys.argv) > 5:
    try:
        test_name = str(sys.argv[1])
        test_title = str(sys.argv[2])
        msg_nr = int(sys.argv[3])
        rate_nr = int(sys.argv[4])
        ratep_nr = int(sys.argv[5])
    except Exception:
        print("Usage: sudo python run_test.py [test_name] [test_title] [msg_nr] [rate_nr] [ratep_nr]")
        exit()

if not any(test_name in item for item in test_list):
    print "Test " + test_name + " not found!"
    exit()

# global vars
sip_server0_user, sip_server0_id, sip_server0_if, rtp_server0_if, sip_server0_port, rtp_server0_port, sip_server0_ip, rtp_server0_ip, sip_server0_file = "", "", "", "", "", "", "", "", ""
sip_server1_user, sip_server1_id, sip_server1_if, rtp_server1_if, sip_server1_port, rtp_server1_port, sip_server1_ip, rtp_server1_ip, sip_server1_file = "", "", "", "", "", "", "", "", ""

sip_client0_user, sip_client0_id, sip_client0_if, rtp_client0_if, sip_client0_port, rtp_client0_port, sip_client0_ip, rtp_client0_ip, sip_client0_file = "", "", "", "", "", "", "", "", ""
sip_client1_user, sip_client1_id, sip_client1_if, rtp_client1_if, sip_client1_port, rtp_client1_port, sip_client1_ip, rtp_client1_ip, sip_client1_file = "", "", "", "", "", "", "", "", ""

sip_twin_port = 0 

order= test_name + "/order"
result = test_name + "/time.out"

# cleanup
try:
    os.remove(order)
    os.remove(result)
except OSError:
    pass


'''
print "SERVER0 USER: " + sip_server0_user + " " + sip_server0_file + " " + sip_server0_ip + ":" + sip_server0_port + " " + rtp_server0_ip + ":" + rtp_server0_port
print "SERVER1 USER: " + sip_server1_user + " " + sip_server1_file + " " + sip_server1_ip + ":" + sip_server1_port + " " + rtp_server1_ip + ":" + rtp_server1_port
print "CLIENT0 USER: " + sip_client0_user + " " + sip_client0_file + " " + sip_client0_ip + ":" + sip_client0_port + " " + rtp_client0_ip + ":" + rtp_client0_port
print "CLIENT1 USER: " + sip_client1_user + " " + sip_client1_file + " " + sip_client1_ip + ":" + sip_client1_port + " " + rtp_client1_ip + ":" + rtp_client1_port
print "TWIN port: " + sip_twin_port
'''

if re.search('3pcc', test_name):
    # users
    sip_server0_user = defs.SIP_3PCC_SERVER0_USER
    sip_server1_user = defs.SIP_3PCC_SERVER1_USER

    sip_client0_user = defs.SIP_3PCC_CLIENT0_USER
    sip_client1_user = defs.SIP_3PCC_CLIENT1_USER

    # id
    sip_server0_id = defs.SIP_3PCC_SERVER0_ID
    sip_server1_id = defs.SIP_3PCC_SERVER1_ID

    sip_client0_id = defs.SIP_3PCC_CLIENT0_ID
    sip_client1_id = defs.SIP_3PCC_CLIENT1_ID

    # if
    sip_server0_if = defs.SIP_3PCC_SERVER0_IF
    sip_server1_if = defs.SIP_3PCC_SERVER1_IF

    rtp_server0_if = defs.RTP_3PCC_SERVER0_IF
    rtp_server1_if = defs.RTP_3PCC_SERVER1_IF

    sip_client0_if = defs.SIP_3PCC_CLIENT0_IF
    sip_client1_if = defs.SIP_3PCC_CLIENT1_IF

    rtp_client0_if = defs.RTP_3PCC_CLIENT0_IF
    rtp_client1_if = defs.RTP_3PCC_CLIENT1_IF

    # port
    sip_server0_port = defs.SIP_3PCC_SERVER0_PORT
    sip_server1_port = defs.SIP_3PCC_SERVER1_PORT

    rtp_server0_port = defs.RTP_3PCC_SERVER0_PORT
    rtp_server1_port = defs.RTP_3PCC_SERVER1_PORT

    sip_client0_port = defs.SIP_3PCC_CLIENT0_PORT
    sip_client1_port = defs.SIP_3PCC_CLIENT1_PORT

    rtp_client0_port = defs.RTP_3PCC_CLIENT0_PORT
    rtp_client1_port = defs.RTP_3PCC_CLIENT1_PORT

    sip_twin_port = defs.SIP_3PCC_TWIN_PORT

    # ip
    sip_server0_ip = "192.168.0.16"
    sip_server1_ip = "192.168.0.16"

    rtp_server0_ip = "192.168.0.16"
    rtp_server1_ip = "192.168.0.16"

    sip_client0_ip = "192.168.0.11"
    sip_client1_ip = "192.168.0.14"

    rtp_client0_ip = "192.168.0.11"
    rtp_client1_ip = "192.168.0.14"

    # files
    sip_server0_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_SERVER0_FILE
    sip_server1_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_SERVER1_FILE

    sip_client0_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_CLIENT0_FILE
    sip_client1_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_CLIENT1_FILE

    # start uas 1 - 3pcc B side
    p = helps.sipp_3pcc_uas_start(
        sip_server1_file,
        sip_client1_ip, sip_client1_port,
        sip_server1_ip, sip_server1_port,
        rtp_server1_ip, rtp_server1_port,
        sip_server0_ip, sip_twin_port,
        sip_client1_user,
        str(msg_nr), str(rate_nr), str(ratep_nr))
    p.wait()

    # start uas 0 - 3pcc A side
    p = helps.sipp_3pcc_uas_start(
        sip_server0_file,
        sip_client0_ip, sip_client0_port,
        sip_server0_ip, sip_server0_port,
        rtp_server0_ip, rtp_server0_port,
        sip_server1_ip, sip_twin_port,
        sip_client0_user,
        str(msg_nr), str(rate_nr), str(ratep_nr))
    p.wait()


else:
    # users
    sip_server0_user = defs.SIP_3PCC_SERVER0_USER
    sip_client0_user = defs.SIP_3PCC_CLIENT0_USER

    # id
    sip_server0_id = defs.SIP_3PCC_SERVER0_ID
    sip_client0_id = defs.SIP_3PCC_CLIENT0_ID

    # if
    sip_server0_if = defs.SIP_3PCC_SERVER0_IF
    rtp_server0_if = defs.RTP_3PCC_SERVER0_IF

    sip_client0_if = defs.SIP_3PCC_CLIENT0_IF
    rtp_client0_if = defs.RTP_3PCC_CLIENT0_IF

    # port
    sip_server0_port = defs.SIP_3PCC_SERVER0_PORT
    rtp_server0_port = defs.RTP_3PCC_SERVER0_PORT

    sip_client0_port = defs.SIP_3PCC_CLIENT0_PORT
    rtp_client0_port = defs.RTP_3PCC_CLIENT0_PORT

    # ip
    sip_server0_ip = "192.168.0.16"
    rtp_server0_ip = "192.168.0.16"

    sip_client0_ip = "192.168.0.11"
    rtp_client0_ip = "192.168.0.11"

    #file
    sip_server0_file = test_name + "/" + defs.SIPP_BASE_DIR + defs.SIPP_SERVER0_FILE
    sip_client0_file = test_name + "/" + defs.SIPP_BASE_DIR + defs.SIPP_CLIENT0_FILE

    # start uas 0
    p = helps.sipp_uas_start(
        sip_server0_file,
        sip_client0_ip, sip_client0_port,
        sip_server0_ip, sip_server0_port,
        rtp_server0_ip, rtp_server0_port,
        sip_client0_user,
        str(msg_nr), str(rate_nr), str(ratep_nr))
    p.wait()


# wait for sipp scenario to stop
while helps.process_is_running("sipp"):
    1;
