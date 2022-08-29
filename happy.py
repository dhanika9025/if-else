n=int(input("enter number"))
x=n
while x>=10:
    sum=0
    while x>0:
        k=k%10
        sum=sum+(k**2)
        k=k//10
    x=sum
    print("sum",sum)
if x==1:
    print(n, "happy number")
else:
    print(n,"not happy number")