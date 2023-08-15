import random
a= 'in'
print(f"{a=='in'}Is a=='in'?")
print(a == 'in')
lis = []
temp = int(input("请输入元素个数\n"))
b=random.sample(range(1,50),7)
for i in range(temp):
    a = input()
    lis.append(a)
print(f"列表元素如下\n{lis},{b}")