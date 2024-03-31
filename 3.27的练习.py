# 打印九九乘法表
i = 1
while i <= 9:

    j = 1
    while j <= i:

        print(f"{j}*{i}={i*j}", end='\t')
        j += 1
   
    print("\n")
    i += 1

#记录字符串里有几个a
name = "Raphtalia"
count = 0
for x in name:

    if x == 'a':

        count += 1

print(f"被统计的字符串中有{count}个a")

#1到100（不含100）有多少个偶数
count = 0
for x in range(1,100):

    if x % 2 == 0:

        count += 1

print(f"1到100(不含100)有{count}个偶数")
