#learning AND & OR Logical Operators
#Use of AND to Find the greatest number among three of them
a=int(input("Enter first number: "))
b=int(input("Enter Second number: "))
c=int(input("Enter Third number: "))
if a>b and a>c:
    print(a, ' is the greatest number among all!')
elif b>c and b>a:
    print(b," is the greatest number among all!")    
else:
    print(c, " is the greatest number among all! ")


#To check if the person is eligible for loan or not,A country defines a rule that any citizen who:
#a.)Has attained the age of 18 0r b.)his/her income is greater than 15000$ can apply for Loan.
income=int(input("Enter your income to check: "))
age=int(input("Enter your age to check: "))
if age>=18 or income>15000:
    print("You are eligible for applying for Loan:-)")
else:
    print("Not eligible for Loan")         

