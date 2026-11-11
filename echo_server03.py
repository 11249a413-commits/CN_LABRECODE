import socket
# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to localhost and port 5000
server.bind(('localhost', 5000))
# Listen for client connections
server.listen(1)
print("Echo Server is waiting for connection...")
# Accept client connection
conn, addr = server.accept()
print("Connected by:", addr)
while True:
    # Receive message from client
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode()
    print("Client:", message)
    # Send the same message back
    conn.sendall(data)
conn.close()
server.close()