

class car:

    #Variable define outside init is class variable Class variable also known as Static Variable
    #Variable Define inside init is instance

    wheels=4

    def __init__(self):
        self.millage=20
        self.com="RR"






c1=car()
c2=car()

c1.millage=18
c1.com="BMW"

#When you want to change the name of an clss variable

car.wheels=8

print(c1.millage,c1.com,c1.wheels)
print(c2.millage,c2.com,c2.wheels)
