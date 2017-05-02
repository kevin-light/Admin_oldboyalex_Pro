# product_list = [
#     ('iphone',5800),
#     ('mac pro',9800),
#     ('bike',800),
#     ('watch',10000),
#     ('coffee',38)
#
# ]
# shopping_cart = []
#
# Alvailable_banlance = input("recharge >>:")
#
# if Alvailable_banlance.isdigit():
#
#     Alvailable_banlance = int(Alvailable_banlance)
#     while True:
#         for index,item in enumerate(product_list):
#             print(index,item)
#         user_choice = input("选着买什么》》：")
#         if user_choice.isdigit():
#             user_choice = int(user_choice)
#             if user_choice < len(product_list) and user_choice >= 0:
#
#                 p_item = product_list[user_choice]
#
#                 if p_item[1] <= Alvailable_banlance:
#                     shopping_cart.append(p_item)
#                     Alvailable_banlance -= p_item[1]
#                     print("added %s into shopping cart,you current balance is \033[31;1m%s\033[0m" % (p_item,Alvailable_banlance))
#                 else:
#                     print("\033[41;1m月剩余[%s],\033[0m" % Alvailable_banlance)
#             else:
#                 print("product code [%s] is not exist" % user_choice)
#         elif user_choice == 'q':
#             print('---shopping lsit ---')
#             for p in shopping_cart:
#                 print(p)
#             print("you carrent balance:",Alvailable_banlance)
#             exit()
#         else:
#             print("invalid option")
#
#
# else:
#     print("please enter a positive integer")
#

product_list = [
    ('iphone', 5800),
    ('mac pro', 16000),
('watch', 1000),
('coffee', 36),
('back', 588),
]

product_cart = []

recharge_amount = input("充值金额>>:")
if recharge_amount.isdigit():
    recharge_amount = int(recharge_amount)
    while True:
        for index, p_item in enumerate(product_list):
            print(index,p_item)
        product_choice = input("product choice index >>:")
        if product_choice.isdigit():
            product_choice = int(product_choice)

            if 0 <= product_choice <= len(product_list) and recharge_amount >= p_item[1]:
                p_item = product_list[product_choice]

                product_cart.append(p_item)
                recharge_amount -= p_item[1]
                print("product choice is %s ,Available balance %s" % (product_cart,recharge_amount))
            else:
                print("余额不足")
        else:
            print("product choice id not pro_list")
else:
    print("充值失败，金额【%s】无效" % recharge_amount)
