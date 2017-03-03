def computepay(h,r):
    if(h > 40):
        return r*40 + 1.5*(h - 40)*r
    else:
        return r*h

hrs = raw_input("Enter Hours:")
hrs = float(hrs)
rate = raw_input("Enter rate:")
rate = float(rate)
p = computepay(hrs,rate)
print p