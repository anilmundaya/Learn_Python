from numpy import *

arr = array([[1,2,3],[9,8,7]])

print(arr)
print(arr.ndim) #dimetion of array
print(arr.shape) #number of  row and colum

arr2 = arr.flatten() #from multidieemtioal to singlw
#arr3 = arr2.reshape(2,4)

print(arr2)
#print(arr3)


m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('1,2,3;4,5,6;7,8,9')
print(m1)
print(diagonal(m1))
print(m1.min())


m3=m1*m2
m4=m1+m2
print(m3)
print(m4)
