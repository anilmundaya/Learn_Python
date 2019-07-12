
#Instace Method
# class method
# static method

class student:

    #Static Variable

    clg="MNC"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


#Instance Method


    def avg(self):
        return self.m1+self.m2+self.m3/2

    def m1(self):
        return self.m1

    @classmethod
    def info(cls):
        return cls.clg




s1 = student(21,34,54)
s2 = student(56,75,34)


print(s1.avg())
print(s2.avg())
print(student.info())
