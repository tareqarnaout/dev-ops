---
layout: page
title:  October 30
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

# Iteration (Turtle Graphics)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Bisc syntax and examples.</span>

## Overview

**Turtle Graphics** is a simple way to draw on the screen by controlling a _turtle_ that can move around the screen holding a pen. 

## Basic Operations

To start using a turtle, you need to `import turtle` and then create a turtle as shown in the code below.

```python
import turtle
t = turtle.Turtle()    # create a turtle named t
```

Moving the turtle immediately causes it to draw. For example, the following commands draws a square:

```python
t.forward(100)         # move forward 100 pixels
t.right(90)            # turn right 90 degrees

t.forward(100)         # right side
t.right(90)            

t.forward(100)         # bottom side
t.right(90)            

t.forward(100)         # left side
t.right(90)            
```

<center>
<video width="400" height="400" autoplay loop muted playsinline>
  <source src="/11102-f25/lessons/videos/1.mov" type="video/mp4">
  Your browser does not support the video tag.
</video>
</center>

There are two issues with the above code. 
- First, the screen immediately closes after drawing the square. To fix this, we'll add `turtle.done()` to the end of the program.
- Second, the drawing is too slow. To increase the speed, we will add `t.speed(10)` to the beginning of the program.

```python
import turtle

t = turtle.Turtle()    
t.speed(10)            # increase the drawing speed

t.forward(100)         
t.right(90)            
t.forward(100)         
t.right(90)            
t.forward(100)         
t.right(90)            
t.forward(100)         
t.right(90)

turtle.done()          # keep the screen open
```

The following are more commands that you can use.

```python
t.backward(50)         # move backward
t.left(90)             # turn left 90 degrees
t.right(45)            # turn right 45 degrees
t.penup()              # lift pen (move without drawing)
t.pendown()            # put pen down (draw while moving)
t.goto(100, 50)        # jump to position (x=100, y=50)
t.setheading(180)      # face a specific angle (0 = east)
t.color("red")         # change pen color
t.pensize(3)           # set pen width
t.hideturtle()         # hide the turtle cursor ▶
t.showturtle()         # show the turtle cursor ▶
t.speed(0)             # 0 = fastest, 1..10 visible animation
```

For the full list of functions, see the [Turtle Graphics documentation](https://docs.python.org/3/library/turtle.html).

## Basic Shapes

We already saw how to draw a square. Here is a more concise version using a loop:

```python
for _ in range(4):
    t.forward(100)
    t.right(90)
```

What does the following code draw?

```python
t.right(45)
for _ in range(4):
    t.forward(100)
    t.right(90)
```

<details class="jtd-accordion">
  <summary>Answer</summary>
    It draws a square rotated by 45 degrees (a diamond shape).
</details>

What if we put the above code inside a loop like this?

```python
for _ in range(8):
    t.right(45)
    for _ in range(4):
        t.forward(100)
        t.right(90)
```
<details class="jtd-accordion">
  <summary>Answer</summary>
    <video width="400" height="400" autoplay loop muted playsinline>
        <source src="/11102-f25/lessons/videos/3.mov" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</details>

What does the following code draw?

```python
length = 100
for _ in range(36):
    for _ in range(4):
        t.forward(length)
        t.right(90)
    length += 10
```

<details class="jtd-accordion">
  <summary>Answer</summary>
    <video width="400" height="400" autoplay loop muted playsinline>
        <source src="/11102-f25/lessons/videos/4.mov" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</details>

What about this?

```python
length = 100
for _ in range(36):
    for _ in range(4):
        t.forward(length)
        t.right(90)
    length += 10
    t.right(10)
```

<details class="jtd-accordion">
  <summary>Answer</summary>
    <video width="400" height="400" autoplay loop muted playsinline>
        <source src="/11102-f25/lessons/videos/5.mov" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</details>

## Randomness

Let's add some randomness to our drawings.

```python
import random
import turtle

t = turtle.Turtle()
t.speed(15)
while True:
    t.right(random.randint(0, 360))
    t.forward(random.randint(20, 50))
```

<details class="jtd-accordion">
  <summary>Answer</summary>
    <video width="400" height="400" autoplay loop muted playsinline>
        <source src="/11102-f25/lessons/videos/6.mov" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</details>

Compare the above to the following:

```python
while True:
    t.right(random.choice([0, 90]))
    t.forward(30)
```

<details class="jtd-accordion">
  <summary>Answer</summary>
    <video width="400" height="400" autoplay loop muted playsinline>
        <source src="/11102-f25/lessons/videos/7.mov" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</details>

## A Random Shapes Screen Saver

We will write a program that simulates a screen saver by drawing random shapes at random locations with random colors. Here is an example of how the output might look like:

To approach this problem, we can break it down into smaller functions:

1. A function that draws a _square_ with a given size.
2. A function that draws a _triangle_ with a given size.
3. A function that moves the turtle to a given (x, y) location without drawing.

4. The main program repeats forever:
   - Chooses a random shape (square, triangle, or circle).
   - Chooses a random location on the screen.
   - Chooses a random size.
   - Chooses a random color.
   - Chooses a random orientation.
   - Calls the appropriate function to draw the shape.

Here is the complete code:

```python
import turtle
import random

t = turtle.Turtle()
t.speed(10)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(size):
    for _ in range(3):
        t.forward(size)
        t.right(120)

t.pensize(3)
while True:
    move_to(random.randint(-200, 200), random.randint(-200, 200))
    size = random.randint(50, 150)
    color = random.choice(['red', 'blue', 'green', 'black', 'purple', 'orange'])
    t.color(color)
    t.right(random.randint(0, 360))

    shape = random.choice(['square', 'triangle', 'circle'])
    if shape == 'square':
        draw_square(size)
    elif shape == 'triangle':
        draw_triangle(size)
    elif shape == 'circle':
        t.circle(size)
```

## A Grid of Stars

Let's draw the following shape:

<center>
<video width="250" height="250" autoplay loop muted playsinline>
    <source src="/11102-f25/lessons/videos/8.mov" type="video/mp4">
    Your browser does not support the video tag.
</video>
</center>

We can break this problem down into smaller problems:
1. Drawing a single star.
2. Drawing a row of stars.
3. Drawing a grid of stars.

Let's begin by defining a function that draws a single star:

```python
def draw_star(side):
    for i in range(5):
        t.forward(side)
        t.right(144)
```

Next, we can define a function that draws a row of stars. The main idea is to repeatedly call the `draw_star` function and then move the turtle to the right to prepare for the next star:

```python
def draw_row(stars, side):
    for i in range(stars):
        draw_star(side)

        # move to the right for the next star
        t.penup()
        t.forward(side)
        t.pendown()
```

Finally, we can define a function that draws a grid of stars. The main idea is to repeatedly call the `draw_row` function and then move the turtle down to prepare for the next row. 

```python
# stars is the number of stars in each row and column.
# side is the length of the side of each star.
def draw_grid(stars, side):
    y = 0
    for i in range(stars):
        draw_row(stars, side)

        # move down one row
        y -= side
        t.penup()
        t.goto(0, y)
        t.pendown()
```

Now, we can call the `draw_grid` function to draw the grid of stars:

```python
# draw a grid of 5x5 stars, each with a side length of 50 pixels
draw_grid(5, 50)
turtle.done()
```