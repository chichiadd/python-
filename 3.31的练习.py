#元素去重
my_list = ["raphtalia","raphtalia","raphtalia","raphtalia","adchichi","chichi","add"]
print(f"有列表{my_list}")
my_set = set()
for x in my_list:
    my_set.add(x)
print(f"存入集合后的结果是{my_set}")

#字典应用：升职加薪
#通过for循环让所有级别为1的职工级别升1级，并加1000元薪水
offer = {'王力宏':{"部门":"科技部","工资":3000,"级别":1},
         '周杰伦':{"部门":"市场部","工资":5000,"级别":2},
         '林俊杰':{"部门":"市场部","工资":7000,"级别":3},
         '张学友':{"部门":"科技部","工资":4000,"级别":1},
         '刘德华':{"部门":"市场部","工资":6000,"级别":2}}
print(f"全体员工的信息如下：\n{offer}")
#用for循环对字典进行遍历
for num in offer:
    if offer[num]["级别"] == 1:
        offer[num]["级别"] += 1
        offer[num]["工资"] += 1000
print(f"对全体员工级别为1的员工完成升职加薪操作，操作后：\n{offer}")
         