# Error Handlingggggggggg


#Run time error Handling


a = 5
b = 0
try:
   print("Resource Open")
   print(a/b)
   #print("Resource Closed")
except Exception as e:
     print(e)
     #print("division By zero")
     #print("Resource Closed")
finally:
      print("Resource Closed")
print('Bye')

