import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 5:
    print("Usage: python TASK3.py A <value_a> B <value_b>")
    sys.exit(1)

# Extract command-line arguments
if sys.argv[1] == 'A':
    A = sys.argv[2]
    B = sys.argv[4]
elif sys.argv[1] == 'B':
    A = sys.argv[4]
    B = sys.argv[2]
else:
    print("Invalid usage. Please use A and B to specify values for A and B.")
    sys.exit(1)

# Check if the inputs are valid numbers
try:
    a = float(A)
    b = float(B)
except ValueError:
    print(f"Invalid data. Please provide valid numbers for A and B. Given values: {A}, {B}")
    sys.exit(1)

# Perform calculations
z = a + b
j = b - a
c = a * b
d = a/b
e = a**b
f = b**a
print(f"Sum: {z}")
print(f"Difference: {j}")
print(f"Multiplied: {c}")
print(f"division:{d}")
print(f"exponential of a^b is:{e}")
print(f"exponential of b^a is:{f}")