"""Denomination for courency"""
# We take only indian courency for this operation
money = float(input("Enter ammount: "))
m = int(money)
p = money - m
# Indian courency
note_500 = 500
note_100 = 100
note_50 = 50
note_20 = 20
note_10 = 10
coins_5 = 5
coins_2 = 2
coins_1 = 1
#***********note_500*********
x = m /note_500
if x==0:
   print(f"in {m}we have {x} of {note_500}/- Notes and {p} paisa")
else:
   y_500 = int(x)
   z_500 = y_500 * note_500
   r_500 = m -z_500
   


#***********note_100*********
   a_100 = r_500 /note_100
   if a_100==0:
      print(f"in {m}we have {y_500} of {note_500}/- Notes and {a_100} of {note_100}/- and {p} paisa")
   else:
      y_100 = int(a_100)
      z_100 = y_100 * note_100
      r_100 = r_500 -z_100
      

#***********note_50**********
      a_50 = r_100 /note_50
      if a_50==0:
         print(f"in {m}we have {y_500} of {note_500}/- Notes and {y_100} of {note_100}/- and {a_50} of {note_50}/- Notes and {p} paisa")
      else:
         y_50 = int(a_50)
         z_50 = y_50 * note_50
         r_50 = r_100 -z_50
         

#***********note_20**********
         a_20 = r_50 /note_20
         if a_20==0:
            print(f"in {m}we have {y_500} of {note_500}/- Notes and {y_100} of {note_100}/- and  {y_50} of{note_50}/- notes and {note_20}/- Notes and {p} paisa")
         else:
            y_20 = int(a_20)
            z_20 = y_20 * note_20
            r_20 = r_50 -z_20
            

#***********note_10**********
            a_10 = r_20/note_10
            if a_10==0:
               print(f"in {m}we have {y_500} of {note_500}/- Notes and {y_100} of {note_100}/- and  {y_50} of{note_50}/- notes and {y_20} of{note_20}/- Notes and{a_10}/- {note_10}/- Notes and {p} paisa")
            else:
               y_10 = int(a_10)
               z_10 = y_10 * note_10
               r_10 = r_20 -z_10
               
#*************coin_5************
               a_5 = r_10/coins_5
               if a_5 ==0:
                  print(f"in {m} we have {y_500} of {note_500}/- Notes and {y_100} of {note_100}/- and  {y_50} of{note_50}/- notes and {y_20} of {note_20}/- Notes and {y_10} of {note_10}/- notes and {a_5} of {coins_5}/- coins and {p} paisa")
               else:
                  y_5= int(a_5)
                  z_5= y_5*coins_5
                  r_5= r_10-z_5 
 #**********coin_2************   
                  a_2 = r_5/coins_2
                  
                  if a_2 == 0:
                     print(f"In {m} we have {y_500} of {note_500}/- Notes and {y_100} of {note_100}/- and  {y_50} of{note_50}/- notes and {y_20} of {note_20}/- Notes and {y_10} of {note_10}/- notes and  {y_5}of {coins_5}/- coins and {a_2} of {coins_2}/- coins and {p} paisa")
                  else:
                     y_2 = int(a_2)
                     z_2 = y_2 * coins_2
                     r_2 = r_5-z_2
#*********coin_1************
                     a_1 = r_2/coins_1
                     z_1 = a_1* coins_1
                     if a_1 ==1:
                        print(f"In {m} we have {y_500} of {note_500}/- Notes and {y_100} of {note_100}/- and  {y_50} of{note_50}/- notes and {y_20} of {note_20}/- Notes and {y_10} of {note_10}/- notes and  {y_5}of {coins_5}/- coins and {a_2} of {coins_2}/- coins and {p} paisa")
                  
                        print(f"""The total Denomination for given money is:
                     courency     Notes/coins         value
                     {note_500}/-               {y_500}           {z_500}
                     {note_100}/-               {y_100}           {z_100}
                     {note_50}/-                {y_50}            {z_50}
                     {note_20}/-                {y_20}            {z_20}
                     {note_10}/-                {y_10}            {z_10}
                     {coins_5}/-                 {y_5}             {z_5}
                     {coins_2}/-                 {y_2}             {z_2}
                     {coins_1}/-                 {a_1}           {z_1}

                     {p}                paisa

                     Total              {money}""")
