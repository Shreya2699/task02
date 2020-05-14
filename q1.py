def outerFun(a, b):
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5
n1=int(input("enter first num"))
n2=int(input("enter second num"))
sum=outerFun(n1,n2)
print(sum)