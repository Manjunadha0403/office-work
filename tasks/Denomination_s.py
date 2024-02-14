# Denomination for currency
# We take only Indian currency for this operation
m = money = int(input("Enter amount: "))

# Calculate number of notes/coins for each denomination
y_500 = m // 500
r = m % 500
v_500 = y_500*500

y_200 = r//200
r = r % 200
v_200 = y_200*200

y_100 = r // 100
r = r % 100
v_100 = y_100*100

y_50 = r // 50
r = r % 50
v_50 = y_50*50

y_20 = r // 20
r = r % 20
v_20 = y_20 * 20

y_10 = r // 10
r = r % 10
v_10 = y_10*10

y_5 = r // 5
r = r % 5
v_5 = y_5*5

y_2 = r // 2
r = r % 2
v_2 = y_2 * 2

y_1 = r // 1
r = r % 1
v_1 = y_1 * 1
# Output the results
print(f"""In {money} we have:
      courency       No.N/C            value       
          {500}/-            {y_500}               {v_500}
          {200}/-            {y_200}               {v_200}
          {100}/-            {y_100}               {v_100}
          {50}/-             {y_50}                {v_50}
          {20}/-             {y_20}                {v_20}
          {10}/-             {y_10}                {v_10}
          {5}/-              {y_5}                 {v_5}
          {2}/-              {y_2}                 {v_2}
          {1}/-              {y_1}                 {v_1}

                        Total =             {money}/-""")