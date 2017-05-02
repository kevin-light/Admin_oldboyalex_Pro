
import socket

client = socket.socket()
client.connect('localhost',6969)

while True:
    msg = input(">>").strip()

    client.sent(msg.encode("utf_8"))
    data = client.recv(1024)
    print("recv:", data.decode())

client.close