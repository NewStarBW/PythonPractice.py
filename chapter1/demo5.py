import math
dayup,ddup,dayfactory=1.0,1.0,1.01
for i in range(1,127):
    if i%7 in range(1,6):
        dayup=1.01*dayup
    else:
        dayup=0.99*dayup
for i in range(42):
    dayup=dayup*0.99
for i in range(1,127):
    if i % 7 in range(1, 6):
        dayup = 1.01 * dayup
    else:
        dayup = 0.99 * dayup
for i in range(70):
    dayup=dayup*0.99
print(dayup)
for i in range(1,6):
    print(i)
