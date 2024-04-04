#hello world!
#json练习
#列表、字典转换json
import json

data1 = [{"name":"拉芙塔莉雅"},{"age":14}]
data2 = {"name":"Rapgtalia","AGE":14}
json_str1 = json.dumps(data1)
json_str2 = json.dumps(data1,ensure_ascii=False)
print(json_str1)
print(json_str2)
str1 = json.loads(json_str1)
print(str1)