sum = 0     # for keeping track of the sum
c = 0       # for keeping track of the count
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break

    sum = sum + num
    c = c + 1

print("Average = ", sum / c)