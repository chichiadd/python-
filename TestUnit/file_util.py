#文件处理相关工具，内含：)
def print_file_info(file_name):
#接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    f = None
    try:
        f = open("file_name","r",encoding= "UTF-8")
        content = f.read()
        print(f"文件的全部内容为{content}")
    except Exception as b:
        print(f"无法打开文件，问题为{b}")
    finally:
        if f: #如果f为None，该语句不会执行
            f.close
def append_to_file(file_name,data):
#接收文件路径以及传入数据，将数据追加写入到文件中
    f = open("file_name","a",encoding= "UTF-8")
    f.write(data + "\n")
    f.close