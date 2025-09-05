Network Checker (Python Automation)

    A simple Python automation script that checks the status of multiple hosts (IP addresses or domains) by pinging them.
    The script prints results to the console and also logs them into a file (network_log.txt) with timestamps.

Features

    Cross-platform (works on Windows, Linux, and macOS)

    Checks if a host is online/offline

    Logs results with timestamps into network_log.txt

    Beginner-friendly and easy to extend

Project Structure
    network_checker/
    |--scripts
       |--network_checker.py   # Main Python script
    │-- network_log.txt      # Log file (auto-created)
    │-- README.md            # Project documentation

Requirements

    Python 3.6+

    Works out of the box (uses built-in modules: os, platform, datetime)

Usage:

    Clone this repository:

    git clone https://github.com/your-username/network_checker.git
    cd network_checker


Run the script:

    python network_checker.py


Example output:

    8.8.8.8 is ONLINE 
    1.1.1.1 is ONLINE 
    github.com is ONLINE 


Check logs inside network_log.txt:

Network Check - 2025-09-04 10:15:23

    8.8.8.8 is ONLINE
    1.1.1.1 is ONLINE 
    github.com is ONLINE 

Customization

    You can edit the list of hosts inside network_checker.py:

    hosts_to_check = ["8.8.8.8", "1.1.1.1", "github.com", "example.com"]
