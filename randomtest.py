#测试随机数
import random
a =random.randint(2,100)
rlist=[]

for i in range(0,a):
    z=random.randint(0,2**31-1)
    
    rlist.append(z)

zlist= random.sample(rlist,a-1)

print(zlist)
