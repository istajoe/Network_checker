import os       # to run system commands like 'ping'
import platform # to detect OS type
import datetime # to log time results


def ping_host(host):
    """
    Pings a host and returns True if reachable, False otherwise.
    """
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    # Build the ping command
    command = f"ping {param} {host}"

    # Run the ping command
    response = os.system(command)

    return response == 0  # 0 means success


def check_network(hosts):
    """
    Checks multiple hosts and logs results into a file.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("network_log.txt", "a") as log_file:
        log_file.write(f"\nNetwork check - {now}\n")
        log_file.write("=" * 40 + "\n")

        for host in hosts:
            if ping_host(host):
                result = f"{host} is ONLINE "
            else:
                result = f"{host} is OFFLINE "

            # Print result
            print(result)

            # Save result
            log_file.write(result + "\n")


# MAIN PROGRAM
if __name__ == "__main__":
    hosts_to_check = [h.strip() for h in input("Hosts to check (comma-separated): ").split(",") if h.strip()]

    if hosts_to_check:
        check_network(hosts_to_check)
    else:
        print("No hosts provided. Exiting.")
