#program for simple calculator
c='y'
while c=="y" or "Y":
    choice=int(input("Enter choice to perform following operation: \n 1:Addition \n 2:Subtraction \n 3:Multiplication \n 4:Division \nYour Choice: "))
    if choice==1 or choice==2 or choice==3 or choice==4:
        a=float(input("Enter first number"))
        b=float(input("Enter second number"))
        print("Result=",end="")
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a/b)
    else:
        print("Kindly choose number from 1 to 4")
    c=input("Enter y/Y if you want to continue or N if not :")
    if c=="y" or c=='Y':
        continue
    else:
        break