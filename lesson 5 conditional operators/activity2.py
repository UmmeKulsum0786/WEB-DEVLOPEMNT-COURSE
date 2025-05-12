#to check the profit 
costprice=int(input("Enter the buying price of the product "))
sellingprice=int(input("Enter the selling price of the product "))
if(sellingprice>costprice):
      print("profit")
      pt=sellingprice-costprice
      print(pt)
else :
  print("No profit")