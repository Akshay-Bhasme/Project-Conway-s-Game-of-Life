def fact(num):
    return 1 if num==1 else (num*fact(num-1))

print(fact(5))

def fact2(num):
    prod=1
    for i in range(1,num+1):
        prod*=i
    print(prod)

fact2(5)