#测试完全数
def isperfect(num):
    slist=[]
    count =num-1
    while count>=1:
        if num % count == 0:
            slist.append(count)
        count-=1
    if sum(slist)==num:
        return True
    else:
        return False
