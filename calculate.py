print("Welcome to the Love Calculator")
name1=input("What is your name?\n")
name2=input("What is their name?\n")
combined_string=name1+name2
lower_case_string = combined_string.lower()


t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true=t+r+u+e

O=lower_case_string.count("o")
V=lower_case_string.count("v")
E=lower_case_string.count("e")

LOVE= L + O + V + E

love_score=int(str(true)+str(LOVE))


print(love_score)
if (love_score<10) or (love_score>90):
    print(f"your love score is {love_score},you go together like cake and mentos")
elif (love_score>=40) and (love_score<=50):
    print(f"your score is {love_score},you are alright together.") 
else:
    print(f"your score is {love_score}")
    
    
    
    

