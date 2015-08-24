import sys
import helps_sipp

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

# vars
sip_server_if = defs.SIP_SERVER_IF
sip_client0_if = defs.SIP_CLIENT0_IF
sip_client1_if = defs.SIP_CLIENT1_IF

sip_server_ip = helps_sipp.get_ip_addr(sip_server_if)
sip_client0_ip = helps_sipp.get_ip_addr(sip_client0_if)
sip_client1_ip = helps_sipp.get_ip_addr(sip_client1_if)
sip_server_uac_ip = "192.168.0.102";
sip_server_uas_ip = "192.168.0.102";

# files
sip_server_file = defs.SIPP_BASE_DIR + defs.UAS_FILE

sip_client0_invite_file = defs.SIPP_BASE_DIR + defs.SIP_CLIENT0_ID + "-" + defs.UAC_INVITE_FILE
sip_client0_reinvite_file = defs.SIPP_BASE_DIR + defs.SIP_CLIENT0_ID + "-" + defs.UAC_INVITE_FILE
sip_client0_bye_file = defs.SIPP_BASE_DIR + defs.SIP_CLIENT0_ID + "-" + defs.UAC_BYE_FILE
sip_client0_refer_file = defs.SIPP_BASE_DIR + defs.SIP_CLIENT0_ID + "-" + defs.UAC_REFER_FILE

sip_client1_invite_file = defs.SIPP_BASE_DIR + defs.SIP_CLIENT1_ID + "-" + defs.UAC_INVITE_FILE
sip_client1_reinvite_file = defs.SIPP_BASE_DIR + defs.SIP_CLIENT1_ID + "-" + defs.UAC_INVITE_FILE
sip_client1_bye_file = defs.SIPP_BASE_DIR + defs.SIP_CLIENT1_ID + "-" + defs.UAC_BYE_FILE

print sip_server_file + " " + sip_client0_invite_file + " " + sip_client1_invite_file + " " + sip_client0_reinvite_file + " " + sip_client1_reinvite_file + " " + sip_client0_bye_file + " " + sip_client1_bye_file

# start SIPp UAS in background
#helps_sipp.sipp_uas_start(defs.SIPP_BASE_DIR + defs.UAS_FILE, helps_sipp.get_ip_addr(defs.SIP_SERVER))

# start SIPP UAC in background

# client 0 invite
p = helps_sipp.sipp_uac_start(
	sip_client0_invite_file,
	sip_client0_ip,
	sip_server_ip,
	str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

# client 0 refer
p = helps_sipp.sipp_uac_start(
	sip_client0_refer_file,
	sip_client0_ip,
	sip_server_ip,
	str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

# client 0 bye
p = helps_sipp.sipp_uac_start(
	sip_client0_bye_file,
	sip_client0_ip,
	sip_server_ip,
	str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

#stop all sipp processes
helps_sipp.sipp_stop()
