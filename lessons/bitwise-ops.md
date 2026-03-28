---
layout: page
title:  Bitwise Operations
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}

h3 {
    font-weight: 500;           /* bold weight */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #9c0101ff;             /* optional: different color */
}

.img-soft {
    width: 75%;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);  
}
</style>


# Bitwise Operations
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

We can sum, subtract, multiply, and divide numbers, regardless of their representation (binary, decimal, hexadecimal, etc.). However, since binary numbers are made up of bits (0s and 1s), representing states (on/off, true/false), there are other operations we can perform on them called **bitwise operations**.

Bitwise operations manipulate individual bits within a binary number. These translate directly to low-level operations in computer hardware, making them efficient for various applications, including graphics processing, cryptography, and network programming.

Here is a table summarizing the bitwise operations we will cover, and how they look like in Python:

```
|=============|========|========================|
| Operation   | Symbol | Example Usage (Python) |
|=============|========|========================|
| AND         |   &    |         a & b          |
| OR          |   |    |         a | b          |
| XOR         |   ^    |         a ^ b          |
| NOT         |   ~    |         ~a             |
| Left Shift  |   <<   |         a << n         |
| Right Shift |   >>   |         a >> n         |
|=============|========|========================|
```

We will explain each operation in detail below.

## AND

**AND**ing two binary numbers results in a new binary number, where the bit is `1` only if the bits of both numbers are `1`. This is equivalent to *multiplying* the bits, or taking the intersection of the bits.

<img src="https://files.realpython.com/media/and.ef7704d02d6f.gif" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

Here is the **truth table** for the AND operation:

<img src="/11102-f25/lessons/images/and.png" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

**Example**

```
    1 1 0 1 0 1 1
AND 1 0 1 1 0 0 1
    -------------
    1 0 0 1 0 0 1
```

Here is a Python example of the AND operation:

```python
>>> a = 0b1101011
>>> b = 0b1011001
>>> bin(a & b)
'0b1001001'
```

Note that in Python the `0b` prefix means that the number is in binary. Note also that you can AND numbers in any base, but the operation is performed on their binary representations. For example:

```python
>>> 1 & 3     
1             # Explanation:  01 & 11 = 01

>>> 5 & 6     
4             # Explanation:  101 & 110 = 100

>>> 4 & 3     
0             # Explanation:  100 & 011 = 000
```

## OR

**OR**ing two binary numbers results in a new binary number, where the bit is `1` if at least one of the bits of the two numbers is `1`. This is equivalent to *adding* the bits, or taking the union of the bits.

<img src="https://files.realpython.com/media/or.7f09664e2d15.gif" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

Here is the **truth table** for the OR operation:

<img src="/11102-f25/lessons/images/or.png" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

**Example**

```
    1 1 0 1 0 1 1
 OR 1 0 1 1 0 0 1
    -------------
    1 1 1 1 0 1 1
```

Here are Python examples of the OR operation:

```python
>>> a = 0b1101011      
>>> b = 0b1011001      
>>> bin(a | b)
'0b1111011'

>>> 1 | 3     
3             # Explanation:  01 | 11 = 11

>>> 5 | 6     
7             # Explanation:  101 | 110 = 111

>>> 4 | 3     
7             # Explanation:  100 | 011 = 111
```

## XOR

**XOR**ing two binary numbers results in a new binary number, where the bit is `1` if the bits of the two numbers are different (i.e., one is `1` and the other is `0`). If both bits are the same (both `0` or both `1`), the result is `0`. 

This operation is also known as **exclusive or** because it excludes the case where both bits are `1`. This operation is also sometimes referred to as the **difference operation**, as it highlights the bits that differ between the two numbers.

<img src="https://files.realpython.com/media/xor.8c17776dd501.gif" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

Here is the **truth table** for the XOR operation:

<img src="/11102-f25/lessons/images/xor.png" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

**Example**

```
    1 1 0 1 0 1 1
XOR 1 0 1 1 0 0 1
    -------------
    0 1 1 0 0 1 0
```

Here are Python examples of the XOR operation:

```python
>>> a = 0b1101011      
>>> b = 0b1011001      
>>> bin(a ^ b)
'0b0110010'  

>>> 1 ^ 3
2             # Explanation:  01 ^ 11 = 10
>>> 5 ^ 6
3             # Explanation:  101 ^ 110 = 011
>>> 4 ^ 3
7             # Explanation:  100 ^ 011 = 111
```

## NOT

**NOT** is a unary operation that inverts the bits of a binary number. It changes `0`s to `1`s and `1`s to `0`s. This operation is also known as **bitwise negation** or **complement**.

**Example**

```
   NOT 1101011
       -------
       0010100
```

In Python, the NOT operation is performed using the `~` operator. However, the result might be surprising. Here is an example:

```python
>>> ~1
-2
```

Let's walk through why this happens. 

- The binary representation of `1` is `0000...0001` (infinite leading zeros).
- Applying the NOT operation flips all bits, resulting in `1111...1110`.
- In two's complement representation (which Python uses for negative numbers), `1111...1110` represents `-2`.

In general, for any integer `x`, the result of `~x` in Python is `-(x + 1)`.

```python
>>> ~5
-6

>>> ~0
-1

>>> ~-3
2
```

## Left Shift

**Left Shift** shifts the bits of a binary number to the left by a specified number of positions. Each left shift effectively multiplies the number by `2` for each position shifted. New bits that enter from the right are filled with `0`s.

<img src="https://files.realpython.com/media/lshift.e06f1509d89f.gif" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

**Example**

```
   0011010 << 2
   -------
   1101000
```

In Python, the left shift operation is performed using the `<<` operator:

```python
a = 0b0011010      # Binary for 26
print(bin(a << 2)) # Output: 0b1101000 (Binary for 104)

print(3  << 1)  # Output:  6 (Binary: 11   << 1 = 110)
print(6  << 1)  # Output: 12 (Binary: 110  << 1 = 1100)
print(12 << 1)  # Output: 24 (Binary: 1100 << 1 = 11000)
print(3  << 3)  # Output: 24 (Binary: 11   << 3 = 11000)
print(-1 << 1)  # Output: -2 (Binary: ...11111111 << 1 = ...11111110)
print(-2 << 2)  # Output: -8 (Binary: ...11111110 << 2 = ...11111000)
```

## Right Shift

**Right Shift** shifts the bits of a binary number to the right by a specified number of positions. Each right shift effectively divides the number by `2` for each position shifted. 

New bits that enter from the left are filled based on the sign bit (for signed integers). For positive numbers, `0`s are filled in, while for negative numbers, `1`s are filled in (this is known as arithmetic right shift).

<img src="https://files.realpython.com/media/rshift.9d585c1c838e.gif" class="img-soft" style="display:block; margin: 20px auto; width:50%;" />

**Example**

```
Assuming positive number:
   1101000 >> 2
   -------
   0011010

Assuming negative number:
    11111100 >> 2
    --------
    11111111
```

Note that the right-most bit is discarded with each shift.

In Python, the right shift operation is performed using the `>>` operator:

```python
a = 0b1101000      # Binary for 104
print(bin(a >> 2)) # Output: 0b0011010 (Binary for 26)

print(24 >> 1)  # Output: 12 (Binary: 11000 >> 1 = 1100)
print(12 >> 1)  # Output: 6  (Binary: 1100  >> 1 = 110)
print(6  >> 1)  # Output: 3  (Binary: 110   >> 1 = 11)
print(24 >> 3)  # Output: 3  (Binary: 11000 >> 3 = 11)

print(-8 >> 1)  # Output: -4 (Binary: ...11111000 >> 1 = ...11111100)
print(-4 >> 1)  # Output: -2 (Binary: ...11111100 >> 1 = ...11111110)
print(-2 >> 1)  # Output: -1 (Binary: ...11111110 >> 1 = ...11111111)
```

## Fun With Bitwise Operations

### Exercise 1

What does the following function do?

```python
def mystery(x):
    return x & 1
```

**Answer:** It returns the least significant bit of `x`. 

### Exercise 2. 

Pick a meaningful name for the following function:

```python
def mystery(x):
    return (x & 1) == 0
```

**Answer:** The function checks if `x` is even. A number is even if its least significant bit is `0`.

### Exercise 3.

What does the following function do?

```python
def mystery(x):
    return x | 1
```

**Answer:** It sets the least significant bit of `x` to `1`, effectively making the number odd.

