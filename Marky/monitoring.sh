#!/usr/bin/bash
#
# Some basic monitoring functionality; Tested on Amazon Linux 2.
#
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
MEMORYUSAGE=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
PROCESSES=$(expr $(ps -A | grep -c .) - 1)
HTTPD_PROCESSES=$(ps -A | grep -c httpd)
DISK_USAGE=$(df -h | awk '$6 == "/" {print $5}')
CPU_USAGE=$(top -bn 1 | awk 'NR==3{printf "%.2f%%", $9}')

echo "Instance ID: $INSTANCE_ID"
echo "Memory utilisation: $MEMORYUSAGE"
echo "No of processes: $PROCESSES"
if [ $HTTPD_PROCESSES -ge 1 ]
then
    echo "Web server is running"
else
    echo "Web server is NOT running"
fi

echo "Disk usage: $DISK_USAGE"
echo "CPU usage: $CPU_USAGE"