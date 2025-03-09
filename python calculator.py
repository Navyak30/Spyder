def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divid(a,b):
    if b==0:
        return "cannot divide"
    else:
        return a/b
def calculator():
    print("select operation")    
    print("1.add") 
    print("2.sub") 
    print("3.mul") 
    print("4.divid") 
    choice=input("enter choice(1/2/3/4)=")
    if choice in["1","2","3","4"]:
      n1=float(input("enter no."))
      n2=float(input("enter no."))
      if choice=="1":
          print(add(n1,n2))
      elif choice=="2":
          print(sub(n1,n2))  
      elif choice=="2":
          print(sub(n1,n2)) 
      elif choice=="3":
          print(mul(n1,n2))  
      elif choice=="4":
          print(divid(n1,n2))     
      else:
          print("invalid input")
calculator()
