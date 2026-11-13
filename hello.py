name = input("what's your name? ")
name = name.strip()
#去除空白格
name = name.title()
#首字母大写但是其余字母小写
first, last = name.split(" ")
#split 用法就是以“”里的内容为分隔符号把字符串切开作为一个列表
print(f"hello,{first}")
