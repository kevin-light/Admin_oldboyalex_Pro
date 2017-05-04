#
# import socket
#
# server = socket.socket()
# server.bind(('localhost',6969))
# server.listen() #监听
#
# print("开始等client。。。")
#
# conn,addr = server.accept()
#
# print("x新链接",addr)
#
# while True:
#     #conn,addr = server.accept() #等待
#     #conn就是客户端连过来而服务器端为其生成的链接实例
#     data = conn.recv(1024)
#     if not data:
#         print("客户端断开了。。。")
#         break
#     print('shoudao recv:', data)
#     conn.send(data.upper())
# server.close()

import socket
server = socket.socket() #获得socket实例
server.bind(("localhost",6969)) #绑定ip port
server.listen()  #开始监听
print("等待客户端的连接...")
conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
print("新连接:",addr )
while True:

    data = conn.recv(1024)
    if not data:
        print("客户端断开了...")
        break
    print("收到消息:",data)
    conn.send(data.upper())

server.close()

