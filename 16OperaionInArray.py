from numpy import *

arrr=array([2,3,4,5,6,7])
arr=array([2,3,4,5,6,7])

#arrr = arrr+5
a = arrr+arr

print(sin(arrr))
print(sum(arrr))
print(min(arrr))
print(max(arrr))
print(a)


#Concaniate 2 arrat

print(concatenate([arrr,arr]))


#Copy an Array

ar=arrr.view()
