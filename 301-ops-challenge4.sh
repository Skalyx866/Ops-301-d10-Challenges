#!/bin/bash

# Write a bash script that performs the following tasks:

# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip
# Hint: gzip is a preinstalled Linux application for performing zip formatted compression.

# Clear the contents of the log file
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log files

timestamp=$(date +%Y%m%d%I%M%S) #Declaring time stamp for logs as variable

#Making a function for the necessary operations
compression() 
{
    #Showing both the name and size of original files
    stat --format %n\ %s /var/log/syslog
    stat --format %n\ %s /var/log/wtmp

    #putting only the size in variables to compare later
    sys=$(stat --format %s /var/log/syslog)
    wtmp=$(stat --format %s /var/log/wtmp)
    
    #zipping files
    zip -v /var/log/backups/syslog-$timestamp /var/log/syslog
    zip -v /var/log/backups/wtmp-$timestamp /var/log/wtmp

    # printing out new file sizes
    stat --format %n\ %s /var/log/backups/syslog-*.zip
    stat --format %n\ %s /var/log/backups/wtmp-*.zip

    # storing new file sizes in variable to compare later
    syslogzip=$(stat --format %s /var/log/backups/syslog-*.zip)
    wtmpzip=$(stat --format %s /var/log/backups/wtmp-*.zip)

    # Printing out the comparison and cleaning original logs
    
    echo "Original syslog file is" $sys "bytes and compressed syslog file is" $syslogzip "bytes"
    echo "Original syslog file is" $wtmp "bytes and compressed syslog file is" $wtmpzip "bytes"
    echo "Compressed syslog file is" $(($sys-$syslogzip))  "smaller!"
    echo "Compressed wtmp file is" $(($wtmp-$wtmpzip)) "smaller!"
    echo "cleaning log files"
    rm -rf syslog wtmp
    echo "logs clean"

}
compression

