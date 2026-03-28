---
layout: page
title:  November 13
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

# List Exercises (Part 3)
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

----

## Exercise 1 (Code Reading)

```python
def mystery(nums):
    c = [0] * 3
    for n in nums:
        c[n] += 1
    print(c)
```

What does the above code print in each of the following cases?
1. If `nums = [0, 0]`
2. If `nums = [1, 1]`
3. If `nums = [2, 2]`
4. If `nums = [0, 1, 2, 0, 1, 2, ...]` (300 elements)

<details class="jtd-accordion">
  <summary>Solution</summary>
    <ol>
        <li> <code>[2, 0, 0]</code></li>
        <li> <code>[0, 2, 0]</code></li>
        <li> <code>[0, 0, 2]</code></li>
        <li> <code>[100, 100, 100]</code></li>
    </ol>
</details>

----

## Exercise 2 (Code Reading)

Read and understand the following function, then suggest suitable name for it.

```python
def mystery(a):
    N = len(a)
    for i in range(1, N):
        if a[i] > a[0]:
            temp = a[i]
            a[i] = a[0]
            a[0] = temp
    print(a)
```

<details class="jtd-accordion">
  <summary>Solution</summary>
    The function finds the maximum element in the list `a` and places it at the front (index 0) of the list. A suitable name would be <code>move_max_to_front(a)</code>.
</details>

----

## Exercise 3 (Code Reading)

Read and understand the following function, then suggest suitable name for it.

```python
def mystery(nums, n):
    N = len(nums)
    for i in range(N-1, -1, -1):
        if nums[i] == n:
            return i
    return -1
```

<details class="jtd-accordion">
  <summary>Solution</summary>
    The function searches for the last occurrence of the integer <code>n</code> in the list <code>nums</code> and returns its index. If <code>n</code> is not found, it returns -1. A suitable name would be <code>find_last_index(nums, n)</code>.
</details>

----

## Exercise 4 (Debugging)

Find and fix the bug in the following function that is supposed to find the index of the first occurrence of `target` in the list `nums`.

```python
def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            pos = i
            break

    return pos
```

**Solution.** The variable `pos` is not initialized before the loop, and if the target is not found, it will raise an error. 

```python
def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
```

Alternatively, we can initialize `pos` to -1 before the loop:

```python
def find_index(nums, target):
    pos = -1
    for i in range(len(nums)):
        if nums[i] == target:
            pos = i
            break
    return pos
```

----

## Exercise 5 (Debugging)

Find and fix the bug in the following code, which is supposed to merge two lists by alternating their elements.

```python
def merge_lists(a, b):
    merged = []
    for i in range(len(a)):
        merged.append(a[i])
        merged.append(b[i])
    return merged
```

**Solution.** The bug is that the code assumes both lists `a` and `b` have the same length. If they don't, it will raise an `IndexError`. We should iterate up to the length of the shorter list and then append the remaining elements from the longer list.

```python
def merge_lists(a, b):
    merged = []
    if len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a

    for i in range(len(shorter)):
        merged.append(a[i])
        merged.append(b[i])

    merged.extend(longer[len(shorter):])
    return merged
```