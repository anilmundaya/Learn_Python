

#data Base and Concept

#Text File


file=open('Myfile','r') #File name and mode


print(file.readline(),end='')
# print(file.readline())

file2=open('NewFile','w')
file3=open('NewFile','a')
file2.write('Secoud file created by pyhon')
file3.write('\n added one more line')


for data in file:
    print(data)
for data in file:
    file3.write(data)
