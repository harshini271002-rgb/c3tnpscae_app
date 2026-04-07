import subprocess
import sys
import threading
import time
import os
import webbrowser
import socket

def get_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

PORT = get_free_port()

def start_server():
    # Force headless so it doesn't open a standard browser tab
    cmd = [
        sys.executable, "-m", "streamlit", "run", "app.py",
        "--server.port", str(PORT),
        "--server.headless", "true",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ]
    # Hide the backend console window for the subprocess
    startupinfo = None
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    
    subprocess.Popen(cmd, startupinfo=startupinfo)

if __name__ == '__main__':
    print("====================================")
    print(" Starting C3 AE Quiz Desktop Engine")
    print("====================================")
    print("Spinning up local server...")
    
    # Start the Streamlit server in a background thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Wait for the server to spin up
    print("Waiting for readiness...")
    time.sleep(3)

    print("Opening Native App UI...")
    url = f"http://localhost:{PORT}"
    
    # Try to open in Chrome/Edge "App Mode" (No URL bar, no tabs, looks like a real desktop app)
    browser_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    ]
    
    opened = False
    for b_path in browser_paths:
        if os.path.exists(b_path):
            try:
                # The --app flag is the key feature here to make it look native
                subprocess.Popen([b_path, f"--app={url}"])
                opened = True
                break
            except Exception:
                pass
                
    if not opened:
        # Fallback to standard browser if Chrome or Edge aren't natively installed
        webbrowser.open(url)
        
    print("App is running. Close this window to stop the background server.")
    
    # Keep the script alive so the child thread lives
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
