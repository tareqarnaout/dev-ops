---
layout: page
title:  October 21
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}
</style>

# Iteration (for-loops)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Bisc syntax and examples.</span>

## Basic Syntax

```python
# Prints 'Hello' 10 times.
for i in range(10):
    print("Hello")
```

---

```python
# Prints 0 1 2 3 4 5 6 7 8 9
# We read this as:
# for every i in the range 0 to 9
for i in range(10):
    print(i)
```

---

```python
# Prints 0 1 2 3 4 5 6 7 8 9 10
for i in range(11):
    print(i)
```

---

```python
# Prints 1 2 3 4 5 6 7 8 9 10
for i in range(1, 11):
    print(i)
```

---

```python
# Prints 5 6 7 8
for i in range(5, 9):
    print(i)
```

---

```python
# Prints 1 3 5 7 9
# The third argument is the skip value
for i in range(1, 11, 2):
    print(i)
```

---

```python
# Does not print anything.
for i in range(10, 1):
    print(i)
```

---

```python
# Prints 10 9 8 7 6 5 4 3 2
for i in range(10, 1, -1):
    print(i)
```

---

```python
# Does not print anything
for i in range(-10, -1, -2):
    print(i)
```

---

```python
# Prints -10 -7 -4
for i in range(-10, -1, 3):
    print(i)
```

---

```python
# QUESTION: Write a program that reads the grades for 5 students 
# and Outputs 'Pass' or 'Fail'.

# SOLUTION.
print("Enter the student grades.")
for i in range(1, 6):
    grade = int(input("Student " + str(i) + ": "))
    if grade >= 50:
        print("Pass")
    else:
        print("Fail")
```
## Sum and Factorial

```python
# QUESTION: Write a program that reads a positive integer n 
# and prints the sum of the integers from 0 to n.
# For example, if the integer is 5, the output should be
# the sum of 0 + 1 + 2 + 3 + 4 + 5.

# SOLUTION.
n = int(input("Enter a number: "))
result = 0
for i in range(n + 1):
    result = result + i # add i to the old result

print('Sum = ', result)
```

---

```python
# QUESTION: Write a program that reads a positive integer n 
# and prints its factorial.
# For example, if the integer is 5, the output should be
# the result of 1 x 2 x 3 x 4 x 5.

# SOLUTION.
n = int(input("Enter a number: "))

result = 1
for i in range(1, n + 1):
    result = result * i

print('Factorial = ', result)
```

## Maximum

```python
# QUESTION: Write a program that reads 10 positive integers
# and prints the maximum.

# SOLUTION.
print("Enter 10 numbers: ")
current_max = None
for i in range(10):
    num = int(input())

    if current_max == None or num > current_max:
        current_max = num

print("Max = ", current_max)
```

## Shapes

```python
# QUESTION: Write a program that reads a positive integer n
# and prints a square of '*' of size n x n.
# If the user enters a negative number, output an error message.
#
# Example output if n = 5:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# SOLUTION.
n = int(input("Enter the size of the square: "))
if n <= 0:
    print("ERROR: INVALID SIZE")
else:
    for i in range(1, n+1):
        print('*' * n)
```

---

```python
# QUESTION. What is the output of the following program
# in each of the following cases:
# If n = 0
# If n = 1
# If n = 2
# If n = 5

n = int(input("Enter the size of the square: "))
for i in range(n + 1):
    print('*' * i)

# ANSWER.
# If n = 0:     No output
#
# If n = 1:     *
#
# If n = 2:     *
#               **
#
# If n = 5:     *
#               **
#               ***
#               ****
#               *****
```

---

```python
# QUESTION: Write a program that reads a positive integer n
# and prints a triangle of '*' of size n as shown below.
#
# Example output if n = 5:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# SOLUTION.
n = int(input("Enter the size of the triangle: "))
for i in range(n + 1):
    print(' ' * (n-i) + '*' * i)
    # print n-i spaces followed by i stars

#               5 spaces 0 stars
#         *     4 spaces 1 stars
#       * *     3 spaces 2 stars
#     * * *     2 spaces 3 stars
#   * * * *     1 space  4 stars
# * * * * *     0 spaces 5 stars
```