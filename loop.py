for num in range(1, 100+1): 
      
    # checking condition 
    if num % 2 == 0: 
        print(num, " ") 
#for odd no
for num in range(1,100): 
      
    # checking condition 
    if num % 2 != 0: 
        print(num," ")

#factorial of given no 
a = int(input("Enter a number: "))
factorial = 1
for i in range(1,a + 1):
       factorial = factorial*i
print("The factorial of",a,"is", factorial )

#prime no
for p in range(1,101):  
   if p > 1:  
       for i in range(2,p):  
           if (p % i) == 0:  
               break  
       else:  
           print(p)
#tables
table=int(input("enter the table no: "))
for i in range(1,11):
    print(table,'x',i,'=',table*i)