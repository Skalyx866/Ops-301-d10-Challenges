#/bin/bash
date=$(date +'%m%d%Y%H%M')
#grabbing the date and time

#reading the contents of syslog and writing it to backup with the date and time
cat /var/log/syslog > syslog-$date

