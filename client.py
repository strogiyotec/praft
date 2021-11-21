import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ('localhost',10000)
socket.connect(server_address)
try:
    message = input("Type your message:\n ")
    print(f"Sending message '{message}' to the server")
    socket.sendall(message.encode("utf-8"))
    response = socket.recv(32)
    print(f"Received data {response}")
finally:
    socket.close()
    

