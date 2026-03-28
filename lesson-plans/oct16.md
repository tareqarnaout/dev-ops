---
layout: page
title:  October 16
nav_exclude: true
author: Ibrahim Albluwi
---

# **6.** Functions 1
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 16, 2025</span>

## Lecture Goals

This is the first of two lectures intended to introduce functions. In this lecture, we will cover:
- Basic terminology.
- Built-in functions.
- Syntax for defining and calling functions.

In the following lecture, we will delve more into issues like scope, call stacks, etc.

## Suggested Live-Coding Mode

Use the Python terminal (`REPL`) for showing built-in functions and then move to writing code in files when you discuss how to define a function. You can keep GitHub Copilot on to speed up writing the functions if you wish.

## Motivation

Many novices struggle to understand the value of functions because the code they write is typically a few lines of code only. Here is one way to motivate why we need to **define** new functions. Ask them: 
> _Imagine if `print()` did not exist, and that every time you wanted to print something to the screen, you had to write from scratch all the complicated and long code that does the printing. Would that be convenient?_. 

Here is a link to an implementation of the `print` function in Python: [https://github.com/mozillazg/pypy/blob/1cb1c9de8cf0e9d33507273ec1562fd1df11ab1a/pypy/module/__builtin__/app_io.py#L87](https://github.com/mozillazg/pypy/blob/1cb1c9de8cf0e9d33507273ec1562fd1df11ab1a/pypy/module/__builtin__/app_io.py#L87)

Luckily, we only need to call the function, rather than always write its code from scratch. This saves time, makes our code shorter and more readable, and reduces the possibilities of making mistakes.

## Outline

Follow the outline of [P4E.4](https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf#page=55.16). However, note the following:

- In **4.2**, you can use `max(1, 5, 0)` or `min(x, y, z)` (for example) instead of or with the examples used in the book. The book examples find the maximum and minimum characters in a string, which might not be clear to the students, given that they do not yet know that characters are represented as numbers (e.g. ASCII).

- In **4.5**, the book uses a `for` loop to show that calling `random.random()` multiple times gives different values. Do **NOT** use a `for` loop. Achieve the same thing by calling the function multiple times in the terminal.

- In **4.5**, instead of:
```python
>>> t = [1, 2, 3, 4]
>>> random.choice(t)
```
Use the following, which might save us the discussion on what lists are.
```python
>>> random.choice([1, 2, 3, 4])
```

- Emphasize the difference between:
    - Functions that are called using the module name like `random.random()` and `math.sqrt(2)`, and functions that are called directly like `max(...)`, `len(...)`, `print(...)`, etc.
    - Functions that require arguments like `max(...)`, `len(...)`, and `random.choice([...])` and functions that don't require arguments like `input()` and `random.random()`.
    - Functions that **return** values like `input()`, `max(...)`, and `len(...)` and functions that don't return values like `print(...)`.

    > All of the above should take 10-20 minutes at most. The great majority of the lecture should focus on how to **define** new functions (4.6 - 4.11).
     {: .note}

<br>

- When teaching about defining new functions, make sure students leave the lecture knowing how to **_define_** and **_call_** a function that:
    - Prints something.
    - Returns something.
    - Receives arguments.
    - Does not receive arguments.

    You can achive multiple things using a single example. For example, the following code covers printing and receiving arguments (the examples below are for reference only, you don't have to use them):

    ```python
    def print_5lines(c, n):
        print(c * n)
        print(c * n)
        print(c * n)
        print(c * n)
        print(c * n)

    print_5lines('#', 5)
    print_5lines('OK', 10)
    ```

    The following code covers calling functions that return a value:

    ```python
    # A function that checks if a grade is an excellent grade
    def is_excellent(grade):
        if grade >= 90:
            return True
        else:
            return False

    # An example of a program that uses the function
    grade = int(input("Enter Your Grade: "))
    if is_excellent(grade):
        print('MashaAllah')
    else:
        print('Try Harder')
    ```

    For the above example, you can mention that the definition of what is an _excellent_ grade can change over time. If that happens, we only change the function. If we did not have the function, we'd have to go to every place in the code where we check the grade and change it.

    Another question students might ask is:
    > _Why return then print, why not just print immediately in the function?_
    
    The function can be used in other programs, which might not want to print.



