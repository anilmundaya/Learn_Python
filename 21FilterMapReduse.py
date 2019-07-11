from functools import *

nums =[1,2,3,4,5,6,7,8,9,10,11,12,13]

# def is_even(n):
#     return n%2==0
#eve= list(filter(is_even,nums))


eve= list(filter(lambda n:n%2==0,nums)) # Print even numer
print(eve)

#Duble The even NUmber
#Use Map FUntion

double = list(map(lambda n:n*2,eve))
print(double)

#Reduse FUntion

addAllVal = reduce(lambda a,b:a+b,double)
print(addAllVal)
