
# import socket
#
# server = socket.socket()
# server.bind(('localhost',9999))
# server.listen() #监听
#
# print("开始等电话")
# conn, addr = server.accept()  # 等待
# # conn就是客户端连过来而服务器端为其生成的链接实例
# print(conn, addr)
# print("电话来了")
#
# while True:
#     data = conn.recv(1024)
#     print('recv:', data.decode())
#     conn.send(data.upper())
#
# server.close()

# import socket
# server = socket.socket()
# server.bind(("localhost",9999))
# server.listen()
#
# conn,addr = server.accept()
# print(conn,addr)
# while True:
#     data = conn.recv(1024)
#     print("recv:",data.decode())
#     conn.send(data.upper())
# server.clsoe()

import socket
server = socket.socket()
server.bind(("localhost",9999))
server.listen()

conne,addr = server.accept()
print(conne,addr)
while True:
    data = conne.recv(1024)
    print("recv",data.decode())
    conne.send(data.upper())
server.clsoe()