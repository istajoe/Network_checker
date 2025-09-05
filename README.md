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
    │-- README.md 
    |-- requirements.txt           # Project documentation

Requirements

    Python 3.6+

    Works out of the box (uses built-in modules: os, platform, datetime)

Usage:

    Clone this repository:

    git clone https://github.com/your-username/network_checker.git
    cd network_checker


Run the script:

    python network_checker.py


Check logs inside network_log.txt: 

Customization

    you will have to add to youyr own hosts to check.