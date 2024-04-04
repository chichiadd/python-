#json练习
#列表、字典转换成json型
data = [{"name":"raphtalia","age":14}]
data2 = {"name":"Raphtalia"}
data_str = json.dumps(data,ensure_ascii = False)