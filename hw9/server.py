# Author: Divyendu Shekhar

from socket import *
import sys

if len(sys.argv) != 2:
    print("Entered invalid format, please use: python server.py <port>")
    sys.exit(1)

HOST = gethostbyname(gethostname())
PORT = int(sys.argv[1])

print(f"server IP address: {HOST}")
print(f"server port number: {PORT}")

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Ready to serve...")

    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode()
            headers = request.split()
            if len(headers) > 1 and headers[0] == 'GET':
                filename = headers[1].lstrip('/')
                try:
                    with open(filename, 'r') as f:
                        content = f.read()
                    response = ("Connection Successful!\n\n"
                                "---------------HTTP RESPONSE---------------\n\n"
                                "HTTP/1.1 200 OK\n\n"
                                f"{content}\n\n"
                                "---------------END OF HTTP RESPONSE---------------\n\n")
                except FileNotFoundError:
                    response = ("Connection Successful!\n\n"
                                "---------------HTTP RESPONSE---------------\n\n"
                                "HTTP/1.1 404 Not Found\n\n"
                                "---------------END OF HTTP RESPONSE---------------\n\n")
                conn.sendall(response.encode())
