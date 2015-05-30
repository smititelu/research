import subprocess

ITER = 10

BASE_PORT = 9999
BASE_USER = "user"

SIP_PROTO= "sip"
SIPS_PROTO= "sips"

DIR_SIPSAK = "msg/"
DIR_SIPP = "xml/"

INVITE_FILE = "invite.msg"
BYE_FILE = "bye.msg"

BASE_INVITE_FILE = "invite.msg"
BASE_BYE_FILE = "bye.msg"

subprocess.call(["ls", "-l"])

def msg_format(index, fin, fout):
    subprocess.call("cat " +  DIR_SIPSAK + INVITE_FILE +                " | " +
                    "sed s/call_id/call_id" + str(index) + "/" +        " | " +
                    "sed s/service/" + BASE_USER + str(index) + "/" +   " > " +
                    fout, shell=True)

for i in range(1, ITER):
    proto   = SIP_PROTO
    port    = BASE_PORT + i
    user    = BASE_USER + str(i)
    fin     = DIR_SIPSAK + INVITE_FILE
    fout    = DIR_SIPSAK + INVITE_FILE + str(i)

    msg_format(i, fin, fout)
    subprocess.call(["sipsak",
                     "-vv",
                     "-l", str(port),
                     "-s", proto + ":" + user + "@" + "127.0.1.1",
                     "-f", fout])
