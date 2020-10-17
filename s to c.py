#python program that accepts a string and calculate the number of digits and letter 
string=input("Enter string:")
digit=0
count=0
for i in string:
      if(i.isdigit()):
            digit=digit+1
      count=count+1
print("The number of digits is:")
print(digit)
print("The number of characters is:")
print(count-digit)
