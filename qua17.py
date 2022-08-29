# Write a python program to input basic salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

from ctypes.wintypes import HACCEL


basic_selary=int(input("enter basic_selary :"))
if basic_selary<=10000:
    HRA=(20%100)*basic_selary
    DA=(80%100)*basic_selary
    print(HRA+DA+basic_selary)
elif basic_selary<=20000:
    HRA=(25%100)*basic_selary
    DA=(90%100)*basic_selary
    print(HRA+DA+basic_selary)
elif basic_selary>20000:
    HRA=(30%100)*basic_selary
    DA=(95%100)*basic_selary
    print(HRA+DA+basic_selary)
else:
    print("enter the code")


    
