days = int(input("Enter Days: "))

M = 30.4
w = 7
print(days)

D = days
R = D / M
if R ==0:
   print(f"enter a valid number:{D}")
else:
   m1 = int(R)
   a = m1*M
   r = D-a
   
   R_2 = r/w
   if R_2 ==0:
      print(f"the total no months{m1}and weeks{R_2}and days {0}")#weeks
   else:
      b = int(R_2)
      a_1 =b*w
      r_1 = r-a_1

if m1==1 and b==1 and r_1==1:  
   print(f"approximately in {D} days we have {m1} month and {b}week and {r_1} day ")
elif m1==1 and b==1 and r_1!=1:  
   print(f"approximately in {D} days we have {m1} month and {b}week and {r_1} days ")
elif m1==1 and b!=1 and r_1==1: 
   print(f"approximately in {D} days we have {m1} month and {b}weeks and {r_1} day ")
elif m1==1 and b!=1 and r_1!=1: 
   print(f"approximately in {D} days we have {m1} month and {b}weeks and {r_1} days ")
elif m1!=1 and b==1 and r_1==1:  
   print(f"approximately in {D} days we have {m1} months and {b}week and {r_1} day ")
elif m1!=1 and b==1 and r_1!=1:  
   print(f"approximately in {D} days we have {m1} months and {b}week and {r_1} days ")
elif m1!=1 and b!=1 and r_1==1: 
   print(f"approximately in {D} days we have {m1} months and {b}weeks and {r_1} day ")
elif m1!=1 and b!=1 and r_1!=1: 
   print(f"appeoximately in {D} days we have {m1} months and {b}weeks and {r_1} days ")



name ="GOAT⊥"