#用循环发工资
import random
memory = 10000
wno =1
while wno <= 20 :

    if memory <= 0 :
         
         print("工资发完了，下个月再来领取吧")
         break
    num = random.randint(1,10)
    if num >= 5:
         
         memory -= 1000
         print(f"员工{wno}发放工资1000元，财产余额剩余{memory}元")
    else:
         
         print(f"员工{wno}，绩效分{num}，低于5，不发工资，下一位。")
    wno += 1

#自定义函数提醒下课
def relax (sno):
     print(f"学号{sno}同学，下课了")

relax(202220040129)

#自动查核酸
def access():
     print("欢迎来到梅洛马格！\n请出示您的健康码以及72小时核酸证明！")

access()

#自定义加法
def add(a,b):
     result = a + b
     return result

result = add(5,2)
print(result)
