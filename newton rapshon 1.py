# NRM
def f(x):
    return 2*x**3-2*x-5
def df(x):
    return 6*x**3-2
a = float(input("Enter an intial guess:"))
z = float(input("no. of significant value:"))
E=10**(-z)

n=50
i=0
while i<n:
     if df(a)!=0:
        if abs(f(a)/df(a))>=E:#stopping condition
            h=(f(a)/df(a))
            c=a-h
            print(f"iteration{i+1} approximation is",c)
            i+=1
            a=c
        else:
            break
     else:
            break
print(" finial approximation is",c)
            
        