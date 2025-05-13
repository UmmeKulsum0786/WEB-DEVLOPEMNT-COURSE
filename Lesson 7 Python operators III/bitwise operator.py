# Understanding bitwise operator based on truth table by changing any number to bits
a=5
b=4
print(a&b)#acts as multiplication of bits if both are 1 then only 1 otherwise 0
print(a|b)#acts add addition of bits 0+1=1
print(a^b)#will give one only if both bits are 1 otherwise 0
print(~a)#reverse the bits and add 1 to last bit to find two's complement e.g ~5=>-(5+1)=>-6
print(a<<2)#shift bits to left and add 0s at last e.g 0101=010100
print(a>>2)#discard last two bits from right 0101 =0001