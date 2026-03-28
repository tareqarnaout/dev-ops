---
layout: page
title:  October 21
nav_exclude: true
author: Ibrahim Albluwi
---

# **8.** Iteration (for-loops)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 21, 2025</span>

## Lecture Goals

This lecture is an introduction to `for` loops (without nesting). The main goal is to introduce the syntax and see examples of repetition and iteration patterns like accumlation (e.g., sum, factorial, etc.) and finding the maximum.

Note that this is not consistent with the book chapter. The book chapter starts with while loops.

## Suggested Teaching Method

This lecture is example-based. Therefore, the expectation is that you'll alternate between showing students code and asking them for the output, explaining a problem and asking students to help you live-code the solution, and simply writing code and explaining it.

Below is a list of the minimum examples students need to see. 

> The first set of examples are short. To speed up going through these examples, I'll be using [IPython](https://ipython.org/install.html), which you can install and run through the terminal in VSCode (we don't have to explain to the students what IPython is). The good thing about IPython is that it has colored syntax highlighting and allows repeating mutli-line instructions using the up-arrow key.
{: .note}

## Basic Syntax

```python
# Prints 'Hello' 10 times.
for i in range(10):
    print("Hello")
```

---

```python
# Prints 0 1 2 3 4 5 6 7 8 9
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
for i in range(1, 11, 2):
    print(i)
```

---

```python
# Does not print anything
for i in range(10, 1):
    print(i)
```

---

```python
# 10 9 8 7 6 5 4 3 2
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
# -10 -7 -4
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
    result = result + i

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
result = None
for i in range(10):
    num = int(input())
    if result == None or num > result:
        result = num
print("Max = ", result)
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
    for i in range(1, n):
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
```