import sys

sys.path.append("/home/miti/git/research/tests/")

import helps
import defs

# check if given number of calls is given as argument
if len(sys.argv) > 1:
    try:
        calls = int(sys.argv[1])
    except Exception:
        print("Usage: sudo python run_test.py [nr_calls]")
        exit()
else:
    calls = defs.BASE_CALLS

# start SIPp UAS in background
#subprocess.call("sipp -bg -sf " + BASE_DIR_SIPP + UAS_FILE, shell=True)

# prepare files to be used by sipsak for sending SIP msg
helps.msg_files_pre(calls, defs.BASE_DIR_SIPSAK, defs.BASE_INVITE_FILE)
helps.msg_files_pre(calls, defs.BASE_DIR_SIPSAK, defs.BASE_REINVITE_FILE)
helps.msg_files_pre(calls, defs.BASE_DIR_SIPSAK, defs.BASE_BYE_FILE)

# send SIP msg using sipsak and the files prepared above
helps.msg_files_send(calls, defs.BASE_DIR_SIPSAK, defs.BASE_INVITE_FILE, defs.BASE_NUMBER, defs.BASE_PORT)
helps.msg_files_send(calls, defs.BASE_DIR_SIPSAK, defs.BASE_REINVITE_FILE, defs.BASE_NUMBER, defs.BASE_PORT)
helps.msg_files_send(calls, defs.BASE_DIR_SIPSAK, defs.BASE_BYE_FILE, defs.BASE_NUMBER, defs.BASE_PORT)

# delete files used by sipsak for sending SIP msg
helps.msg_files_pos(calls, defs.BASE_DIR_SIPSAK, defs.BASE_INVITE_FILE)
helps.msg_files_pos(calls, defs.BASE_DIR_SIPSAK, defs.BASE_REINVITE_FILE)
helps.msg_files_pos(calls, defs.BASE_DIR_SIPSAK, defs.BASE_BYE_FILE)
