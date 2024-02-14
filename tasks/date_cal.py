D = Days = int(input("Enter days: "))
# Currency denominations
yy = 365
mm = 30
ww  = 7
dd = 1
# Calculate years,months,weeks,days
y = D // yy
r= D % yy

m = r//mm
r = r % mm

w = r //ww
r = r % ww

d = r // dd
r = r % dd

print(f"""Approximately  In {D} Days we have
    Years   {y}   
    Months  {m} 
    Weeks   {w} 
    Days    {d} """)