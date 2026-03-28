---
layout: page
title:  October 28
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

# Iteration (practice)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Bisc syntax and examples.</span>

## Overview

This page includes solved code-reading exercises on loops.

## Warmu Up Exercise

How many times will each of `A`, `B`, and `C` be printed on the screen if we run the following code?

```python
for i in range(1000):
    print('A')
    print('C')
    for j in range(1000):
        print('B')
        print('C')
```

<details class="jtd-accordion">
  <summary>Solution</summary>
    <ul>
        <li>  <code>A</code> : <code>1,000</code></li>
        <li>  <code>B</code> : <code>1,000,000</code></li>
        <li>  <code>C</code> : <code>1,001,000</code></li>
    </ul>
</details>


## Exercise 1

Choose a meaningful function name for the following code. Choose the name based on your understanding of what the code does overall.

```python
def foo(n):
    for i in range(1, n):
        if i * i == n:
            return i
    return -1
```

<details class="jtd-accordion">
  <summary>Suggested Solution</summary>
    <code>integer_square_root</code>.<br>
    <br>
    To understand what the code does, ask yourself: What does the function return in each of the following cases?
    <ul>
        <li> If <code>n=1</code></li>
        <li> If <code>n=4</code></li>
        <li> If <code>n=16</code></li>
        <li> If <code>n=1000000</code></li>
        <li> If <code>n=3</code></li>
        <li> If <code>n=10</code></li>
        <li> If <code>n=-5</code></li>
    </ul>
    <br><b>Note.</b> The name <code>square_root</code> is not the best name, because the function only returns <b>integer</b> square roots. 
</details>

## Exercise 2

Choose a meaningful function name for the following code. Choose the name based on your understanding of what the code does overall.

```python    
def mystery(n):
    x = 0
    c = abs(n)  # absolute value

    while c > 0:
        x = x + 2
        c = c - 1

    if n >= 0:
        return x
    else:
        return -x
```

<details class="jtd-accordion">
  <summary>Suggested Solution</summary>
    <code>double</code> or <code>multiply_by_2</code>.<br>
    <br>The above function returns the value of <code>`n * 2</code>, but it does the work in a complicated way. It repeats <code>n</code> times adding the number <code>2</code>. It also handles negative numbers.<br>To understand the code better, try tracing it on a piece of paper for the following values of <code>n</code>:
    <ul>
        <li> <code>n=1</code></li>
        <li> <code>n=2</code></li>
        <li> <code>n=4</code></li>
        <li> <code>n=-1</code></li>
        <li> <code>n=-4</code></li>
    </ul>
</details>

## Exercise 3

Choose a meaningful function name for the following code. Choose the name based on your understanding of what the code does overall.

```python    
def mystery():
    result = None
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        if num % 2 == 0:
            result = num
    return result
```

<details class="jtd-accordion">
  <summary>Suggested Solution</summary>
    <code>last_even</code><br>
    <br>The function updates <code>result</code> each time it encounters an even number. When the loop terminates, the function returns whatever is inside <code>result</code>. If no even number was encountered, <code>result</code> would have <code>None</code>. If one or more even numbers were encountered, it would have the last even number stored.
    <br><br>To understand the code better, try tracing it on a piece of paper for the following values:
    <ul>
        <li> <code>0</code></li>
        <li> <code>1, 3, 5, 0</code></li>
        <li> <code>1, 2, 0</code></li>
        <li> <code>2, 3, 4, 5, 0</code></li>
        <li> <code>8, 7, 6, 5, 4, 1, 0</code></li>
    </ul>
</details>

## Exercise 4

Choose a meaningful function name for the following code. Choose the name based on your understanding of what the code does overall.

```python    
def mystery(n):
    temp1 = -1
    temp2 = -1

    for i in range(n):
        value = int(input("Enter a positive number: "))
        if i == 0:
            temp1 = value
        elif value > temp1:
            temp2 = temp1
            temp1 = value
        elif value > temp2:
            temp2 = value
    
    return temp2
```

<details class="jtd-accordion">
  <summary>Suggested Solution</summary>
    <code>second_largest</code>
    <br><br>To understand the code better, try tracing it on a piece of paper for the following values:
    <ul>
        <li> <code>n = 0</code> and no values are given.</li>
        <li> <code>n = 1</code> and value is <code>10</code></li>
        <li> <code>n = 2</code> and the values are: <code>10, 5</code></li>
        <li> <code>n = 6</code> and the values are: <code>10, 5, 4, 3, 2, 1</code></li>
        <li> <code>n = 2</code> and the values are: <code>5, 10</code></li>
        <li> <code>n = 6</code> and the values are: <code>1, 2, 3, 4, 5, 6</code></li>
    </ul>
</details>


> Remember that you can use [PythonTutor](https://pythontutor.com/python-compiler.html#mode=edit) to trace the code step-by-step and see how the variable values change in each iteration.
{: .tip}