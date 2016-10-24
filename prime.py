#测试一个整数，是否为质数
num =947
count =num-1
while count>0:
    if num%count==0:
        print(num,count)
        break
    count-=1
