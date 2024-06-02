import subprocess
import time

import os

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current Working Directory:", current_directory)

def run_server():
    return subprocess.Popen(['./server.py'])

def run_client(param):
    return subprocess.Popen(['./client.py', str(param)])

def main():
    for param in range(-1000, 1001):
        print(f"Running server and client with param: {param}")
        
        # Start the server
        server_process = run_server()
        
        # Give the server a little time to start
        time.sleep(1)
        
        # Start the client with the current parameter
        client_process = run_client(param)
        
        # Wait for the client to finish
        client_process.wait()
        
        # Terminate the server
        server_process.terminate()
        
        # Wait for the server to clean up properly
        server_process.wait()
        
        print(f"Completed iteration with param: {param}")

if __name__ == "__main__":
    main()
