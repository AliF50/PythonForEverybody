hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)

if(h>40):
    pay = 40*rate + 1.5*(h-40)*rate
else:
    pay = rate*h-40
print(pay)