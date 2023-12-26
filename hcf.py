def hcf(a,b):
    mini= min([a,b])
    hcf=1
    for i in range(2,(mini//2+1)):
        if a%i==0 and b%i==0:
            hcf=i
    print(hcf)

hcf(48,54)