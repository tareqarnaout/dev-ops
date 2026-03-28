---
layout: page
title:  October 28
nav_exclude: true
author: Ibrahim Albluwi
---

# **11.** Iteration (practice)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 28, 2025</span>

## Overview

The main goal of this lecture is to improve students' code reading skills.

There are two basic skills related to code reading that we would like to focus on:

1. **Tracing.** The ability to keep track of the variable values as the program executes, and to know their final values after the program finishes execution.
2. **Explaining.** The ability to explain in a few words what the code does, without describing what the code does line by line.

These two skills are distinct, but related. For example, a student might resort to tracing before explaining, while an expert might be able to explain simply by looking at the code and without having to manually trace.

Let's look at the following piece of code:

```python
def foo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime. When asked to explain what the code does, many novices resort to explaining every line. So, they might answer as follows:

> _This function has a loop that goes through all the numbers from 2 to n-1 and check if `n` divides the number. If `n` divides the number, the function returns `False`. If `n` does not divide any of the numbers, the function returns `True`._

While the description above is correct, it is a sign of low code-reading skills. It shows that the student can understand the separate lines, but can't understand what the code does overall.

To force students to think about the big picture, we will ask them to give a **meaningful name** for the function, instead of asking them to explain what the function does. This way, they will not be able to give a line-line by description.

## Lecture Outline

You can use the examples in the student [notes](/11102-f25/lessons/loops-practice). Be prepared with a few more examples, just in case you finish these examples early. The examples don't have to be code-reading examples, they can be anything related to iteration.

The fourth example is the least important one, so skip it if you run out of time. They can study it alone or ask during office hours if you don't get to it.

When solving a code reading question with the students, it is a good idea to:
1. Give them a 1-2 minutes to work in pairs on coming up with a suitable function name for the code.
2. Get a few answers from the students and write them on the board.
3. Turn on GitHub copilot in VSCode and type in a comment above the function: `# A good name for this function is`. This will automatically trigger copilot to suggest a name.
4. Trace the code on the board (explicitly showing how the values of the variables change with every iteration) to verify what the code does, and discuss which of the suggested function names is good, which is bad, and why.

You don't have to do all of these steps for every single example, but this can be a good general outline that you can make use of.