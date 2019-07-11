#IS a feacturs

#DEcorators add extra fetures in existing FUnctions

def div(a,b):
    return a/b

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1=smart_div(div)
res=div1(2,4)
print(res)

#Change The BEhavior of exixsting Function
