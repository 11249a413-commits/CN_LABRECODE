import socket
# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client.connect(('localhost', 5000))
while True:
    # Enter a message
    message = input("Enter message (exit to stop): ")
    if message.lower() == "exit":
        break
    # Send message to server
    client.sendall(message.encode())
    # Receive echoed message
    data = client.recv(1024)
    print("Echo from server:", data.decode())
client.close()