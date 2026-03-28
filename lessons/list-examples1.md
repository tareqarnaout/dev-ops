---
layout: page
title:  November 9
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

# List Exercises (Part 1)
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

----
## Exercise 1: Reverse The Input 

Write a program that reads a list of `20` integers from the user, then prints them in reverse order.

```python
N = 20
nums = [0] * N
for i in range(N):
    num = int(input("Enter an integer: "))
    nums[i] = num

print("The numbers in reverse order are:")
print(nums[::-1])
```

----

## Example 2: Sort the Input

Write a program that keeps reading integers from the user until the user enters `-1`. Then, the program prints the integers sorted in ascending order (excluding the `-1`).

```python
nums = []
while True:
    num = int(input("Enter an integer (-1 to stop): "))
    if num == -1:
        break
    nums.append(num)

print("The numbers in sorted order are:")
print(sorted(nums))
```

----

## Example 3: Random Unique Numbers

Write a program that generates a list of `100` _unique_ random integers between `0` and `1000`, then prints the list sorted in ascending order.

To solve this problem, we will begin with an empty list, and keep generating random integers and adding them to the list until the list has `100` unique integers. When generating a random integer, we will check if it is already in the list; if it is, we will not add it again.

```python
import random

nums = []
while len(nums) < 100:
    num = random.randint(0, 1000)
    if num not in nums:
        nums.append(num)

print("The unique random numbers are:")
print(sorted(nums))
```

----

## Example 4: Is Equivalent

Define a function `is_equivalent(a, b)` that takes two lists of integers as arguments and returns `True` if both lists contain the same elements (regardless of order and frequency), and `False` otherwise.

**Examples.**

```python
# should print equivalent
a = [1, 2, 3]
b = [1, 2, 1, 2, 2, 2, 1, 3, 3]
print(is_equivalent(a, b))

# should print not equivalent because of 3 and 4
a = [1, 2, 4]
b = [1, 2, 1, 2, 2, 2, 1, 3, 3]
print(is_equivalent(a, b))
```

**Solution.**
```python
def is_equivalent(a, b):   
    # check that every element in a is in b 
    for element in a:
        if element not in b:
            return False

    # check that every element in b is in a
    for element in b:
        if element not in a:
            return False

    return True
```

----
## Exercise 5 (Code Reading)

Read and understand the following function, then suggest suitable name for it.

```python
def mystery(a, b):
    N1 = len(a)
    N2 = len(b)

    if N1 > N2:
        return False
    
    for i in range(N2):
        if a == b[i: i+N1]:
            return True
    
    return False
```

<details class="jtd-accordion">
  <summary>Solution</summary>
    The function checks if list <code>a</code> is a sublist of list <code>b</code>. A suitable name would be <code>is_sublist(a, b)</code> or <code>contains_sublist(a, b)</code>.
</details>