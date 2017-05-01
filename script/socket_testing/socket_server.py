
import socket

server = socket.socket()
server.bind(('localhost',6969))
server.listen() #监听

print("开始等电话")
print(conn, addr)
print("dianhualaile")

while True:
    conn,addr = server.accept() #等待
    #conn就是客户端连过来而服务器端为其生成的链接实例


    data = conn.recv(1024)
    print('recv:', data)
    server.send(data.upper())

server.close()