x = int(input())
y = int(input())
z = int(input())

if x >= y:
    if x >= z:
        print(x)
    else:
        print(z)
elif y >= z:
    print(y)
else:
    print(z)