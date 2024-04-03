#字符串相关工具

def str_reverse(s):
#接受传入字符串，将字符串反转返回
    return s[::-1]
        
def substr(s,x,y):
#按照下标x和y，对字符串进行切片
    return s[x:y]
    
if __name__ == __name__:
    print(str_reverse("Raphtalia"))
    print(substr("Raphtalia",0,4))