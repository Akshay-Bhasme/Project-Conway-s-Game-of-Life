def lcm(a,b):
    high= max([a,b])
    
    while high>1:
        if high%a==0 and high%b==0:
            return high
        else:
            high+=1

print(lcm(13,7))
