import socket
import base64

# Create socket
# s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
# host = socket.gethostname()
# host = "www.treelin.com"
host = socket.gethostname()
port = 12345

# Display received information
try:
    # Connect to server
    s.connect((host, port))
    while True:
        bytes1 = s.recv(10)
        if len(bytes1) == 0:
            break
        print(bytes1)
    s.close()
except ConnectionError as e:
    print("Exception: ", e)
