# Divyendu Shekhar
import http.client
import sys

def get_resource(resource):
    conn = http.client.HTTPConnection("localhost", 8070)
    conn.request("GET", f"/{resource}")
    response = conn.getresponse()
    status_code = response.status
    content_type = response.headers.get("Content-type")
    content = response.read().decode()

    print(f"Response Status Code: {status_code}")
    print(f"Content Type: {content_type}")
    print("Response Content:")
    print(content)

    conn.close()

get_resource(sys.argv[1])