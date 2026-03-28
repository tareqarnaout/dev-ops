# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Write a program that reads two integers, x and y, and       # 
# an operator: +, -, *, or /                                  #
# The program should print out the result of the operation    #
# or output an error message if the oepration is not valid.   #
#                                                             #
# --------------------- EXAMPLE RUN ------------------------- #
# Enter x: 1                                                  #
# Enter y: 3                                                  #
# Enter opeartion: +                                          #
# Result = 4                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

x = int(input("Enter x: "))
y = int(input("Enter y: "))
op = input("Enter the operator: ")

if op == '+':
    print("Result = ", x + y)
elif op == '-':
    print("Result = ", x - y)
elif op == '*':
    print("Result = ", x * y)
elif op == '/':
    if y == 0:
        print("ERROR: CAN'T DIVID BY ZERO!")
    else:
        print("Result = ", x / y)
else:
    print("ERROR: INVALID OPERATION!")