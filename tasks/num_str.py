data = input("Enter a data_values:")
data_v= data  
# Check the type of input data
a = data_v.split()
try:
   i = 0
   while i < len(a):
        x = a[i]
        y = float(x)
        n = y*0
        i = i+1
   print(f"The Given data is numeric string{a}")      
except:
    print(f"The Given data is not a numeric string{a}") 