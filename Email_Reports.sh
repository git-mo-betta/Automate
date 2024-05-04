

Email_Reports.py 

My Backup server script for emailed reports to Network Operations

!/bin/bash

# Get yesterday's date in YYYY-MM-DD format
date="$(date -d "yesterday" '+%Y-%m-%d')"
# Use bconsole to get the job logs
if echo "list jobs" | bconsole > /usr/noc/job_logs.txt; then
    # Parse the job logs to find failed jobs from yesterday
    lines=$(grep -E "$date.*f" /usr/noc/job_logs.txt | tee /usr/noc/failed_logs.txt | wc -l) 
        # Check if there were any failed jobs
    if [ -s /usr/noc/failed_logs.txt ]; then
        # If the file is not empty, send an email with the failed jobs
        (echo "TEST EMAIL $date"; cat /usr/noc/failed_logs.txt) | /usr/local/bacula7/sbin/bsmtp -h localhost -f "bacula@localhost" -s "Failed Bacula Jobs from $date" NOC@example.com
    else
        echo "TEST EMAIL $date" | /usr/local/bacula7/sbin/bsmtp -h localhost -f "bacula@localhost" -s "Failed Bacula Jobs from $date" NOC@example.com
    fi
else
    echo "Failed to get job logs"
fi
