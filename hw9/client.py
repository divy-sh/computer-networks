# Author: Divyendu Shekhar

from socket import *
import sys

if len(sys.argv) != 4:
    print("Entered invalid format, please use: python client.py <server_ip> <port> <html_file>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
FILENAME = sys.argv[3]

try:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request = f"GET /{FILENAME} HTTP/1.1\nHost: {HOST}\n\n"
        s.sendall(request.encode())
        response = s.recv(8192).decode()

        if "Connection Successful!" in response:
            print("Connection Successful!")
            print(response.split('Connection Successful!')[1])
        else:
            print("Error while connecting!")
except:
    print("Error while connecting!")