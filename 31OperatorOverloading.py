#
#
# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self, other):
#          m1=self.m1 + other.m1
#          m2=self.m2+other.m1
#          s3=student(m1,m2)
#          return s3
#
#
#
#
# s1=student(59,68)
# s2=student(58,67)
# s3=s1+s2
# print(s3.m1)
# print(s3.m2)


#Method OverLoding same methos name with different parameters

#Method Overridding same methos name with same  parameters different class

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:s=a
        return s

s1=student(59,68)
print(s1.sum(3,4))


#Mthod overriding
class a:
     def show(self):
         print("In a Show")

class b(a):
    def show(self):
        print("In a show 3")

a1 = a()
a2 = b()
a2.show()
