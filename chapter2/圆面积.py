import math
r=eval(input("圆的半径\n"))
area=math.pi*r**2
judge=input("圆面积默认保留两位小数，若需要自定义位数，请输入yes,否则输入no\n")
if judge=='yes':
    n=int(input('请输入需要保留的小数位数\n'))
    print(round(area,n))
else:
    print(round(area,2))