# import socket
# import os,subprocess
#
# server = socket.socket()
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# server.bind(("localhost",8000))
# server.listen()
#
# while True:
#     print("等待客户端连接。。。")
#     conn,addr = server.accept()
#     print("新链接",addr)
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             print("客户端断开了。。。")
#             break
#         print("收到命令：",data)
#        #res = os.popen(data.decode()).read()
#         res = subprocess.Popen(data,shell=True,stderr=subprocess.PIPE).stdout.read()
#
#         if len(res) == 0:
#             res = "cmd exec success ,has not output".encode("utf-8")
#         conn.send(str(len(res)).endcode("utf-8"))
#         print("等待ack应答。。。")
#         client_final_ack = conn.recv(1024)
#         print("客户应答",client_final_ack.decode())
#         print(type(res))
#         conn.sendall(res)
#
# server.close()





import socket
import os,subprocess


server = socket.socket() #获得socket实例
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost",9999)) #绑定ip port
server.listen()  #开始监听

while True: #第一层loop
    print("等待客户端的连接...")
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:

        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break #这里断开就会再次回到第一次外层的loop
        print("收到命令:",data)
        #res = os.popen(data.decode()).read() #py3 里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下
        res = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE).stdout.read() #跟上面那条命令的效果是一样的
        if len(res) == 0:
            res = "cmd exec success,has not output!".encode("utf-8")
        conn.send(str(len(res)).encode("utf-8")) #发送数据之前,先告诉客户端要发多少数据给它
        print("等待客户ack应答...")
        client_final_ack = conn.recv(1024) #等待客户端响应
        print("客户应答:",client_final_ack.decode())
        print(type(res))
        conn.sendall(res) #发送端也有最大数据量限制,所以这里用sendall,相当于重复循环调用conn.send,直至数据发送完毕

server.close()
