---
layout: page
title:  October 26
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

# Iteration (nested loops)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Bisc syntax and examples.</span>

## Overview

This page includes examples requiring nested iteration (a loop repeated inside a loop).

## Example 1.

**QUESTION.** Define and implement a function named `mult_table` that receives two numbers `n1` and `n2` as arguments and prints the multiplication table (`1` to `12`) for all the numbers between `n1` and `n2` inclusive. 

**SOLUTION.** To solve this problem, we need first to be able to print the multiplicatoin table for a single number. Once that is done, we can use a loop to repeat this code for all the numbers in the given range.

```python
n = 5
for i in range(1, 13):
    print(n, " x ", i, " = ", n * i)
```

This will print the multiplication table for the number `n` (which is set to `5` in the above code). The result will look like this:

```
5  x  1  =  5
5  x  2  =  10
5  x  3  =  15
5  x  4  =  20
5  x  5  =  25
5  x  6  =  30
5  x  7  =  35
5  x  8  =  40
5  x  9  =  45
5  x  10  =  50
5  x  11  =  55
5  x  12  =  60 
```

Now, we need to vary `n` based on the given range. To achieve this, we can place the above code inside a loop that iterates between `n1` and `n2+1`. The following is the full answer to the question.

```python
def mult_table(n1, n2):
    for n in range(n1, n2+1):
        print(" --- TABLE FOR: ", n, "--- ")
        for i in range(1, 13):
            print(n, " x ", i, " = ", n * i)
```

The outer loop repeats in each iteration two things: (1) printing a header, and (2) printing one full multiplication table. The output for calling `mult_table(1, 3)` is as follows.

{% include expandable-code.html
title="Output"
id="output"
language="python"
file='code/mult-table-output.txt'
%}

We could have achieved the same thing by defining a function for printing a single multiplication table and calling it inside a loop, as shown below.

```python
def one_table(n):
    print(" --- TABLE FOR: ", n, "--- ")
    for i in range(1, 13):
        print(n, " x ", i, " = ", n * i)

def mult_table(n1, n2):
    for n in range(n1, n2+1):
        one_table(n)
```

## Example 2.

**QUESTION.** Define and implement a function named `print_primes` that receives two numbers `n1` and `n2` as arguments and prints all the _prime_ numbers in the given range. A prime number is a number that is only divisible by itself and by 1.

**SOLUTION.** To solve this problem, we need first to be able to check if a given number is prime or not. If we can do that, we can use a loop to check all the numbers between `n1` and `n2`.

To check if a given number `n` is prime, we can check all the numbers between `2` and `n-1` (inclusive) to see if any of them divides `n`. Here is a piece of code that achieves that.

```python
prime = True            # assume n is prime

for i in range(2, n):   # If any number i in the range 
    if n % i == 0:      # (2, n] divides n, then our
        prime = False   # assumption that n is prime is false! 
        break           # no need to continue 

if prime:               # check if our assumption changed.
    print(n)            # Same as: if prime == True:
```

{: .important-title}
> NOTE
>
> The above code uses a **flag** named `prime`:
> - The flag begins raised up (`True`).
> - The loop checks if `n` has divisors. If a divisor is found, the flag is brought down (changes to `False`). 
> - After the loop, we check if the flag is still up (`True`) or if it is down (`False`). If it is still up, no divisors were found, and our assumption that `n` is prime is still true.

Another option is to use a counter instead of a flag. The counter begins at `0` and is incremented each time a divisor is found. After the loop, if the counter is still `0`, then `n` is prime. Here is the code using a counter.

```python
count = 0               # begin with no divisors found

for i in range(2, n):   # check all numbers between 2 and n-1
    if n % i == 0:      # if i divides n,
        count += 1      # increment the counter

if count == 0:          # if no divisors were found,
    print(n)            # then n is prime
```

Now, we are ready to place this code inside a loop that checks every value between `n1` and `n2` if it is prime or not. Here is a full answer for the question:

```python
def print_primes(n1, n2):
    for n in range(n1, n2+1):
        prime = True            
        for i in range(2, n):
            if n % i == 0:
                prime = False    
        
        if prime:
            print(n)
```
Calling the above function using the range 3-20 prints the numbers `3 5 7 11 13 17 19` each on a separate line.

We could have simplified the code by first defining a function that checks if a given number is prime, and then called the function inside the loop.

```python
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:      # If a divisor is found,
            return False    # stop the loop and the function
                            # and return False
    return True
    # This is outside the loop.
    # If we reach here, this means that none of the numbers
    # between 2 and n-1 divided n, so the number is prime

def print_primes(n1, n2):
    for n in range(n1, n2+1):
        if is_prime(n):    # same as: if is_prime(n) == True:
            print(n)
```

## Example 3.

What is the output of the following program?

```python
for i in range(1, 6):
    line = ''
    for j in range(1, 6):
        line += "(" + str(i) + "," + str(j) + ")"
    print(line)
```

<details class="jtd-accordion">
  <summary>Solution</summary>
<pre>
(1,1)(1,2)(1,3)(1,4)(1,5)
(2,1)(2,2)(2,3)(2,4)(2,5)
(3,1)(3,2)(3,3)(3,4)(3,5)
(4,1)(4,2)(4,3)(4,4)(4,5)
(5,1)(5,2)(5,3)(5,4)(5,5)
</pre>
</details>

## Example 4.

What is the output of the following program?

```python
for i in range(4):
    line = ''
    for j in range(4):
        if i == j:
            line += "X"
        else:
            line += '-'
    print(line)
```

<details class="jtd-accordion">
  <summary>Solution</summary>
<pre>
X---
-X--
--X-
---X
</pre>
</details>