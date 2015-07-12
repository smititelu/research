import sys

import helps_sipsak

sys.path.append("/home/miti/git/research/tests/")
import defs

# check if given number of calls is given as argument
if len(sys.argv) > 1:
    try:
        calls = int(sys.argv[1])
    except Exception:
        print("Usage: sudo python run_test.py [nr_calls]")
        exit()
else:
    calls = defs.SIPSAK_BASE_CALLS

# start SIPp UAS in background
helps_sipsak.sipp_uas_start(defs.SIPP_BASE_DIR + defs.UAS_FILE)
#subprocess.call("sipp -bg -sf " + BASE_DIR_SIPP + UAS_FILE, shell=True)

# prepare files to be used by sipsak for sending SIP msg
helps_sipsak.msg_files_pre(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_INVITE_FILE)
helps_sipsak.msg_files_pre(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_REINVITE_FILE)
helps_sipsak.msg_files_pre(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_BYE_FILE)

# send SIP msg using sipsak and the files prepared above
helps_sipsak.msg_files_send(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_INVITE_FILE, defs.SIPSAK_BASE_NUMBER, defs.SIPSAK_BASE_PORT)
helps_sipsak.msg_files_send(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_REINVITE_FILE, defs.SIPSAK_BASE_NUMBER, defs.SIPSAK_BASE_PORT)
helps_sipsak.msg_files_send(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_BYE_FILE, defs.SIPSAK_BASE_NUMBER, defs.SIPSAK_BASE_PORT)

# delete files used by sipsak for sending SIP msg
helps_sipsak.msg_files_pos(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_INVITE_FILE)
helps_sipsak.msg_files_pos(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_REINVITE_FILE)
helps_sipsak.msg_files_pos(calls, defs.SIPSAK_BASE_DIR, defs.SIPSAK_BYE_FILE)

#stop all sipp processes
helps_sipsak.sipp_stop()
