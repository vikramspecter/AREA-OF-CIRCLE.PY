a=input("HI WHAT TYPE OF NUMBER DO YOU WANT TO ENTER(INTEGER OR DECIMAL)")
if a=="integer" or a=="INTEGER":
    b=int(input("enter the number"))
    x=b**2
    m=3.14*x
    print("THE AREA OF CIRCLE IS",m)
elif a=="decimal" or a=="DECIMAL" or a=="float" or a=="FLOAT":
    c=float(input("enter the number"))
    y=c**2
    n=3.14*y
    print("AREA OF CIRCLE IS",n)
else:
    print("PLEASE ENTER THE THE CORRECT TYPE OF NUMBER")
