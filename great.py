P= float(input("Enter first number: "))
Q= float(input("Enter second number: "))
R = float(input("Enter third number: "))
 
if (P > Q) and (P > R):
   largest = p
elif (Q > P) and (Q > R):
   largest = Q
else:
   largest = R
 
print("The largest number is",largest)