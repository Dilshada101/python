a=int(input("Enter the ist number:"))
b=int(input("Enter the second number:"))

print("The value of ",a,"+",b,"=",a+b)
print("The value of ",a,"-",b,"=",a-b)
print("The value of ",a,"*",b,"=",a*b)
print("The value of ",a,"/",b,"=",a/b)
print("The value of ",a,"//",b,"=",a//b)
print("The value of ",a,"%",b,"=",a%b)
print("The value of ",a,"**",b,"=",a**b)


# using match case
def calculator():
    print("choose operator:+,_,/,*")
    op=input("Enter the opertor:")
    a=int(input("Eter the ist number:"))
    b=int(input("Enter the 2nd number:"))
    match op:
        case "+":
            print("Addition of 2 no.s is:",a+b)
        case "-":
            print("subtraction of 2 no.s is",a-b)
        case "*":
            print("Multiplication of 2 no.s is",a*b)
        case "/":
            print("Division of 2 no.s is",a/b)
        case _:
            print("invalid operator")

calculator()