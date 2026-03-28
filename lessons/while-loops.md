---
layout: page
title:  October 23
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

# Iteration (while-loops)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Bisc syntax and examples.</span>

## Overview

For loops are suitable for situations where we know how many times we want to repeat a certian piece of code. However, if the number of iterations is unknown, we can use a `while` loop. This loop allows repeating a block of code **as long as** a certain condition is met.

## Basic Syntax

### Example 1. 
The following code repeats until the user enters anything other than "1234".

```python
psw = input("Enter a password: ")
while psw == '1234':
    print("This is not a good password!")
    psw = input("Enter a password: ")

print("Thank you!")
```

How can we change the code so that it repeats until the user enters a password of length greater than `8`?

```python
# Repeats until the user enters a password more than 8 characters long.
psw = input("Enter a password: ")
while len(psw) < 8:
    print("This is a short password!")
    psw = input("Enter a password: ")

print('Thank you!')
```

### Example 2.
The following code counts down from 5 to 1 and then prints `Booom!`

```python
# Counts down from 5 to 1.
c = 5
while c >= 1:
    print(c)
    c = c - 1
print("Booom!")
```

This `while` loop is equivalent to the following `for` loop.

```python
# Counts down from 5 to 1.
for c in range(5, 0, -1):
    print(c)

print("Booom!")
```

> Every `for` loop can be written as a `while` loop. However, it is usually clearer and shorter if you use a `for` loop for situations where the number of iterations is known before-hand (as in the count-down example)
{: .tip}

### Exercise 1

Explain in your own words what the following code does, then run it to check if your understanding is correct or not.

```python
c = 0
answer = input("Do you like Python? (enter y or n): ")
while answer != 'y':
    print("Are you " + 'really ' * c + "sure you don't like Python?")
    print("I will ask again:")
    answer = input("Do you like Python? (enter y or n): ")
    c = c + 1

print("Thank you! I knew you loved Python!")
```

### Exercise 2

Catch and fix the bug in the following program. It is supposed to skip 2's while counting down from `n` to `1`. you can run the program with multiple inputs to find the error.

```python
n = int(input("Enter a number: "))
while n != 0:
    print(n)
    n = n - 2
print("Done!")
```

<details class="jtd-accordion">
  <summary>Solution</summary>
    This is a classic example of an <b>infinite loop</b>. The program will run for ever if the user enters an <i>odd</i> number or a <i>negative</i> number, because <code>n</code> will never be equal to 0. To fix this issue, change the loop condition to be <code>while n > 0</code>.
</details>

## Breaking Out of a Loop

The following is another way to write the password example.

```python
while True:
    psw = input("Enter a password: ")
    if len(psw) > 8:
        break
    print("Your password is too short!")

print("Thank you!")
```

There are two new things going on in the above loop:
- The `while True` statement means that we want the loop to repeat for ever.
- The `break` statement stops the loop. If password length is greater than `8`, the `break` statement will exit the loop, which means that the following `print` statement will **not** be executed.

### Exercise 3

Write a program that keeps reading integers from the user until the user enters a negative integer. The program should then print the average of the entered numbers.

**Note.** To compute the average, we need to know the sum of the entered integers, and how many integers the user entered.

{% include expandable-code.html
title="Solution"
id="avg-while"
language="python"
file='code/avg-while.py'
%}

### Exercise 4

Rewrite the 'Are you really really sure' example above using `while True` and `break`.

{% include expandable-code.html
title="Solution"
id="really-while"
language="python"
file='code/really-while.py'
%}

## Skipping an Iteration

To skip an iteration, you can use `continue`. This statement stops the current iteration and goes immediately to the loop condition (skipping the lines below `continue`).

What does the following program print?

```python
battery = 100
while battery > 0:
    print("Flying drone. Battery = ", battery, "%")
    battery = battery - 10

    if battery > 20:
        continue

    print("WARNING: Low Battery!!")
```
<details class="jtd-accordion">
  <summary>Solution</summary>
    <pre>Flying drone. Battery =  100 %
Flying drone. Battery =  90 %
Flying drone. Battery =  80 %
Flying drone. Battery =  70 %
Flying drone. Battery =  60 %
Flying drone. Battery =  50 %
Flying drone. Battery =  40 %
Flying drone. Battery =  30 %
WARNING: Low Battery!!
Flying drone. Battery =  20 %
WARNING: Low Battery!!
Flying drone. Battery =  10 %
WARNING: Low Battery!!</pre>
</details>