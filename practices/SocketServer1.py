import socket

# Create socket
s = socket.socket()

# Bind port
host = socket.gethostname()
port = 12345
s.bind((host, port))

print("Create socket and bind to {0}:{1}".format(host, port))

# listening
s.listen(5)

# Wait client connecting
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    c.send(bytes('Thank you for connecting', "utf-8"))
    c.close()                # Close the connection
