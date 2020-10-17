  
for p in range(1,101):  
   if p > 1:  
       for i in range(2,p):  
           if (p % i) == 0:  
               break  
       else:  
           print(p)  