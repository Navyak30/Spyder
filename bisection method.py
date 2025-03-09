# BISECTION FORMULA
import math
def f(x):
    return x**2-4
a=float(input("Enter lower limit:"))
b=float(input("Enter lower limit:"))
z=float(input("Enter significant digit:"))
E = 10**(-z) # tolrance value
n = math.ceil((math.log(abs(b-a)/E))/math.log(2))#no. of iteration
print("no of iteration n:",n)
i=1
while i<n:
    c=(a+b)/2
    if f(a)>0 and f(b)<0:
       if f(c)>0:
          c=a
       elif f(c)<0:
           c=b
           
    elif(a)<0 and f(b)>0:
       if f(c)<0:
          c=a
       elif f(c)>0:
            c=b
    print(f"{i} iteration approx",c)
    i+=1
    
        