DAYS = int(input("Enter Days: "))

days = int(DAYS)

D = 7
print(days)

x = days
R = x / D

if R == 0:
    print(f"The Input is zero give some other input: {R}")
else:
    y = int(R)
    z = y * D
    w = x - z

    if w == 1:
        print(f"In {x} days, we have {y} weeks and {w} day")
    else:
        print(f"In {x} days, we have {y} weeks and {w} days")

print("""https://api-dev.wlb.spreadagency.co.nz/api/products/06ab3a5b-c9d7-4f91-b0a1-af919838b918/""")