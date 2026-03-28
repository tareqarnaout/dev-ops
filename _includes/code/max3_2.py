x = int(input())
y = int(input())
z = int(input())

m = x       # assume x is the maximum

if y > m:   # if y is greater than the current maximum
    m = y   # make y the new maximum

if z > m:   # if z is greater than the current maximum
    m = z   # make z the new maximum

print(m)    # print the maximum