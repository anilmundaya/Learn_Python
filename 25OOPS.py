
#PYTHON SUPPORT ALL TYPE OF PROGRAMING

#fUNCTIONAL OOPS PROCEDURE


#OOPS
class Computer:
    def __init__(self,cpu,ram): #called automaticcllay same as constrictor
        self.cpu=cpu
        self.ram=ram

    def config(self):

        print("Hp pavilon")
        print(self.cpu,self.ram)
comp = Computer(14,14)
comp1 = Computer(12,13)


comp.config()
comp1.config()


