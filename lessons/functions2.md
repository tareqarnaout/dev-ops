---
layout: page
title:  October 19
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

# Functions
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Planning, problem decomposition, code reuse, and variable scope.</span>

## Area of A Circle


### Problem Description

The steps below will walk you through the solution of the following problem.

> $$\cdot$$
>
> Write a program that reads the following information regarding a circle:
> - **The center**: Two integers representing the $$x$$ and $$y$$ coordinates of the circle center.
> - **A point**: Two integers representing the $$x$$ and $$y$$ coordinates for a point on the perimeter of the circle.
>  
> Your program must output the **_area_** of the circle.
>
> Remember that the area of the circle is $$\pi r^2$$, and the distance between two points $$(x_1, y_1)$$ and $$(x_2, y_2)$$ can be computed using the formula:
>
> $$\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$
>
> $$\cdot$$
{: .highlight}


### Step 1: Program Plan

We will begin by laying out the steps for solving the problem as comments in out program

```python
# (1) Read the coordinates of c (the center point)

# (2) Read the coordiantes of p (a point on the perimeter)

# (3) Compute the distance between c and p to find the radius

# (4) Compute the area using the formula: Pi*r^2

# (5) Print c, p, and the area
```

Breaking down a long program into steps before writing code is important. It makes the problem easier and reduces the chances of making mistakes.

### Step 2: Implementation

Next, we will fill out the code for the above steps.

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

Let's assume that we want to modify the program so that it reads information for **_two_** circles instead of one. 

The code below is an example for how the code can look like.

{% include expandable-code.html
title="Solution"
id="area-long"
language="python"
file='code/area_long.py'
%}

### Step 4: Refactoring

The above code (for two circles) clearly has a lot of duplicate code. It is long and not nice to read. We can use functions to improve (refactor) our code. 

Instead of rewriting the same code twice, we will define a function that does the work for a single circle, and then call this function twice.

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

### Further Improvements

We refactored our code because we needed to do the same thing for two circles and found that the code would be too long and repetitive. However, instead of being reactive to changes in our code, we can proactively think about whether we can break down our code further into smaller pieces that can be reused.

The **distance** computation between two points is an operation that is not only for computing the area of a circle. This is something that we might need in other applications. Therefore, we can put it in a separate function.

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


## Tracing Function Calls

To understand how programs that involve functions get executed, copy and paste th code below into [PythonTutor](https://pythontutor.com/render.html#mode=edit) and click on **Visualize**. Keep clicking **Next** to trace the execution of the code step by step and see what happens in memory.

Note the following:


{% include expandable-code.html
title="Code"
id="frames-1"
language="python"
file='code/frames-1.py'
%}

- **The flow of execution**. The code in the functions is not executed until the function is called. Execution starts from the first line outside any function definition.
- **Memory Frames**. For each function call, a frame is reserved in memory for the function call. This frame holds the memory needed for the function and is destroyed when the function ends.

## Local Variables

### Exmaple 1

What is the output of the following code?

```python
def fun():
    a = 2
    b = 4
    result = a**2 * b**2

fun()
print(a, b, result)
```

This program will crash.

The variables `a`, `b` and `result` were all defined inside the function. Therefore, they are unknown outside the function. These are called **_local_** variables, which get created when the function is called, and then get destroyed when the function completes.

You can trace the execution with PythonTutor to see what happens.

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

Note the following four different variables in the program:
- The `a` and `b` that are **_local_** to the function. These are created when the function is called and are destroyed when the function ends.
- The `a` and `b` that are defined in the **_global_** frame (after the function).

Try tracing the program using PythonTutor to understand what happens:

- The program starts at `a = 3` and then `b = 4`.
- Next, `fun` is called and two new variables are created. A new `a` holding a copy of `3` and a new `b` holding a copy of `4`. These variables are **_local_** to the function.
- Next, the values  of local variables `a` and `b` change to `9` and `16` (without affecting the other `a` and `b`).
- When the function ends, the result of `math.sqrt(9 + 16)` is returned, and the **_local_** variables in `fun` are destroyed.
- The `a` and `b` in the global frame still hold the original values `3` and `4`. 
