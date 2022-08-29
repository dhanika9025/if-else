year=int(input("enter which year do you want to check?  :"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leapyear")
        else:
            print("not leapyear")
    else:
        print("leap year")
else:
    print(" not  leapyear")
