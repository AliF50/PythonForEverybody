largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        if smallest is None:
            smallest = int(num)
            largest = int(num)
            continue
        if int(num) < smallest:
            smallest = int(num)
        if int(num) > largest:
            largest = int(num)
    except:
        print('Invalid input')

print 'Maximum is',largest
print 'Minimum is',smallest