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
pcap_in=$1
pcap_out=$1-out
pcap_filter="(sip && sip.resend == false) || (rtp && (rtp.timestamp == 240))"

png_title=$2 
png_callflow_name=callflow.png 

#filter duplicate frames
editcap -v -D $frame_range $pcap_in $pcap_out 2&> /dev/null

callflow "$pcap_out" "--capture-filter" "$pcap_filter" "--title" "$png_title" "--no-time" "--no-archive" "--no-loops" "--remove-duplicate-frames" 2&> /dev/null

cp "${pcap_in%.*}/$png_callflow_name" "${pcap_in%.*}.png"

rm $pcap_out
rm -R "${pcap_in%.*}"
