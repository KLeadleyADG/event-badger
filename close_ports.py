import subprocess

# Ports to close
ports_to_close = [5000, 5001, 8081]

def get_process_id(port):
    """Get the process ID using the given port."""
    try:
        result = subprocess.run(
            ["netstat", "-ano"], capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            if f":{port}" in line:
                parts = line.split()
                pid = parts[-1]  # The PID is usually the last column
                return pid
    except subprocess.CalledProcessError:
        print(f"Failed to check port {port}")
    return None

def kill_process(pid):
    """Kill a process by its PID."""
    try:
        subprocess.run(["taskkill", "/F", "/PID", pid], check=True)
        print(f"Successfully terminated process {pid}")
    except subprocess.CalledProcessError:
        print(f"Failed to terminate process {pid}")

def close_ports(ports):
    """Close the given ports by terminating their processes."""
    for port in ports:
        pid = get_process_id(port)
        if pid:
            print(f"Port {port} is being used by PID {pid}, attempting to close...")
            kill_process(pid)
        else:
            print(f"No process found using port {port}")

if __name__ == "__main__":
    print("Closing any processes using ports:", ports_to_close)
    close_ports(ports_to_close)
    print("All specified ports have been closed.")
