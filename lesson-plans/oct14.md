---
layout: page
title:  October 14
nav_exclude: true
author: Ibrahim Albluwi
---

# **5.** Conditionals 2
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 14, 2025</span>

## Overview

This is the second lecture on Conditionals. Students already know the syntax and will practice now reading and writing code involving conditionals.

## Suggested Teaching Method
For each exercise, give students 1-2 minutes to think about the answer in pairs and then discuss the answer as a class. However, keep an eye on the clock and move faster if you run out of time.

## Warm-up Exercise

**Question**. Write a program that reads a password. If the user enters `123` output `are you serious?`, if the user enters `abc` output `No Way!`. Otherwise, print `OK!`.

```python
password = input("Enter a password: ")
if password == '123':
    print("Are you serious?")
elif password == 'abcd':
    print("No Way!")
else:
    print("OK!")
```

Live-code this exercise, or any other similar `if-elif-else` example of your choice (in 5 minutes), just to remind students about the syntax of `if`, `else`, and `elif`, and about the importance of indentation.

## Exercise 1

Present the following slide on the screen. Ask students to spend ~4 minutes in pairs to check which of the four pieces of code is correct. All the pieces of code are supposed to print the letter grade given a numerical value.

![Comic: My Password is Password123](/11102-f25/lesson-plans/images/conditionals.png)<br>
[PDF Version](/11102-f25/lesson-plans/images/conditionals.pdf)<br>
[PDF Version (with notes)](/11102-f25/lesson-plans/images/conditionals-notes.pdf)

Discuss the bugs in the upper two versions and the style issue in the fourth one (the unnecessary use of the `and` clause).

## Exercise 2

What is wrong with the following piece of code? How can we fix it?
```python
if temp > 20:
    print("Hot")
elif temp > 25:
    print("Warm")
else:
    print("Cold")
```
<details class="jtd-accordion">
  <summary>Solution</summary>
This code will never print <code>Warm</code>. To fix it, we need to swap the first condition with the second.
</details>

## Exercise 3

Write a program that reads three integers and prints the maximum. The goal of this exercise is for students to see multiple ways to solve the same problem. Give students a few minutes to think. Ask them to pull out a piece of paper and to try to write the code.

{% include expandable-code.html
title="Solution 1"
id="max3_1"
language="python"
file='code/max3_1.py'
%}

{% include expandable-code.html
title="Solution 2"
id="max3_2"
language="python"
file='code/max3_2.py'
%}

{% include expandable-code.html
title="Solution 3"
id="max3_3"
language="python"
file='code/max3_3.py'
%}

Which of these solutions doe the students find more **_readable_**?

## Exercise 4

{: .highlight-title }
> 💡 **NOTE**
>
> This exercise is for practice only. Students should not understand from it that they should avoid using these operators. On the contrary, they should see that using such operators simplifies the code.

### Exercise 4.1

Rewrite the following piece of code so that they do **not** use `and`, `or`, or `not`. 

```python
if x == 1 and y == 1:
    print("Both are 1")
else:
    print("At least one is not 1")
```

{% include expandable-code.html
title="Solution 1"
id="and_1"
language="python"
file='code/and_1.py'
%}

The following two solutions are incorrect, what is wrong with each of them?

**Non-Solution 1**.
```python
if x == 1:
    if y == 1:
        print("Both Are 1")
    else:
        print("At least one is not 1")
```

<details class="jtd-accordion">
  <summary>Explanation</summary>
Nothing will be printed if <code>x !=1 1</code>.
</details><br>

**Non-Solution 2**.
```python
if x == 1:
    if y == 1:
        print("Both Are 1")
else:
    print("At least one is not 1")
```

<details class="jtd-accordion">
  <summary>Explanation</summary>
Nothing will be printed if <code>x == 1</code> and <code>y != 1</code>.
</details><br>

{% include expandable-code.html
title="Corrected Code"
id="and_4"
language="python"
file='code/and_4.py'
%}

While this code is correct, it is not as clean as the first solution we proposed above.

### Exercise 4.2

Rewrite the following piece of code so that they do **not** use `and`, `or`, or `not`. 

```python
if x == 1 or y == 1:
    print("At least one is 1")
else:
    print("Oops!")
```

{% include expandable-code.html
title="Solution"
id="or_1"
language="python"
file='code/or_1.py'
%}
