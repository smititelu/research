import sys
import helps

sys.path.append("../")
import defs

# check if given number of calls is given as argument
if len(sys.argv) > 3:
    try:
        msg_nr = int(sys.argv[1])
        rate_nr = int(sys.argv[2])
        ratep_nr = int(sys.argv[3])
    except Exception:
        print("Usage: sudo python run_test.py [msg_nr] [rate_nr] [ratep_nr]")
        exit()
else:
    msg_nr = defs.UAC_MSG_NR
    rate_nr = defs.UAC_MSG_RATE
    ratep_nr = defs.UAC_MSG_RATEP

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
sip_server0_file = defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_SERVER0_FILE
sip_server1_file = defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_SERVER1_FILE

sip_client0_file = defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_CLIENT0_FILE
sip_client1_file = defs.SIPP_3PCC_BASE_DIR + defs.SIPP_3PCC_CLIENT1_FILE

'''
print "SERVER0 USER: " + sip_server0_user + " " + sip_server0_file + " " + sip_server0_ip + ":" + sip_server0_port + " " + rtp_server0_ip + ":" + rtp_server0_port
print "SERVER1 USER: " + sip_server1_user + " " + sip_server1_file + " " + sip_server1_ip + ":" + sip_server1_port + " " + rtp_server1_ip + ":" + rtp_server1_port
print "CLIENT0 USER: " + sip_client0_user + " " + sip_client0_file + " " + sip_client0_ip + ":" + sip_client0_port + " " + rtp_client0_ip + ":" + rtp_client0_port
print "CLIENT1 USER: " + sip_client1_user + " " + sip_client1_file + " " + sip_client1_ip + ":" + sip_client1_port + " " + rtp_client1_ip + ":" + rtp_client1_port
print "TWIN port: " + sip_twin_port
'''

# start uac 0
helps.sipp_3pcc_uac_start(
	sip_client0_file,
	sip_client0_ip, sip_client0_port,
	rtp_client0_ip, rtp_client0_port,
	sip_server0_ip, sip_server0_port,
	sip_server0_user,
	str(msg_nr), str(rate_nr), str(ratep_nr))

# start uac 1
helps.sipp_3pcc_uac_start(
	sip_client1_file,
	sip_client1_ip, sip_client1_port,
	rtp_client1_ip, rtp_client1_port,
	sip_server1_ip, sip_server1_port,
	sip_server1_user,
	str(msg_nr), str(rate_nr), str(ratep_nr))

# start uas 1 - 3pcc B side
helps.sipp_3pcc_uas_start(
	sip_server1_file,
	sip_client1_ip, sip_client1_port,
	sip_server1_ip, sip_server1_port,
	rtp_server1_ip, rtp_server1_port,
	sip_server0_ip, sip_twin_port,
	sip_client1_user,
	str(msg_nr), str(rate_nr), str(ratep_nr))

# start uas 0 - 3pcc A side
helps.sipp_3pcc_uas_start(
	sip_server0_file,
	sip_client0_ip, sip_client0_port,
	sip_server0_ip, sip_server0_port,
	rtp_server0_ip, rtp_server0_port,
	sip_server1_ip, sip_twin_port,
	sip_client0_user,
	str(msg_nr), str(rate_nr), str(ratep_nr))
