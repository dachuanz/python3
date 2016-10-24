def getfactors(num):
    slist=[]
    count = num
    while count>=1:
        if num % count == 0:
           slist.append(count) 
        count -= 1
    return slist
