# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0


while principal > 0:

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('total_paid', total_paid)

# Exercise 1.8: Extra payments
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

while principal > 0:

    if month <= 12:
        payment = 3684.11
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        
    else:
        payment = 2684.11
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    month = month + 1

print('total_paid', total_paid)
print('month', month)

### Exercise 1.9: Making an Extra Payment Calculator
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        
    else:
        payment = 2684.11
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    month = month + 1

print('total_paid', total_paid)
print('month', month)

### Exercise 1.10: Making a table
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1

    if principal < payment:
        payment = principal*(1+rate/12)
        principal = principal*(1+rate/12) - payment
        total_paid = total_paid + payment

    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

     
    print(month, round(total_paid,2), round(principal,2))
    

print('total_paid', total_paid)
print('month', month)
