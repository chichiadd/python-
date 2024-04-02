f = open("D:\\word.txt","r",encoding="UTF-8")
# #全部读取,并统计单词数量
# count = 0
# content = f.read()
# print(content)
# count = content.count("raphtalia")
# print(f"raphtalia出现的次数为{count}")

#全部读取,并统计单词数量2
# count = 0
# content_line = f.readlines()
# for word in content_line:
#     if word == "Raphtalia":
#         count += 1
# print(f"Raphtalia出现的次数为{count}")

#读取内容，一行一行读取
count = 0
for line in f:
    line = line.strip()
    words = line.split("，")
    for word in words:
        if word == "raphtalia":
            count += 1
print(f"raphtalia出现的次数为{count}")

f.close()

