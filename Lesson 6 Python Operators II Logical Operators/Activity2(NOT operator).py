#Understanding NOT operator means if value is 1True it will return False and vice versa
v1=True
v2=False
if not v1:
    print("I am v2 and my value is False")
if not v2:
    print("I am v1 and my value is True")  
    
      
a = int(10)
b = 12
c = 12

print(a != b)
print(b != c)


a = "python"
b = "coding"

if a != b :
    print(a, 'and', b, 'are different.')


a = 4
b = 5

if (a == 1) != (b == 5):
    print('Hello')




a1 = int(input("enter a number"))

if a1%2 != 0 :
    print(a1, "is not even number.")
    
    