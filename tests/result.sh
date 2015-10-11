#/bin/bash
handover_time=time.out

test_dir=$1
test_title=$2

# enter folder
cd "$test_dir"

# average handover time
awk '{ sum += $1; n++ } END { if (n > 0) print "Test \033[92m'${test_dir}'\033[0m average handover time = \033[92m"sum / n "\033[0m MICROseconds\n\n\n\n"}' < "$handover_time"

# return from folder
cd ".."
