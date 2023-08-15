'''
此文件包含程序顺序结构，分支结构等
'''
# 以下对象bool()值为False
'''
False.数值0,None,空字符串，空列表，空元组，空字典，空集合
'''

'''
if 100>a>10:        注意，非常便捷的一点
    if
    else
else:
    if
    else
'''
# a=int(input('请输入一个整数：'))
# b=int(input('请输入另一个整数：'))
# print( (a,'大于等于',b) if a>=b else (a,'小于等于',b))
# pass 语句，占位符，什么都不做，用到需要写语句的地方
'''
answer=input("您是会员吗：y/n\n")
if answer=='y':
    pass
else:
    pass
'''
a=range(5)          # 默认从0开始，步长为一
b=range(5,10)
c=range(5,10,2)
print(a,b,c)        # 输出为迭代器对象
print(list(a),list(b),list(c))  # 可以看到列表
print(2 in a)       # true  not bool(0) 结果为true
