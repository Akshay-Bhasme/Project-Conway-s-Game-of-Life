#Prime Number
def prime(l,u):
    for i in range(l,u+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

prime(2,10)