import os
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(
    filename="start_servers.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s]: %(message)s"
)

# Prevent recursive execution
if getattr(sys, 'frozen', False):  # Check if running as an executable
    # Check if the current process matches the original executable name
    current_executable = os.path.basename(sys.executable)
    if "start_servers.exe" in current_executable:
        # Further refine: ensure this is not a subprocess spawned intentionally
        if len(sys.argv) > 1 and sys.argv[1] == "--no-recursion":
            logging.info("Legitimate subprocess execution. Continuing.")
        else:
            logging.error("Recursive execution detected. Exiting.")
            sys.exit(1)

# Handle PyInstaller's temporary directory
base_dir = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

# Paths
frontend_path = os.path.join(base_dir, "frontend")
node_server_path = os.path.join(base_dir, "backend", "node_server")
python_server_path = os.path.join(base_dir, "backend", "python_server")
node_modules_path = os.path.join(base_dir, "node_modules")

# Debug log for paths
logging.info(f"Base directory: {base_dir}")
logging.info(f"Frontend path: {frontend_path}")
logging.info(f"Node.js server path: {node_server_path}")
logging.info(f"Python server path: {python_server_path}")
logging.info(f"Node modules path: {node_modules_path}")

# Start React Native (Frontend)
try:
    logging.info("Starting React Native server...")
    react_native_command = os.path.join(node_modules_path, ".bin", "npx")
    subprocess.Popen(
        [react_native_command, "expo", "start", "-c", "--no-recursion"],
        cwd=frontend_path,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
except Exception as e:
    logging.error(f"Error starting React Native server: {e}")

# Start Node.js Server (Backend)
try:
    logging.info("Starting Node.js server...")

    # Ensure NODE_PATH includes the root node_modules
    env = os.environ.copy()
    env["NODE_PATH"] = node_modules_path

    # Resolve the path to server.js
    server_js_path = os.path.join(node_server_path, "server.js")

    # Log the resolved path for debugging
    logging.info(f"Resolved server.js path: {server_js_path}")

    if not os.path.exists(server_js_path):
        logging.error(f"server.js not found at {server_js_path}")
        raise FileNotFoundError(f"server.js not found at {server_js_path}")

    subprocess.Popen(
        ["node", server_js_path, "--no-recursion"],
        cwd=node_server_path, 
        stdout=sys.stdout,
        stderr=sys.stderr,
        env=env
    )
except Exception as e:
    logging.error(f"Error starting Node.js server: {e}")

# Start Python Flask Server (Backend)
try:
    logging.info("Starting Python Flask server...")

    # Add python_server_path to sys.path dynamically
    python_command = (
        f"import sys, os; sys.path.insert(0, '{python_server_path}'); "
        f"from app import app; app.run(host='0.0.0.0', port=5001, debug=True)"
    )

    subprocess.Popen(
        [sys.executable, "-c", python_command, "--no-recursion"],
        stdout=sys.stdout,
        stderr=sys.stderr
    )
except Exception as e:
    logging.error(f"Error starting Python Flask server: {e}")
