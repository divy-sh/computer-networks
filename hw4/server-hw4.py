# Divyendu Shekhar
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import mimetypes

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve HTML or JSON content based on the requested resource
        content_type, _ = mimetypes.guess_type(self.path)
        if content_type == "text/html":
            try:
                # Open and serve the requested HTML file
                with open(self.path, 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', content_type)
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                # Handle file not found error
                self.send_error(404, f"File Not Found: {self.path}")
        elif content_type == "application/json":
            try:
                # Open and serve the requested JSON file
                with open(self.path, 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', content_type)
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                # Handle file not found error
                self.send_error(404, f"File Not Found: {self.path}")
        else:
            # Handle unsupported content type
            self.send_response(404)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(b'404 Not Found - Unsupported Content Type')

# Server setup
port = 8070
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving on port {port}")
httpd.serve_forever()