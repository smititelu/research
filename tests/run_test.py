import sys
import helps
import defs
import os
import time

test_list = ['refer-3pcc', 'reinvite-3pcc']

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
else:
    test_name = "default_test"
    test_title = "default_title"
    msg_nr = defs.UAC_MSG_NR
    rate_nr = defs.UAC_MSG_RATE
    ratep_nr = defs.UAC_MSG_RATEP

if not any(test_name in item for item in test_list):
    print "Test " + test_name + " not found!"
    exit()

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
sip_server0_ip = helps.get_ip_addr(sip_server0_if)
sip_server1_ip = helps.get_ip_addr(sip_server1_if)

rtp_server0_ip = helps.get_ip_addr(rtp_server0_if)
rtp_server1_ip = helps.get_ip_addr(rtp_server1_if)

sip_client0_ip = helps.get_ip_addr(sip_client0_if)
sip_client1_ip = helps.get_ip_addr(sip_client1_if)

rtp_client0_ip = helps.get_ip_addr(rtp_client0_if)
rtp_client1_ip = helps.get_ip_addr(rtp_client1_if)

# files
sip_server0_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_SERVER0_FILE
sip_server1_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_SERVER1_FILE

sip_client0_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_CLIENT0_FILE
sip_client1_file = test_name + "/" + defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_CLIENT1_FILE

order= test_name + "/order"
result = test_name + "/time.out"

'''
print "SERVER0 USER: " + sip_server0_user + " " + sip_server0_file + " " + sip_server0_ip + ":" + sip_server0_port + " " + rtp_server0_ip + ":" + rtp_server0_port
print "SERVER1 USER: " + sip_server1_user + " " + sip_server1_file + " " + sip_server1_ip + ":" + sip_server1_port + " " + rtp_server1_ip + ":" + rtp_server1_port
print "CLIENT0 USER: " + sip_client0_user + " " + sip_client0_file + " " + sip_client0_ip + ":" + sip_client0_port + " " + rtp_client0_ip + ":" + rtp_client0_port
print "CLIENT1 USER: " + sip_client1_user + " " + sip_client1_file + " " + sip_client1_ip + ":" + sip_client1_port + " " + rtp_client1_ip + ":" + rtp_client1_port
print "TWIN port: " + sip_twin_port
'''
# cleanup
try:
    os.remove(order)
    os.remove(result)
except OSError:
    pass

# start tcpdump capture
helps.tcpdump_start(test_name + "/" + test_name + ".pcap")

# start uac 0
p = helps.sipp_3pcc_uac_start(
	sip_client0_file,
	sip_client0_ip, sip_client0_port,
	rtp_client0_ip, rtp_client0_port,
	sip_server0_ip, sip_server0_port,
	sip_server0_user,
	str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

# start uac 1
p = helps.sipp_3pcc_uac_start(
	sip_client1_file,
	sip_client1_ip, sip_client1_port,
	rtp_client1_ip, rtp_client1_port,
	sip_server1_ip, sip_server1_port,
	sip_server1_user,
	str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

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

while helps.process_is_running("sipp"):
       1;

# create order file used for ca
fd=open(order, "w+")
print >> fd, sip_client0_ip + ":.* UAC wlan0"
print >> fd, sip_server0_ip + ":.* UAS server0"
if sip_server0_ip != sip_server1_ip:
	print >> fd, sip_server1_ip + ":.* UAS server1"
print >> fd, sip_client1_ip + ":.* UAC wlan1"
fd.close()

# stop tcpdump
helps.tcpdump_stop()

# start final processing script
p = helps.result_start(test_name, test_title)
p.wait()

