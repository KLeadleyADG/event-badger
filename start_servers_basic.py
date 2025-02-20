import subprocess
import sys
import os
import time

print("Starting server script...")

# Ports to close before starting the servers
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

def is_running_in_vscode():
    """Detect if script is running inside VS Code's integrated terminal."""
    return "TERM_PROGRAM" in os.environ and os.environ["TERM_PROGRAM"] == "vscode"

def run_command_in_new_terminal(command, title=""):
    """Run a command in a new terminal window, working for VS Code and normal terminals."""
    try:
        print(f"Running in new terminal: {' '.join(command)}")

        if sys.platform == "win32":
            if is_running_in_vscode():
                # Run inside VS Code Terminal using PowerShell
                subprocess.Popen(
                    ["powershell", "-NoExit", "-Command", " ".join(command)],
                    creationflags=subprocess.CREATE_NEW_CONSOLE
                )
            else:
                # Run in a new cmd.exe window
                subprocess.Popen(
                    ["cmd.exe", "/k", f"title {title} & {' '.join(command)}"],
                    creationflags=subprocess.CREATE_NEW_CONSOLE
                )
        else:
            # Linux/macOS - Open in a new terminal window
            subprocess.Popen(
                ["gnome-terminal", "--", "bash", "-c", f"{' '.join(command)}; exec bash"]
            )
    except Exception as e:
        print(f"Error running command {command}: {e}")

if __name__ == "__main__":
    # Close ports before starting servers
    print("Closing any processes using ports:", ports_to_close)
    close_ports(ports_to_close)

    # Start each server in a new terminal window
    run_command_in_new_terminal(["npm", "run", "start:node"], title="Node.js Server")
    time.sleep(3)  # Give Node.js time to start

    run_command_in_new_terminal(["npm", "run", "start:python"], title="Python Server")
    time.sleep(3)  # Give Python server time to start

    run_command_in_new_terminal(["npx", "expo", "start", "-c"], title="Expo Server")

    print("All servers have been started in separate terminals.")
