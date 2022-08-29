from cgi import print_exception
from random import random
import rockpapaer 
rock='''
   ---
---'  -----)
      (-----)
      (----)
      (----)
      (---)
---'---(---)
'''
paper='''
    ----
---'----(----)

     -----)
     --------)
     -----------)
     --------------)
---'-------------)
'''
scissors='''
  ------
---'  ----)----
     ------)
     -----------)
     (------)
---'---(---)
'''
print(rock)
user_choice=int(input("what do you choice?type 0 for rock,1 for paper or 2 for scissors.\n?"))
computer_choice=random.radint(0,2)
print(f"computer choice{computer_choice}")

if user_choice==0  and computer_choice==2:
     print("you win")
elif computer_choice>user_choice:
     print("you loss")
else:
     print("youn type an invalid number you loss?")
                             
                        

