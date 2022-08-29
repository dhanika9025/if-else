a=[2,2,3,5,5,9]
i=0
k=[]
while i<len(a):
    if a[i] not in k :
        k.append(a[i])
        i=i+1
print(k)