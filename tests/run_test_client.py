import sys
import helps
import defs
import os
import time
import re


#################################### tests #####################################
test_list = ['refer-3pcc', 'reinvite-3pcc', 'reinvite-proactive-3pcc', 'reinvite-proactive-extension-3pcc', 'join-3pcc', 'reinvite-uac', 'reinvite-uas', 'options-uas', 'kamailio-geolocation-1', 'kamailio-geolocation-2']

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
sip_uas_server0_ip = defs.UAS_SERVER_IP_0
sip_uas_server1_ip = defs.UAS_SERVER_IP_1

rtp_uas_server0_ip = defs.UAS_SERVER_IP_0
rtp_uas_server1_ip = defs.UAS_SERVER_IP_1

sip_uac_client0_ip = defs.UAC_CLIENT_IP_0
sip_uac_client1_ip = defs.UAC_CLIENT_IP_1

rtp_uac_client0_ip = defs.UAC_CLIENT_IP_0
rtp_uac_client1_ip = defs.UAC_CLIENT_IP_1

sip_kamailio_server_ip = defs.KAMAILIO_SERVER_IP

# port
sip_uas_server0_port = defs.UAS_SERVER_PORT_00
rtp_uas_server0_port = defs.UAS_SERVER_PORT_01

sip_uas_server1_port = defs.UAS_SERVER_PORT_10
rtp_uas_server1_port = defs.UAS_SERVER_PORT_11

sip_uac_client0_port = defs.UAC_CLIENT_PORT_00
rtp_uac_client0_port = defs.UAC_CLIENT_PORT_01

sip_uac_client1_port = defs.UAC_CLIENT_PORT_10
rtp_uac_client1_port = defs.UAC_CLIENT_PORT_11

sip_twin_port = defs.TWIN_PORT

sip_kamailio_server_port = defs.KAMAILIO_SERVER_PORT

# users
sip_uas_server0_user = defs.UAS_SERVER_USER_0
sip_uas_server1_user = defs.UAS_SERVER_USER_1

sip_uac_client0_user = defs.UAC_CLIENT_USER_0
sip_uac_client1_user = defs.UAC_CLIENT_USER_1

# xml files
sipp_uas_server0_file = test_name + "/" + defs.UAS_SERVER_BASE_DIR + defs.UAS_SERVER_FILE_0
sipp_uas_server1_file = test_name + "/" + defs.UAS_SERVER_BASE_DIR + defs.UAS_SERVER_FILE_1

sipp_uac_client0_file = test_name + "/" + defs.UAC_CLIENT_BASE_DIR + defs.UAC_CLIENT_FILE_0
sipp_uac_client1_file = test_name + "/" + defs.UAC_CLIENT_BASE_DIR + defs.UAC_CLIENT_FILE_1

sipp_uas_server0_register_file = test_name + "/" + defs.UAS_SERVER_BASE_DIR + defs.UAS_SERVER_REGISTER_FILE_0
sipp_uas_server1_register_file = test_name + "/" + defs.UAS_SERVER_BASE_DIR + defs.UAS_SERVER_REGISTER_FILE_1

sipp_uac_client0_register_file = test_name + "/" + defs.UAC_CLIENT_BASE_DIR + defs.UAC_CLIENT_REGISTER_FILE_0
sipp_uac_client1_register_file = test_name + "/" + defs.UAC_CLIENT_BASE_DIR + defs.UAC_CLIENT_REGISTER_FILE_1

sipp_uas_server0_unregister_file = test_name + "/" + defs.UAS_SERVER_BASE_DIR + defs.UAS_SERVER_UNREGISTER_FILE_0
sipp_uas_server1_unregister_file = test_name + "/" + defs.UAS_SERVER_BASE_DIR + defs.UAS_SERVER_UNREGISTER_FILE_1

sipp_uac_client0_unregister_file = test_name + "/" + defs.UAC_CLIENT_BASE_DIR + defs.UAC_CLIENT_UNREGISTER_FILE_0
sipp_uac_client1_unregister_file = test_name + "/" + defs.UAC_CLIENT_BASE_DIR + defs.UAC_CLIENT_UNREGISTER_FILE_1

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
print "SERVER0 USER: " + sip_uas_server0_user + " " + sipp_uas_server0_file + " " + sip_uas_server0_ip + ":" + sip_uas_server0_port + " " + rtp_uas_server0_ip + ":" + rtp_uas_server0_port
print "SERVER1 USER: " + sip_uas_server1_user + " " + sipp_uas_server1_file + " " + sip_uas_server1_ip + ":" + sip_uas_server1_port + " " + rtp_uas_server1_ip + ":" + rtp_uas_server1_port
print "CLIENT0 USER: " + sip_uac_client0_user + " " + sipp_uac_client0_file + " " + sip_uac_client0_ip + ":" + sip_uac_client0_port + " " + rtp_uac_client0_ip + ":" + rtp_uac_client0_port
print "CLIENT1 USER: " + sip_uac_client1_user + " " + sipp_uac_client1_file + " " + sip_uac_client1_ip + ":" + sip_uac_client1_port + " " + rtp_uac_client1_ip + ":" + rtp_uac_client1_port
print "TWIN port: " + sip_twin_port
'''

################################## test run ###################################
if re.search('3pcc', test_name):
	sip_kamailio_server_ip = ""

	# start tcpdump capture
	helps.start_tcpdump(test_name + "/" + test_name + ".pcap")

	# start uac 1
	p = helps.start_sipp_uac_3pcc (
		sipp_uac_client1_file,
		sip_uac_client1_ip, sip_uac_client1_port,
		rtp_uac_client1_ip, rtp_uac_client1_port,
		sip_uas_server1_ip, sip_uas_server1_port,
		sip_uas_server1_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

	# start uac 0
	p = helps.start_sipp_uac_3pcc (
		sipp_uac_client0_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_uas_server0_ip, sip_uas_server0_port,
		sip_uas_server0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

        # wait for sipp scenario to stop
        while helps.is_process_running("sipp_uac"):
                1;

	# stop tcpdump
	helps.stop_tcpdump()


elif re.search('kamailio-geolocation-1', test_name):
	############################## REGISTER ###############################
	# start uac 0 register
	p = helps.start_sipp_uac (
		sipp_uac_client0_register_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uac_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

        # wait for sipp scenario to stop
        while helps.is_process_running("sipp_uac"):
                1;

	################################ TEST #################################
	# start tcpdump capture
	helps.start_tcpdump(test_name + "/" + test_name + ".pcap")

	# start uac 0
	p = helps.start_sipp_uac (
		sipp_uac_client0_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uas_server0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

        # wait for sipp scenario to stop
        while helps.is_process_running("sipp_uac"):
                1;

	# stop tcpdump
	helps.stop_tcpdump()

	############################# unREGISTER ##############################
	# start uac 0 unregister
	p = helps.start_sipp_uac (
		sipp_uac_client0_unregister_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uac_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

        # wait for sipp scenario to stop
        while helps.is_process_running("sipp_uac"):
                1;


elif re.search('kamailio-geolocation-2', test_name):
	############################## REGISTER ###############################
	# start uac 0 register wlan0
	p = helps.start_sipp_uac (
		sipp_uac_client0_register_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uac_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

	# start uac 0 register wlan1
	p = helps.start_sipp_uac (
		sipp_uac_client0_register_file,
		sip_uac_client1_ip, sip_uac_client1_port,
		rtp_uac_client1_ip, rtp_uac_client1_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uac_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

        # wait for sipp scenario to stop
        while helps.is_process_running("sipp_uac"):
                1;

	############################# TEST ##############################
	# start tcpdump capture
	helps.start_tcpdump(test_name + "/" + test_name + ".pcap")

	# start uac 0
	p = helps.start_sipp_uac (
		sipp_uac_client0_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uas_server0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

	# start uac 1
	p = helps.start_sipp_uac (
		sipp_uac_client1_file,
		sip_uac_client1_ip, sip_uac_client1_port,
		rtp_uac_client1_ip, rtp_uac_client1_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uas_server0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

        # wait for sipp scenario to stop
        while helps.is_process_running("sipp_uac"):
                1;

	# stop tcpdump
	helps.stop_tcpdump()

	############################# unREGISTER ##############################
	# start uac0 unregister wlan0
	p = helps.start_sipp_uac (
		sipp_uac_client0_unregister_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uac_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

	# start uac0 unregister wlan1
	p = helps.start_sipp_uac (
		sipp_uac_client0_unregister_file,
		sip_uac_client1_ip, sip_uac_client1_port,
		rtp_uac_client1_ip, rtp_uac_client1_port,
		sip_kamailio_server_ip, sip_kamailio_server_port,
		sip_uac_client0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

	# wait for sipp scenario to stop
	while helps.is_process_running("sipp_uac"):
		1;


else:
	sip_uac_client1_ip = ""
	sip_kamailio_server_ip = ""

	# start tcpdump capture
	helps.start_tcpdump(test_name + "/" + test_name + ".pcap")

	# start uac 0
	p = helps.start_sipp_uac (
		sipp_uac_client0_file,
		sip_uac_client0_ip, sip_uac_client0_port,
		rtp_uac_client0_ip, rtp_uac_client0_port,
		sip_uas_server0_ip, sip_uas_server0_port,
		sip_uas_server0_user,
		str(msg_nr), str(rate_nr), str(ratep_nr)
	)

	p.wait()

	# wait for sipp scenario to stop
	while helps.is_process_running("sipp_uac"):
		1;

	# stop tcpdump
	helps.stop_tcpdump()


# start processing callflow flow only for one sip msg
if msg_nr == 1:
	# create order file used for ca
	fd=open(order, "w+")

	if sip_uac_client1_ip != "":
		print >> fd, sip_uac_client1_ip + ":.* UAC 1"
	print >> fd, sip_uac_client0_ip + ":.* UAC 0"

	if sip_kamailio_server_ip != "":
		print >> fd, sip_kamailio_server_ip + ":.* Kamailio"

	print >> fd, sip_uas_server0_ip + ":.* UAS"
	if sip_uas_server0_ip != sip_uas_server1_ip and sip_uas_server1_ip != "":
		print >> fd, sip_uas_server1_ip + ":.* UAS"

	fd.close()

	p = helps.start_callflow(test_name, test_title)
	p.wait()

# start processing results
p = helps.start_callresult(test_name, test_title)
p.wait()
