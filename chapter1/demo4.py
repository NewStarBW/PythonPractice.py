'''
此项目包含循环结构知识点
'''
for item in 'python':
    print((item))       # 取出python元素，放到item
for i in range(10):
    print(i)
for _ in range(10):
    print("人生苦短，我用python")  # 输出十遍
sum=0
for item in range(1,101):   # 输出[a,b)
    if item % 2 == 0:
        sum = sum+item
print(sum)
'''
for :
    if:    
        break       # 没有碰到break,for正常结束，进行最后的else
    else:
else:
'''
a="t"
b="oM   "
c=f"{a} {b}"
d=''' a 
b'''
print("Hello,",c.title(),"!")
print(c.upper())
print(c.lower())
print(b.rstrip()+"kol")
print(c.lstrip())
print(d.strip())
print(1_000_000_000_000_000_000_000_000)
# import this
a = ['vd','da','zsd','yw','ad']
a.sort(reverse=True)
print(a)
print(sorted(a))
a.remove('yw')
print(a)
a.pop(0)
print(a)
a.pop(-1)
print(a)
c=range(10)
print(list(c))
print(len(c))
for a in c:
    print(a)
b=list(range(10))
print(b)
m=[value**2 for value in range(1,10)]
print(m)
print(m[2:5])
v = 1, 2
print(v[0])
languages = {'english', 'chinese', 'japanese'}
print(languages)
test=['a', 'b', 'c', 'd', 'e', 'f']
out=test[:]
out.append('a')
print(out)