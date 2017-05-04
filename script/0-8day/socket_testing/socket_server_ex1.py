import socket

server = socket.socket()
server.bind(("localhost",6969))
server.listen()

print("开始等电话")
conn,addr = server.accept()
print(conn,addr)

print("电话来了")
data = conn.recv(1024)
print("recv:",data)
conn.send(data.upper())
server.close()