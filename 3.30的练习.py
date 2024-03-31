"""
列表常用功能练习
 列表.append(元素)  向列表中追加一个元素
列表.extend(容器) 将数据容器的内容依次取出，追加到列表尾部
列表.insert(下标，元素) 在指定下标处，插入指定的元素
del 列表[下标]   删除列表指定下标元素
列表.pop(下标) 删除列表指定下标元素
列表.remove(元素)从前向后，删除此元素第一个匹配项
列表.clear() 清空列表
列表.count(元素)统计此元素在列表中出现的次数
列表.index(元素)查找指定元素在列表的下标
找不到报错ValueError
len(列表)统计容器内有多少元素
"""
my_list = [21,25,21,23,22,20]
print(my_list)
my_list.append(31)
print(my_list)
my_list.extend([29,33,30])
print(my_list)
x = my_list.pop(0)
print(f"列表的第一个元素是{x}")
y = my_list.pop(-1)
print(f"列表的最后一个元素是{y}")
index = my_list.index(31)
print(f"元素31在列表中的下标是{index}")
print(f"最终的列表为{my_list}")

#取出列表内偶数练习
list = [1,2,3,4,5,6,7,8,9,10]
#while循环
i = 0
while_list = []
while i < len(list):
    if list[i] % 2 == 0:
        while_list.append(list[i])
    i += 1
print(f"用while循环后的列表为{while_list}")
#for循环
for_list = []
for x in list:
    if x % 2 == 0:
        for_list.append(x)
print(f"用for循环后的列表为{for_list}")

#分割字符串
my_str = "I am Raphtalia"
#统计字符串中有多少个a
count = my_str.count('a')
print(f"字符串{my_str}中共有{count}个a")
#将字符串中的空格替换成|
new_my_str = my_str.replace(" ","|")
print(f"字符串{my_str}被替换空格后变成{new_my_str}")
#把字符串中的|去掉
new_my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}按照|分隔变成{new_my_str_list}")

#hello
#world213