print("welcome to python pizza delivers!?")
size=input("what size pizza do y6ou want ?s,m,or l :")
add_pepperoni=input("do youn want pepperoni? yes or no :")
extra_cheese=input("do you want extra chees?y or n :")
bill=0
if size=="s":
    bill=bill+15
elif size=="m":
    bill=bill+20
else:
    bill=bill+25
    
if add_pepperoni=="yes":
    if size =="s":
        bill+=2
    else:
        bill+=3

if extra_cheese=="y":
    bill+=1
    
    
print(f"your final bill is ${bill}")
    
    


                  
                  
                    