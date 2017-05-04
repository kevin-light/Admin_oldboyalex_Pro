import  socket

client = socket.socket()
client.connect(("localhost",6969))
client.send(b"hello")
data = client.recv(1024)
print("recv:",data)

client.close()