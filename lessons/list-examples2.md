---
layout: page
title:  November 11
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

# List Exercises (Part 2)
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

----

## Example 1: Check if Sorted

Define a function `is_sorted(lst)` that takes a list of integers as an argument and returns `True` if the list is sorted in ascending order, and `False` otherwise.

```python
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

# Example usage:
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([5, 3, 4, 1, 2]))
print(is_sorted([10, 20, 20, 30]))
print(is_sorted([]))    # An empty list is considered sorted
print(is_sorted([42]))  # A single-element list is considered sorted
```

> We can solve problem using a single line as follows:
>```python
> def is_sorted(nums):
>     return nums == sorted(nums)
>```
> However, the above solution is less efficient than our solution, since it creates a copy of the list and sorts the elements. For small lists, this is fine. However, for large lists (e.g., containing 1 million elements), this can be a problem. We will discuss program efficiency later in the course.
{: .note }

----

## Example 2: Exam Grades

Write a program that reads midterm exam grades of 10 students, and then reads final exam grades of the same 10 students. The program should then compute and print the total grade for each student.

```python
N = 10
midterm = [0] * N
final   = [0] * N

# Read midterm grades
for i in range(N):
    midterm[i] = int(input("Midterm Exam grade for student " + str(i + 1) + ": "))

# Read final grades
for i in range(N):
    final[i] = int(input("Final Exam grade for student " + str(i + 1) + ": "))

# Compute and print total grades
for i in range(N):
    print("Total grade for student", i + 1, ":", midterm[i] + final[i])
```

----

## Exercise 3 (Code Reading)

```python
def mystery(a):
    N = len(a)
    for i in range(0, N-1, 2):
        a[i+1] = a[i]

    print(a)
```

What does the above code print in each of the following cases?
1. If `a = [1]`
2. If `a = [1, 2]`
3. If `a = [1, 0, 1, 0, 1, 0, ...]` (100 elements)
4. If `a = [0, 1, 2, 3, 4, 5, ...]` (100 elements)

<details class="jtd-accordion">
  <summary>Solution</summary>
    <ol>
        <li> <code>[1]</code></li>
        <li> <code>[1, 1]</code></li>
        <li> <code>[1, 1, 1, 1, 1, 1, ...]</code></li>
        <li> <code>[0, 0, 2, 2, 4, 4, ...]</code></li>
    </ol>
</details>

----

## Exercise 4 (Code Reading)

```python
def mystery(a):
    i = 0
    j = len(a) - 1
    while i < j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1
    
    print(a)
```

Understand what the above code does and then rewrite it using a single line.

<details class="jtd-accordion">
  <summary>Solution</summary>
        The above code reverses the list. This can be done in a single line using slicing:
        <code> print(a[::-1]) </code>
</details>

----

## Exercise 5 (Code Reading)

```python
def mystery(a):
    N = len(a)
    for i in range(N // 2):
        if a[i] in a[N // 2:]:
            return True
    return False
```

What does the above code return in each of the following cases?
1. If `a = [1]`
2. If `a = [1, 1, 1, 1, ...]` (100 elements)
3. If `a = [1, 2, 3, 4, ...]` (100 elements)
4. If `a = [1, 2, 3, ..., 50, 1, 2, 3, ..., 50]` (100 elements)

<details class="jtd-accordion">
  <summary>Solution</summary>
  This code checks if _any_ element in the first half of the list is also in the second half of the list.
    <ol>
        <li> <code>False</code></li>
        <li> <code>True</code></li>
        <li> <code>False</code></li>
        <li> <code>True</code></li>
    </ol>
</details>