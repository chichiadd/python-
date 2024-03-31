#模拟ATM
money = 5000000
name = input("请输入您的用户名：")
#查询
def query(show_header):
    if show_header:
        print("------查询余额------")
    print(f"{name}您好，您的余额为{money}")
#存款
def saving():
    print("------存款------")
    num = int(input("请输入您想存入的金额："))
    global money
    money += num
    print(f"{name}您好，存款{num}元成功")
    query(False)
#取款
def get_money():
    print("------取款------")
    num = int(input("请输入您想取的金额："))
    global money
    money -= num
    print(f"{name}您好，取款{num}元成功")
    query(False)
#主菜单
def main():
   print("------主菜单------") 
   print(f"{name}，您好，欢迎来到梅格洛马银行ATM，请选择操作：")
   print("查询余额\t[请输入1]")
   print("存款\t\t[请输入2]")
   print("取款\t\t[请输入3]")
   print("退出\t\t[请输入4]")
   return input("请输入您的选择：")
   

while True:
    access = main()
    if access == '1':
        query(True)
        continue
    elif access == '2':
        saving()
        continue
    elif access == '3':
        get_money()
        continue
    else:
        print("程序退出了")
        break
