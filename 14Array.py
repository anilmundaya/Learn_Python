# #Same like other array .Only same data type is alloweed
#
import array as ar
#
# values =ar.array('i',[2,3,4,5,6]) #You have to specigy type code
#
# for i in values:
#     print(i)
# print(values)
#
# print(values.buffer_info()) #size of array
# print(values[0],values[2])

# array values coming from user
arr= ar.array('i',[])

n = int(input("Enter the length of array"))
for i in range(n):
    x=int(input("Enter the value of array"))
    arr.append(x)
print(arr)

# Searcjing in array

value = int(input("Enther the value to search"))
k=0
for i in arr:
    if i == value:
        print('your array at',k)
        break

    k=+1

# doing searching using function

print(arr.index(value))
