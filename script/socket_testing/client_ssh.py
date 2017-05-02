# import socket
# import sys
#
# client = socket.socket()
# client.connect(("localhost",8000))
#
# while True:
#     msg = input(">>:").strip()
#     if len(msg) == 0: continue
#     client.send(msg.encode("utf-8"))
#
#     res_return_size = client.recv(1024)
#     print("get cmd result", res_return_size)
#     total_rece_size = int(res_return_size)
#     print("totle size",res_return_size)
#     client.send("准备好接受".encode("utf-8"))
#     received_size = 0
#     cmd_res = b''
#     f = open("test_copy.html","wb")
#     while received_size != total_rece_size:
#         data = client.recv(1024)
#         received_size += len(data)
#         cmd_res += data
#     else:
#         print("数据收完了",received_size)
#         f.write(cmd_res)
#
# client.clsoe()



import socket
import sys

client = socket.socket()

client.connect(("localhost",9999))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )

    res_return_size  = client.recv(1024) #接收这条命令执行结果的大小
    print("getting cmd result , ", res_return_size)
    total_rece_size = int(res_return_size)
    print("total size:",res_return_size)
    client.send("准备好接收了,发吧loser".encode("utf-8"))
    received_size = 0 #已接收到的数据
    cmd_res = b''
    f = open("test_copy.html","wb")#把接收到的结果存下来,一会看看收到的数据 对不对
    while received_size != total_rece_size: #代表还没收完
        data = client.recv(1024)
        received_size += len(data) #为什么不是直接1024,还判断len干嘛,注意,实际收到的data有可能比1024少
        cmd_res += data
    else:
        print("数据收完了",received_size)
        #print(cmd_res.decode())
        f.write(cmd_res) #把接收到的结果存下来,一会看看收到的数据 对不对
    #print(data.decode()) #命令执行结果

client.close()
