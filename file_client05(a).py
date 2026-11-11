import socket
import os
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5006))
filename = input("Enter the file name to send: ")
if not os.path.isfile(filename):
    print("File not found!")
    client.close()
    exit()
client.sendall(filename.encode())
client.recv(1024)  # Wait for server acknowledgement
with open(filename, "rb") as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client.sendall(data)
client.shutdown(socket.SHUT_WR)
print("File sent successfully!")
client.close()