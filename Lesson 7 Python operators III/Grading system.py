#calculate average of three subjects marks and tell the grade
English=int(input("Enter marks in english "))
Maths=int(input("Enter marks in Maths "))
Computer=int(input("Enter marks in Computer "))
avg=(English+Maths+Computer)/3
print("Your average is",avg)
if avg>=91 and avg<=100:
    print("your Grade is A1")
elif avg>=81 and avg<=91: 
     print("your Grade is A2")
elif avg>=71 and avg<=81:
     print("your Grade is B1")
elif avg>=61 and avg<=71:
     print("your Grade is B2")
elif avg>=51 and avg<=61:
     print("your Grade is C1")
elif avg>=41 and avg<=51:
     print("your Grade is C2")
elif avg>=33 and avg<=41:
     print("your Grade is D")
elif avg>=21 and avg<=33:
     print("your Grade is E1")
elif avg>=0 and avg<=21:
     print("your Grade is E2")
else:
    print("Wrong Input")                         