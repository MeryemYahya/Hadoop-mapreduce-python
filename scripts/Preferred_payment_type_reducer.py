#!/usr/bin/env python3

import sys

dictionary ={"1": "Credit card" , "2": "Cash" , "3": "No charge" , "4": "Dispute" , "5": "Unknown" , "6": "Voided trip"}
total ={}
current_payement = None
current_count = 0
payment = None

for line in sys.stdin:
   
    line = line.strip()
    line = line.split(' ', 1)
    count=line[-1]
    payment=line[0]
    try:
        count = int(count)
    except ValueError:
      
        continue

    if current_payement == payment:
        current_count += count
    else:
        if current_payement:
            print(dictionary[current_payement], current_count)
            total[dictionary[current_payement]]= current_count
        current_count = count
        current_payement = payment

if current_payement == payment:
    print(dictionary[current_payement], current_count)
    total[dictionary[current_payement]]= current_count

preferredpayment = max(total , key=total.get)

print("Preferred payment type :", preferredpayment )




