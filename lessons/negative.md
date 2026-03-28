---
layout: page
title:  Dec 11
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


# Data Representation (Part 2)
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Representing Negative Numbers

There are multiple ways to represent negative numbers in binary. The most straightforward way is to use dedicate the most significant bit (MSB) as a sign bit.

**Example:** If we are using a byte (8 bits) to store the number **-5**, we can represent it as `10000101`:

- The MSB (leftmost bit) is `1`, indicating that the number is negative.
- The remaining bits `0000101` represent the absolute value of the number, which is `5`.

This method is called **sign-magnitude representation**. Here is an example table for 3-bit sign-magnitude representation:

```
| Binary | Sign  | Magnitude | Value |
|--------|-------|-----------|-------|
| 000    |   0   |    00     |  +0   |
| 001    |   0   |    01     |  +1   |
| 010    |   0   |    10     |  +2   |
| 011    |   0   |    11     |  +3   |
|--------|-------|-----------|-------|
| 100    |   1   |    00     |  -0   |
| 101    |   1   |    01     |  -1   |
| 110    |   1   |    10     |  -2   |
| 111    |   1   |    11     |  -3   |
```

As you can see, this representation has two representations for zero: `000` (+0) and `100` (-0). This is not ideal!

Another major issue with sign-magnitude representation is that arithmetic operations (like addition and subtraction) do not work as expected. Here is an exampple for adding `+5` and `-2` using 4-bit sign-magnitude representation:

```
  +5 in sign-magnitude:  0101
  -2 in sign-magnitude:  1010 +
                         ----
                         1111  (which is -7 in sign-magnitude)
```

The correct answer should be `+3`, but we got `-7` instead! You can try other examples and see that addition and subtraction do not work correctly in sign-magnitude representation.

## Two's Complement Representation

### Overview

A more common method is called **two's complement**. In this method, the most significant bit (MSB) still indicates the sign of the number, and positive numbers are represented as usual. However, the way negative numbers are represented is different.

Here is a 4-bit two's complement representation table:

```
| Binary | Sign Bit | Remaining Bits | Value |
|--------|----------|----------------|-------|
|  0000  |    0     |      000       |  +0   |
|  0001  |    0     |      001       |  +1   |
|  0010  |    0     |      010       |  +2   |
|  0011  |    0     |      011       |  +3   |
|  0100  |    0     |      100       |  +4   |
|  0101  |    0     |      101       |  +5   |
|  0110  |    0     |      110       |  +6   |
|  0111  |    0     |      111       |  +7   |
|--------|----------|----------------|-------|
|  1000  |    1     |      000       |  -8   |
|  1001  |    1     |      001       |  -7   |
|  1010  |    1     |      010       |  -6   |
|  1011  |    1     |      011       |  -5   |
|  1100  |    1     |      100       |  -4   |
|  1101  |    1     |      101       |  -3   |
|  1110  |    1     |      110       |  -2   |
|  1111  |    1     |      111       |  -1   |  
```

There are two major observations from the table above:

1. There is only one representation for zero: `0000`.
2. The range of representable numbers is asymmetric. For 4-bit two's complement, we can represent the positive numbers from `0` to `+7`, but the negative numbers from `-1` to `-8`.

### Interpreting The Above Table

If you take any number in the table above, flipt all its bits and add `1`, you will get its negative/positive counterpart. For example:

```
    +5 in two's complement:  0101
    
    Flip bits:               1010
    Add 1:                  +0001
                             -----
                             1011  (which is -5 in two's complement)
```

Try this for all the numbers in the table, including the zero, and negative numbers.

You will notice that the only exception is `-8` (`1000`), which does not have a positive counterpart in 4-bit two's complement. Flipping its bits and adding `1` results in `1000` again.

### Converting to Two's Complement

Given a negative decimal integer, you can find its two's complement representation using the following steps:

1. Find the binary representation of its absolute value.
2. Flip all the bits (change `0`s to `1`s and `1`s to `0`s).
3. Add `1` to the result.

**Example:** Let's find the two's complement representation of `-7` using 8 bits.

```
1.   Absolute value of -7 is 7.
     7 in binary (8 bits) is: 00000111

2.   Flip all bits: 11111000

3.   Add 1:
     11111000
   + 00000001
   -----------
     11111001
```

### Converting from Two's Complement

To convert a two's complement binary number back to decimal, we follow the same steps in reverse:

1. If the MSB is `0`, the number is positive, and you can convert it directly to decimal.
2. If the MSB is `1`, the number is negative:
    - Flip all the bits.
    - Add `1` to the result.
    - Convert the resulting binary number to decimal and add a negative sign.

**Example:** Let's convert `11111001` (which is `-7` in two's complement) back to decimal.

```
1.   MSB is `1`, so the number is negative.

2.   Flip all bits: 00000110

3.   Add 1:
     00000110
   + 00000001
   ----------- 
     00000111

4.   Convert `00000111` to decimal: 7
5.   Add negative sign: -7
```

Thus, `11111001` in two's complement represents `-7` in decimal.

### Adding Two's Complement Numbers

When adding two's complement numbers, you can use the same binary addition rules as for unsigned binary numbers. If there is a carry out of the most significant bit, it is simply discarded.

**Example 1:** Let's add `5` and `-3` using 8-bit two's complement, assuming each number is stored in 4 bits.

```  
 5 in two's complement:  0101
-3 in two's complement:  1101 +
                         ----
                         0010  (which is 2 in decimal)
```

**Example 2:** Let's add `-4` and `-3` using 5-bit two's complement.

```
-4 in two's complement:  11100
-3 in two's complement:  11101 +
                         -----
      (discard carry) 1  11001  (which is -7 in decimal)
``` 

**Example 3:** Let's add `3` and `-5` using 5-bit two's complement.

```
 3 in two's complement:  00011
-5 in two's complement:  11011 +
                         -----
                         11110  (which is -2 in decimal)
```

This shows that two's complement representation allows for straightforward binary addition, even with negative numbers.

## Video Summary

<div class="video-container">
    <iframe 
        src="https://www.youtube.com/embed/4qH4unVtJkE?si=-iPVQ2-ME61kxXIy" 
        title="Converting from decimal to binary | Applying mathematical reasoning | Pre-Algebra | Khan Academy" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen>
    </iframe>
</div>

