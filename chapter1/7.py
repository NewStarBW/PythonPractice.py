import math
dayup,daydayup,dayfactory = 1.0,1.0,0.01
for i in range(1,127):
    if i % 7 in [6,0]:
        dayup *=1.0 - dayfactory
    else:
        dayup *=1.0 + dayfactory#秋季学期18周
dayup *= math.pow((1 - dayfactory), 42)#寒假6周
for i in range(1,127):
    if i % 7 in [6,0]:
        dayup *=1.0 - dayfactory
    else:
        dayup *=1.0 + dayfactory#春季学期18周
dayup *= math.pow((1 - dayfactory), 70)#暑假10周
daydayup = math.pow((1 + dayfactory), 365)#一年每天都在学习
print("第二年秋季的能力值是:{:.2f},{:.2f}.".format(dayup,daydayup))
