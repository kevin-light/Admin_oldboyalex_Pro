#
# import socket
#
# client = socket.socket()
# client.connect(('localhost',6969))
#
# while True:
#     msg = input(">>").strip()
#     if len(msg) == 0: continue
#     client.sent(msg.encode("utf_8"))
#     data = client.recv(1024)
#     print("服务器recv:", data.decode())
#
# client.close


import socket

client = socket.socket()
client.connect(("localhost",6969))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )

    data = client.recv(1024)
    print("来自服务器:",data)

client.close()

#socket客户端支持多交互