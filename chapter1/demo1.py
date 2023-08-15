# coding:utf-8  #中文编码声明，将文档转为utf-8类型
from decimal import Decimal
import keyword
fp=open("D:/tepo.txt","a+")
print("注意看",file=fp)    # 文件写入
fp.close()
print(keyword.kwlist)   # 显示标识符
print(Decimal('1.1')+Decimal('2.2'))
print(0b1101111111)         # 避免浮点存储显示错误
f=12
print(type(f))
ff=True
print((type(ff)))       # 输出数据类型
print(ff)
print(chr(0b100111001011000))   # 0b/0o/0x分别表示二、八、十六进制。chr将编码转化为字符
print(ord('乘'))     # ord将字符转化为编码对应十进制数
str1="""人生苦短
，我用Python"""        # 三引号可以换行
print(str1)
''' #三引号多行注释
这是注释
这也是注释
'''
name="张三"
age=20
print("名字是："+name+"，年龄是："+str(age))     # "+"表示连接，但必须为相同类型。所以将int转化为str//str为纯数字，可以转化为int//
# float转int抹零取整
a=b=c=20
print(a,id(a))  # 获得地址
print(b,id(b))
print(c,id(c))