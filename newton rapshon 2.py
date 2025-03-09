def f(x):
    return x**2-2*x+1
def df(x):
    return 6*x**3-2
a = float(input("Enter an intial guess:"))
z = float(input("no. of significant value:"))
m= int(input("Enter the multiplicity factor:"))
E=10**(-z)

n=50
i=0
while i<n:
     if df(a)!=0:
        if abs(f(a)/df(a))>=E:
            h=(f(a)/df(a))
            c=a-m*h
            print(f"iteration{i+1} approximation is",c)
            i+=1
            a=c
        else:
             break
     else:
         break
print("final approximation is",c)

         


