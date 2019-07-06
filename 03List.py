# nums =[23,23,56,13,78,14]
#names=['anil','aiswarya','arun']
# print(nums)
# print(names)
# ara=[nums,names]
# print(ara)
# nums.append(21)
# nums =[23,23,56,13,78,14]


# NOt and IN
# names=['anil','aiswarya','arun']
# print("anil" in names)
# print(not "anil" in names)
# print(not "mini" in names)

# list Functions
nums =[23,23,56,13,78,14]
nums.append(30)
nums.insert(0,99)
print(len(nums),nums)
nums.remove(78) #remove by value in index
nums.pop(2) #remove value by index number
print(nums)
nums.pop()
print(nums)
del nums[3:] #deleted from the value assigned      :
print(nums)

nums.sort()
min(nums)
max(nums)
print(nums)
