x =int(input("enter a number"))
print(x)
y = x-x
z = y*x
print(y)
print(z)
def factors (x):
    if x < 0:
        return 0
    elif x == 0 or x == 1:
        return 1
    else:
        fact = 1
        while(x > 1):
            fact *= x
            x -= 1
        return fact
print("Factorial of",x,"is",factors (x))
if x > 1:
    for i in range(2, int(x/2)+1):

        if (x % i) == 0:
            print(x, "is not a prime number")
            break
    else:
        print(x, "is a prime number")

else:
    print(x, "is not a prime number")
def My_Function ():
    n = x
fact = 1
 
for i in range(1, x+1):
    fact = fact * i
 
print("The factorial of x is : ", end="")
print(fact)
My_Function()