def feb(num):
    lst=[]
    for i in range(0,num+1):
        if i<=1:
            print(i)
            lst.append(i)
        else:
            print(sum(lst[-2:]))
            lst.append(sum(lst[-2:]))

#feb(10)
def feb2(num):
    return num if num<=1 else (feb2(num-1)+feb2(num-2))

for i in range(10+1):
    print(feb2(i))