

 #Polymorphisam

 #4 way of implementing this
 #
 #  # Duck Typing
 #  # Oprator Over Loadinf
 #  # method Over Loading
 #  # MEthod Over Ridding

#1 Duck Typing

class pycharm:
    def execute(self):
        print("compaling")
        print("Running")

class vs:
    def execute(self):
        print("spell Check")
        print("extesnion")
        print("tutorials")

class lapTop:
    def code(self,ide): #Duck typing
        ide.execute()

ide=vs()
lap1 = lapTop()
lap1.code(ide)

