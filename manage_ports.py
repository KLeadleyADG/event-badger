import os
import subprocess
import platform

def check_port(port):
    """
    Check if a specific port is open and return its details.
    """
    system = platform.system()
    try:
        if system == "Windows":
            # Use netstat to find the port
            result = subprocess.check_output(f"netstat -ano | findstr :{port}", shell=True, text=True)
            for line in result.splitlines():
                if "LISTENING" in line:
                    parts = line.split()
                    protocol = parts[0]
                    local_address = parts[1]
                    pid = parts[-1]
                    return {"port": port, "protocol": protocol, "address": local_address, "pid": pid}
        else:
            # Use lsof to find the port on Unix-based systems
            result = subprocess.check_output(f"lsof -i :{port}", shell=True, text=True)
            for line in result.splitlines():
                if "LISTEN" in line:
                    parts = line.split()
                    protocol = parts[-1]
                    local_address = parts[8]
                    pid = parts[1]
                    return {"port": port, "protocol": protocol, "address": local_address, "pid": pid}
    except subprocess.CalledProcessError:
        return None

def close_port(pid, port):
    """
    Close the process associated with a port.
    """
    try:
        system = platform.system()
        if system == "Windows":
            subprocess.check_call(f"taskkill /PID {pid} /F", shell=True)
        else:
            os.kill(int(pid), 9)
        print(f"Successfully closed port {port} (PID: {pid}).")
    except Exception as e:
        print(f"Failed to close port {port} (PID: {pid}): {e}")

if __name__ == "__main__":
    ports_to_check = [5000, 5001, 8081]
    for port in ports_to_check:
        port_info = check_port(port)
        if port_info:
            print(f"Port {port} is in use:")
            print(f"  Protocol: {port_info['protocol']}")
            print(f"  Address: {port_info['address']}")
            print(f"  PID: {port_info['pid']}")
            choice = input(f"Do you want to close port {port} (PID: {port_info['pid']})? (y/n): ").strip().lower()
            if choice == "y":
                close_port(port_info['pid'], port)
            else:
                print(f"Port {port} (PID: {port_info['pid']}) will remain open.")
        else:
            print(f"Port {port} is not in use.")

