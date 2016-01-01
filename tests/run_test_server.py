import sys
import helps
import defs
import os
import time
import re


#################################### tests #####################################
test_list = ['refer-3pcc', 'reinvite-3pcc', 'reinvite-proactive-3pcc', 'reinvite-proactive-extension-3pcc', 'join-3pcc', 'reinvite-uac', 'reinvite-uas', 'options-uas', 'kamailio-geolocation-1']

################################### checks ####################################
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

################################### globals ####################################
# ip
sip_server0_ip = defs.SERVER_IP_0
sip_server1_ip = defs.SERVER_IP_1

rtp_server0_ip = defs.SERVER_IP_0
rtp_server1_ip = defs.SERVER_IP_1

sip_client0_ip = defs.CLIENT_IP_0
sip_client1_ip = defs.CLIENT_IP_1

rtp_client0_ip = defs.CLIENT_IP_0
rtp_client1_ip = defs.CLIENT_IP_1

kamailio_server_ip = defs.KAMAILIO_SERVER_IP

# port
sip_server0_port = defs.SERVER_PORT_00
rtp_server0_port = defs.SERVER_PORT_01

sip_server1_port = defs.SERVER_PORT_10
rtp_server1_port = defs.SERVER_PORT_11

sip_client0_port = defs.CLIENT_PORT_00
rtp_client0_port = defs.CLIENT_PORT_01

sip_client1_port = defs.CLIENT_PORT_10
rtp_client1_port = defs.CLIENT_PORT_11

sip_twin_port = defs.TWIN_PORT

kamailio_server_port = defs.KAMAILIO_SERVER_PORT

# users
sip_server0_user = defs.SERVER_USER_0
sip_server1_user = defs.SERVER_USER_1

sip_client0_user = defs.CLIENT_USER_0
sip_client1_user = defs.CLIENT_USER_1

# xml files
sip_server0_file = test_name + "/" + defs.SERVER_BASE_DIR + defs.SERVER_FILE_0
sip_server1_file = test_name + "/" + defs.SERVER_BASE_DIR + defs.SERVER_FILE_1

sip_client0_file = test_name + "/" + defs.CLIENT_BASE_DIR + defs.CLIENT_FILE_0
sip_client1_file = test_name + "/" + defs.CLIENT_BASE_DIR + defs.CLIENT_FILE_1

sip_server0_register_file = test_name + "/" + defs.SERVER_BASE_DIR + defs.SERVER_REGISTER_FILE_0
sip_server1_register_file = test_name + "/" + defs.SERVER_BASE_DIR + defs.SERVER_REGISTER_FILE_1

sip_client0_register_file = test_name + "/" + defs.CLIENT_BASE_DIR + defs.CLIENT_REGISTER_FILE_0
sip_client1_register_file = test_name + "/" + defs.CLIENT_BASE_DIR + defs.CLIENT_REGISTER_FILE_1

sip_server0_unregister_file = test_name + "/" + defs.SERVER_BASE_DIR + defs.SERVER_UNREGISTER_FILE_0
sip_server1_unregister_file = test_name + "/" + defs.SERVER_BASE_DIR + defs.SERVER_UNREGISTER_FILE_1

sip_client0_unregister_file = test_name + "/" + defs.CLIENT_BASE_DIR + defs.CLIENT_UNREGISTER_FILE_0
sip_client1_unregister_file = test_name + "/" + defs.CLIENT_BASE_DIR + defs.CLIENT_UNREGISTER_FILE_1

# other files
order= test_name + "/order"
result = test_name + "/time.out"

################################## cleanups ###################################
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

################################## test run ###################################
if re.search('3pcc', test_name):
	# start uas 1 - 3pcc B side
	p = helps.start_sipp_uas_3pcc (
		sip_server1_file,
		sip_client1_ip, sip_client1_port,
		sip_server1_ip, sip_server1_port,
		rtp_server1_ip, rtp_server1_port,
		sip_server0_ip, sip_twin_port,
		sip_client1_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

	# start uas 0 - 3pcc A side
	p = helps.start_sipp_uas_3pcc (
		sip_server0_file,
		sip_client0_ip, sip_client0_port,
		sip_server0_ip, sip_server0_port,
		rtp_server0_ip, rtp_server0_port,
		sip_server1_ip, sip_twin_port,
		sip_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()


elif re.search('kamailio', test_name):
	# start uas 0 register
	p = helps.start_sipp_uas (
		sip_server0_register_file,
                kamailio_server_ip, kamailio_server_port,
		sip_server0_ip, sip_server0_port,
		rtp_server0_ip, rtp_server0_port,
		sip_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

        p.wait()

	# wait for sipp scenario to stop
	while helps.is_process_running("sipp_uas"):
		1;

	# start uas 0
	p = helps.start_sipp_uas (
		sip_server0_file,
                kamailio_server_ip, kamailio_server_port,
		sip_server0_ip, sip_server0_port,
		rtp_server0_ip, rtp_server0_port,
		sip_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

        p.wait()

	# wait for sipp scenario to stop
	while helps.is_process_running("sipp_uas"):
		1;

	# start uas 0 unregister
	p = helps.start_sipp_uas (
		sip_server0_unregister_file,
                kamailio_server_ip, kamailio_server_port,
		sip_server0_ip, sip_server0_port,
		rtp_server0_ip, rtp_server0_port,
		sip_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

        p.wait()

	# wait for sipp scenario to stop
	while helps.is_process_running("sipp_uas"):
		1;


else:
	# start uas 0
	p = helps.start_sipp_uas (
		sip_server0_file,
		sip_client0_ip, sip_client0_port,
		sip_server0_ip, sip_server0_port,
		rtp_server0_ip, rtp_server0_port,
		sip_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()


# wait for sipp scenario to stop
while helps.is_process_running("sipp_uas"):
	1;
