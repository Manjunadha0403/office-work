data = input("Enter a data_values:")
alpha_v =[]
num_v =[]

# Renamed the variable to avoid shadowing the built-in str
data_v= data  
# Check the type of input data
a = data_v.split()

print("The given Data:", a)

for words in a:
    if words.isalpha():
        alpha_v.append(words)
        
    elif words.isnumeric():
        num_v.append(words)
    else:
        print(f"Some extra charactres are occured{a}")
        break
print(alpha_v)
for words in alpha_v:
    if words == words[::-1]:  # Check if the word is a palindrome
        print(f"{words} is a PALINDROME")
    else:
        print(f"{words} is NOT a PALINDROME")
        
print(num_v)

i = 0
while i < len(num_v):
    x = num_v[i]
    y = float(x)
    z = int(y)
 
    temp_original = z
    reverse_num = 0

    while z > 0:
        last_digit = z % 10
        reverse_num = reverse_num * 10 + last_digit
        z = z // 10  # Use integer division to update z without the remainder

    if temp_original == reverse_num:
        print(f"{x} is a palindrome.")
    else:
        print(f"{x}The number is not a palindrome.")
    
    i = i + 1