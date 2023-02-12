# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment=1000
month=1
extra_payment_start_month=1
extra_payment_end_month=12

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal* (1+rate/12) - payment - extra_payment
        total_paid = total_paid + extra_payment + payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(month, total_paid,principal)
    month+=1
if principal<0:
   due=-principal
print('Total paid', round(total_paid,2))
print('Month', month-1)
print('Due', due) 
