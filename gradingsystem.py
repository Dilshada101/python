marks=int(input("Enter the marks:"))
if(marks<=100 and marks>80):
    print("Grade A")
elif(marks<=80 and marks>60):
    print("Grade B")
elif(marks<=60  and marks>=40):
    print("Grade C")
else:
    print("Fail")
# using function
def marks(x):
    if (x<=100 and x>80):
        return "Grade A"
    elif (x<=80 and x>60):
        return "Grade B"
    elif(x<=60 and x>=40):
        return "Grade C"
    else:
        return "fail"
x=int(input("Enter your marks:"))
grade=marks(x)
print("Your grade is:",grade)