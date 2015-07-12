import sys
import helps_sipp

sys.path.append("/home/miti/git/research/tests/")
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

# start SIPp UAS in background
helps_sipp.sipp_uas_start(defs.SIPP_BASE_DIR + defs.UAS_FILE)

# start SIPP UAC in background
p = helps_sipp.sipp_uac_start(defs.SIPP_BASE_DIR + defs.UAC_INVITE_FILE, "127.0.0.1", str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

p = helps_sipp.sipp_uac_start(defs.SIPP_BASE_DIR + defs.UAC_REINVITE_FILE, "127.0.0.1", str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

p = helps_sipp.sipp_uac_start(defs.SIPP_BASE_DIR + defs.UAC_BYE_FILE, "127.0.0.1", str(msg_nr), str(rate_nr), str(ratep_nr))
p.wait()

#stop all sipp processes
helps_sipp.sipp_stop()
