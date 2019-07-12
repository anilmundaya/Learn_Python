
class a:

    def feture(self):
        print("working 1")

    def feture2(self):
        print("working 2")

# class b(a):
#     def feture3(self):
#         print("working 3")
#
#     def feture4(self):
#         print("working 4")

class b:
    def feture3(self):
        print("working 3")

    def feture4(self):
        print("working 4")

class c(a,b):
    def feture5(self):
        print("working 5")

    def feture6(self):
        print("working 6")



a1 =a()
b1 =b()
c1 =c()

a1.feture()
a1.feture2()


# b1.feture()
# b1.feture2()
b1.feture3()
b1.feture4()


c1.feture()
c1.feture2()
c1.feture3()
c1.feture4()
c1.feture5()
c1.feture6()
