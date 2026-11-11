import socket
# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client.connect(('localhost', 8080))
# Create an HTTP GET request
http_request = (
    "GET / HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Connection: close\r\n"
    "\r\n"
)
# Send the HTTP request
client.sendall(http_request.encode())
# Receive the server response
response = b""
while True:
    chunk = client.recv(1024)
    if not chunk:
        break
    response += chunk
print("--- Received HTTP Response ---")
print(response.decode())
client.close()