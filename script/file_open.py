# f = open("yesterday.txt",'r')
#
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell)
# f.seek(0)
# print(f.readline())


# # for i in range(5):
# #     print(f.readline())
#
# for index,line in enumerate(f.readlines()):
#

# count = 0
#
# for line in f:
#     if count == 9:
#         print('__----==-----')
#         count += 1
#         continue
#     print(line)
#     count += 1

#
# import sys
# for i in range(10):
# sys.stdout.write("#")


# import sys,time
#  进度条方式打印
# for i in range(20):
#     sys.stdout.write("$")
#     sys.stdout.flush()
#     time.sleep(0.1)



#字符串插入
# f = open("yesterday2","r",encoding="utf-8")
# f_new = open("yesterday2","w",encoding="utf-8")
#
# for line in f:
#     if '就如夜晚的微风' in line:
#         line = line.replace("就如夜晚的微风","如夜晚的风抽麦浪")
#     f_new.write(line)
#
# f.close()
# f_new.close()

#
# with open("yesterday2","r",encoding="utf-8") as f:
#     for line in f:
#         print(line)