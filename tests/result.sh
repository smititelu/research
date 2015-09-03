#/bin/bash

# Premises:
# - inkscape
# - wireshark's editcap
# - callflow

whereis wireshark > /dev/null
if test $? -ne 0; then
	echo "Install wireshark!"
	exit 0
fi

whereis inkscape > /dev/null
if test $? -ne 0; then
	echo "Install inkscape!"
	exit 0
fi

whereis callflow > /dev/null
if test $? -ne 0; then
	echo "Install callflow!"
	exit 0
fi

if test $# -lt 2; then
	echo "Usage: ./png_from_pcap.sh pcap_in png_name_in"
	exit 0
fi

frame_range=99999

handover_time=time.out

test_dir=$1
test_title=$2

pcap_in=${test_dir}.pcap
pcap_out=${test_dir}.pcap-out
pcap_filter="(sip) || (rtp && (rtp.timestamp == 240))"

png_callflow_name=callflow.png
png_out=${test_dir}.png

# enter folder
cd "$test_dir"

# filter duplicate frames
#editcap -v -D $frame_range $pcap_in $pcap_out > /dev/null 2>&1
cp $pcap_in $pcap_out

# build png
callflow "$pcap_out" "--capture-filter" "$pcap_filter" "--title" "$test_title" "--no-time" "--no-archive" "--no-loops" "--remove-duplicate-frames"
cp "${pcap_in%.*}/$png_callflow_name" "$png_out"

# average handover time
awk '{ sum += $1; n++ } END { if (n > 0) print "\n\n\nAverage handover time = " sum / n " MICROseconds"; }' < "$handover_time"

# cleanup
rm -R "${pcap_in%.*}/"
mv $pcap_out $pcap_in

# return from folder
cd ".."
