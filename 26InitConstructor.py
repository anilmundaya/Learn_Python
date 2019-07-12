

class Computer:
    def __init__(self):
        self.name='anil'
        self.age=21

    def update(self):
         self.age=30

    def compare(self,other):
         if self.age==other.age:return True
         else:return False

#Every time  you Create an Object ir Create Different Spaces
c1 = Computer()
c2 = Computer()


print(id(c1))
print(id(c2))
# c1.name="Arun"
# c1.age=22
c1.update()
if c1.compare(c2):
    print("There age are same")
else:print("differnet")


print(c1.name)
print(c2.name)
