# Taking total amount as input from user
amount =int(input("Please Enter Amount for Withdraw :"))

# Calculating the number of notes of different denominations
c2000=amount//2000
amount=amount-(c2000*2000)

c500=amount//500
amount=amount-(c500*500)

c200=amount//200
amount=amount-(c200*200)

c100=amount//100
amount=amount-(c100*100)

c50=amount//50
amount=amount-(c50*50)

c20=amount//20
amount=amount-(c20*20)

c10=amount//10
amount=amount-(c10*10)

coins=amount

print( "notes of 2000 rupee" , c2000)
print("notes of 500 rupee" , c500)
print("notes of 200 rupee" , c200)
print( "notes of 100 rupee" , c100)
print("notes of 50 rupee" , c50)
print("notes of 20 rupee" , c20)
print("notes of 10 rupee" , c10)
print("number of coins in rupee",coins )