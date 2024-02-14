"""Days Calculation """

from datetime import datetime, timedelta

print("""Select option for year calculation
         A. From Today
         B. Non
         E. Exit""")
while True:
    option = input("Enter option (A/B/E): ")
    operation = option.upper()

    if operation == 'E':
        print("You Choose Option E: ")
        print("Exiting the program.")
        break

    if operation not in ('A', 'B'):
        print("Invalid option. Please enter A, B, or E.")
        continue

    if operation == "A":
        try:
# Get the current system date
            today_date = datetime.now().strftime('%Y-%m-%d')
            print(f"Today's date is: {today_date}")
# Use the current system date as the initial date
            initial_date = datetime.strptime(today_date, "%Y-%m-%d")

            days = int(input("Enter Days: "))
#Final Value for Output from "A"
            final_date = initial_date + timedelta(days=days)
            print(f"The final date from {today_date} after {days} days is {final_date.strftime('%Y-%m-%d')}")
        except ValueError:
            print("Unable to calculate.")
            continue

    elif operation == "B":
        days = int(input("Enter Days: "))
        y = 365.25
        M = 30.4
        w = 7
        h_1 = 1
        print(days)

        D = days
        try:
##******************Years***********
            q = D / y
            if q == 0:
                print(f"The use Enter Zero at input {D}")
            elif q !=0:
                k = int(q)
                l = k * y
                o = D - l
##*****************Months***************
                R = o / M
            if R == 0:
                print(f"approximately in {D} days we have {k} years with {0} months, {0} weeks, {0} days, and {0} hours")
            elif R !=0:
            
                m = int(R)
                a = m * M
                r_r = o - a
                r = r_r
                
##***************** Weeks ******************
                R_2 = r / w
                if R_2 == 0:
                    print(f"approximately in {D} days we have {k} years with {m} month, {R_2} weeks, {0} days, and {0} hours")  # weeks
                elif R_2 !=0:
                    w_k = int(R_2)
                    a_1 = w_k * w
                    r_1 = r - a_1

#*****************Days******************#
                    d_1 = r_1/1
                    if d_1 ==0:
                      print(f"approximately in {D} days we have {k} years with {m} months, {w_k} weeks, {d_1} days, and {0} hours")  # weeks")
                    else:
                        d = int(d_1)
                        a_h = d * 1
                        r_h = d_1 - a_h                        
##***************Hours ******************
                        h_1 =r_h/24
                        if h_1 >= 0:
                           print(f"approximately in {D} days we have {k} years with {m} months, {w_k} weeks, {d} days, and {h_1} hours")  # weeks")
                           break
                        else:
                           print("Negelect the Hours value in output")
#********** Output Block*********
                if k == 1 and m==1 and w_k==1 and r_1==1 :  
                    print(f"approximately in {D} days we have {k} year and  {m} month and {w_k}week and {r_1} day and {h_1}hours")

                elif k == 1 and m==1 and w_k==1 and r_1!=1 :  
                    print(f"approximately in {D} days we have {k} year and {m} month and {w_k}week and {d} days and {h_1}hours ")

                elif k == 1 and  m==1 and w_k!=1 and r_1==1 : 
                    print(f"approximately in {D} days we have {k} year and {m} month and {w_k}weeks and {r_1} day and {h_1}hours")

                elif k == 1 and m==1 and w_k!=1 and r_1!=1 : 
                    print(f"approximately in {D} days we have {k} year and {m} month and {w_k}weeks and {d} days and {h_1}hours")

                elif k == 1 and m!=1 and w_k==1 and r_1==1 : 
                    print(f"approximately in {D} days we have {k} year and {m} months and {w_k}week and {r_1} day and {h_1}hours")

                elif k == 1 and m!=1 and w_k==1 and r_1!=1: 
                    print(f"approximately in {D} days we have {k} year and {m} months and {w_k}week and {d} days and {h_1}hours")

                elif k == 1 and m!=1 and w_k!=1 and r_1==1 : 
                    print(f"approximately in {D} days we have {k} year and {m} months and {w_k}weeks and {r_1} day and {h_1}hours")

                elif k == 1 and m!=1 and w_k!=1 and r_1!=1 : 
                    print(f"approximately in {D} days we have {k} year and {m} months and {w_k}weeks and {d} days and {h_1}hours")

                elif k != 1 and m==1 and w_k==1 and r_1==1 :  
                    print(f"approximately in {D} days we have {k} years and  {m} month and {w_k}week and {r_1} day and {h_1}hours")

                elif k != 1 and m==1 and w_k==1 and r_1!=1 :  
                    print(f"approximately in {D} days we have {k} years and {m} month and {w_k}week and {d} days and {h_1}hours ")

                elif k != 1 and  m==1 and w_k!=1 and r_1==1 : 
                    print(f"approximately in {D} days we have {k} years and {m} month and {w_k}weeks and {r_1} day and {h_1}hours")

                elif k != 1 and m==1 and w_k!=1 and r_1!=1 : 
                    print(f"approximately in {D} days we have {k} years and {m} month and {w_k}weeks and {d} days and {h_1}hours")

                elif k != 1 and m!=1 and w_k==1 and r_1==1 : 
                    print(f"approximately in {D} days we have {k} years and {m} months and {w_k}week and {r_1} day and {h_1}hours")

                elif k != 1 and m!=1 and w_k==1 and r_1!=1 : 
                    print(f"approximately in {D} days we have {k} years and {m} months and {w_k}week and {d} days and {h_1}hours")

                elif k != 1 and m!=1 and w_k!=1 and r_1==1 : 
                    print(f"approximately in {D} days we have {k} years and {m} months and {w_k}weeks and {r_1} day and {h_1}hours")

                
                elif k == 0 and m==0 and w_k==0 and r_1==0 and h_1==0: 
                    print(f"approximately in {D} days we have {k} years and {m} months and {w_k}weeks and {r_1} days and {h_1}hours")
                
                elif k == 0 and m==0 and w_k==0 and r_1!=0 and h_1!=0: 
                    print(f"approximately in {D} days we have {k} years and {m} months and {w_k}weeks and {d} days and {h_1}hours")
                
                elif k == 0 and m==0 and w_k==0 and r_1!=0 and h_1==0: 
                    print(f"approximately in {D} days we have {k} years and {m} months and {w_k}weeks and {d} days and {h_1}hours")
                
                elif k == 0 and m==0 and w_k==0 and r_1==0 and h_1!=0: 
                    print(f"approximately in {D} days we have {k} years and {m} months and {w_k}weeks and {r_1} days and {h_1}hours")

                else:
                    print("error in out put")

        except:
            print("error")
