# W.A.P Take input from user for marks of five subject and calculate the average of marks and print it
English= int(input("Enter your marks in English out of 100 "))
Computer=int(input("Enter your marks in Computer out of 100 "))
Science=int(input("Enter your marks in Science out of 100 "))
Mathematics=int(input("Enter your marks in Maths out of 100 "))
Social_Studies=int(input("Enter your marks in Social studies out of 100 "))
print("Marks in English ",English)
print("Marks in Computer ",Computer)
print("Marks in Science ",Science)
print("Marks in Maths ",Mathematics)
print("Marks in Social_studies ",Social_Studies)
Sum= English + Computer +Science +Mathematics + Social_Studies
perc= float(Sum/500)*100
print("The Calculated percentage is =" , perc,"%") 