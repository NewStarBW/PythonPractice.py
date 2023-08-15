import random
A=random.randint(1,101)
print(A)
guss=int(input('请输入第1次猜测数\n'))
for i in range(2,7):
    if guss==A:
        print('你猜对了')
        break
    elif i==6:
        print('你的十次猜数机会已经用完')
        break
    elif guss<A:
        print('你猜小了')
        guss=int(input(f'请输入第{i}次猜测数\n'))
    elif guss>A:
        print('你猜大了')
        guss = int(input(f'请输入第{i}次猜测数\n'))
