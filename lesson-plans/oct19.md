---
layout: page
title:  October 19
nav_exclude: true
author: Ibrahim Albluwi
---

# **7.** Functions 2
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 19, 2025</span>

## Lecture Goals

This is the second of two lectures intended to introduce functions. In this lecture, we will:
- Re-emphasize basic concepts.
- Emphasize the value of problem decomposition and planning.
- Emphasize the value of functions for code reuse.
- Discuss call stacks and variable scope.

## Circle Area

Explain the following exercise to the students and then give them ~5 minutes to to solve it in pairs. 

While students are solving the exercise, go around the classroom to help, answer questions, and motivate students to work.

> **Exercise.** Write a program that reads the following information regarding a circle:
> - **The center**: Two integers representing the $$x$$ and $$y$$ coordinates of the circle center.
> - **A point**: Two integers representing the $$x$$ and $$y$$ coordinates for a point on the perimeter of the circle.
> 
> Your program must output the **_area_** of the circle.
>
> Remember that the area of the circle is $$\pi r^2$$, and the distance between two points $$(x_1, y_1)$$ and $$(x_2, y_2)$$ can be computed using the formula:
>
> $$[\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}]$$

> You don't have wait until all or most students are done. The goal of giving them ~5 minutes is to force them to think a bit before live-coding begins.
{: .note }

### Step 1: Program Plan

Write down the steps for completing the program as comments, as shown below. Involve the students in the process by asking them about what the steps are going to be.

```python
# (1) Read the coordinates of c (the center point)

# (2) Read the coordiantes of p (a point on the perimeter)

# (3) Compute the distance between c and p to find the radius

# (4) Compute the area

# (5) Print c, p, and the area
```

This is an important step. We need to send a message to the students that planning and breaking down the solution for a problem into steps is important.

### Step 2: Implementation

Next, start filling out the code for the steps with the students to get the following program.

```python
import math

# (1) Read the coordinates of c (the center point)
print("Reading the circle center.")
cx = int(input("Enter x: "))
cy = int(input("Enter y: "))

# (2) Read the coordiantes of p (a point on the perimeter)
print("Reading a point on the perimeter.")
px = int(input("Enter x: "))
py = int(input("Enter y: "))

# (3) Compute the distance between c and p to find the radius
xDiff = (cx - px) ** 2
yDiff = (cy - py) ** 2
r = math.sqrt(xDiff + yDiff)

# (4) Compute the area
a = math.pi * r ** 2

# (5) Print c, p, and the area
print("Center: (", cx, ", ", cy, ")")
print("Point: (", px, ",", py, ")")
print("Area = ", a)
```

### Step 3: Expansion

Ask the students about how to modify the program so that it reads information for **_two_** circles. The code below is an example for how the code can look like.

{% include expandable-code.html
title="Solution"
id="area-long"
language="python"
file='code/area_long.py'
%}

### Step 4: Refactoring

Discuss with the students about how to improve the code and make it shorter. Clearly, there is a lot of duplication. Initially we could start by defining a function that does all the work for a single circle and call it twice.

```python
import math

def circle_area():
    print("Reading the center point.")
    cx = int(input("Enter x: "))
    cy = int(input("Enter y: "))

    print("Reading a point on the perimeter.")
    px = int(input("Enter x: "))
    py = int(input("Enter y: "))

    xDiff = (cx - px) ** 2
    yDiff = (cy - py) ** 2
    r = math.sqrt(xDiff + yDiff)
    area = math.pi * r ** 2

    print("Center: (", cx, ", ", cy, ")")
    print("Point: (", px, ",", py, ")")
    print("Area 1 = ", area)


print("---- CIRCLE 1 ----")
circle_area()

print("---- CIRCLE 2 ----")
circle_area()
```

Next, we can show the following program and ask them about the benefit it offers over the previous one:

```python
import math

def distance(x1, y1, x2, y2):
    xDiff = (x1 - x2) ** 2
    yDiff = (y1 - y2) ** 2
    return math.sqrt(xDiff + yDiff)

def circle_area():
    print("Reading the center point.")
    cx = int(input("Enter x: "))
    cy = int(input("Enter y: "))

    print("Reading a point on the perimeter.")
    px = int(input("Enter x: "))
    py = int(input("Enter y: "))

    r = distance(cx, cy, px, py)
    area = math.pi * r ** 2

    print("Center: (", cx, ", ", cy, ")")
    print("Point: (", px, ",", py, ")")
    print("Area 1 = ", area)

print("---- CIRCLE 1 ----")
circle_area()

print("---- CIRCLE 2 ----")
circle_area()
```

The main value of the second solution is that we have `distance` as a function that can be used by others, or by ourselves if we decide later to do computations that involve distances between points. Without the function, we might be forced to repeat the distance computation in multiple places.

## Tracing Function Calls

Trace the program below using [PythonTutor](https://pythontutor.com/render.html#mode=edit). Emphasize the following ideas:

- **The flow of execution**. The code in the functions is not executed until the function is called. Execution starts from the first line outside any function definition.
- **Memory Frames**. For each function call, a frame is reserved in memory for the function call. This frame is destroyed when the function ends.

{% include expandable-code.html
title="Code"
id="frames-1"
language="python"
file='code/frames-1.py'
%}

## Local Variables

### Exmaple 1

Show the following program to the students and give them ~1 minute to find its output.

```python
def fun():
    a = 2
    b = 4
    result = a**2 * b**2

fun()
print(a, b, result)
```

The goal of this exercise is to emphasize the meaning of **_local_** variables.

The variables `a`, `b` and `result` were all defined inside the function. Therefore, they are unknown outside the function. These are called **_local_** variables, which get created when the function is called, and then get destroyed when the function completes.

You can trace the execution with PythonTutor to make the idea clear.

### Example 2

What is the output of the following code?

```python
import math

def fun(a, b):
    a = a ** 2
    b = b ** 2
    return math.sqrt(a + b)

a = 3
b = 4
result = fun(a, b)
print(a, b, result)
```

Note that there are four variables in the program:
- The `a` and `b` that are **_local_** to the function. These are created when the function is called and are destroyed when the function ends.
- The `a` and `b` that are defined in the **_global_** frame (after the function).

Try tracing the program using PythonTutor to understand what happens:

- The program starts at `a = 3` and then `b = 4`.
- Next, `fun` is called and two new variables are created. A new `a` holding a copy of `3` and a new `b` holding a copy of `4`.
- Next, the values  of the new `a` and `b` changes to `9` and `16` (without affecting the other `a` and `b`).
- When the function ends, the result of `math.sqrt(9 + 16)` is returned, and the **_local_** variables in `fun` are destroyed.
- The old `a` and `b` (in the global frame) still hold the original values `3` and `4`. 


## Extra Work

If you are left with time in the lecture, you can make use of it in solving more code reading or code writing exercises that involve functions.