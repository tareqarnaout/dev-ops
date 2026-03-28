---
layout: page
title:  November 4
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

# Strings (Iteration & Manipulation)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Basic syntax and examples.</span>

## Basic Iteration

The following three pieces of code all do the same thing (printing the characters of the string, each on a separate line).

```python
course = 'Introduction'
for c in course:
    print(c)
```

```python
course = 'Introduction'
for i in range(len(course)):
    print(course[i])
```

```python
course = 'Introduction'
i = 0
while i < len(course):
    print(course[i])
    i += 1
```

> The first piece of code is **[pythonic](https://realpython.com/ref/glossary/pythonic/)**, but the other two are not. while the three pieces of code all work fine, any professional Python programmer would cringe at the sight of the second and third pieces of code! Nevertheless, we include them here because they are important for examples you will see later on.
{: .note}

## Debugging

The following code attempts to print the course name in reverse. However, it has bugs. What are they? 

```python
course = 'Introduction'
for i in range(len(course), 0, -1):
    print(course[i])
```

<details class="jtd-accordion">
  <summary>Answer</summary>
    <ul>
        <li> The range should start at <code>len(course) - 1</code>. Otherwise we will get an <code>IndexError</code>.</li>
        <li> The range should end at <code>-1</code>. Otherwise we will not see the character at index <code>0</code>.</li>
    </ul>
</details>

Note that the easiest way to iterate over the characters of the string in reverse order is as follows:
```python
for c in course[::-1]:
     print(c)
```

## Application 1: Palindromes

A _palindrome_ is a string that can be read left-to-right or right-to-left. The following are examples of palindromes and non-palindromes:

**Palindromes.** `a`, `bb`, `bab`, `abccba`, `karak`, `madam`, `level`.<br>
**Non-Palindromes.** `ab`, `abcdabcd`, `ABCcba`, `hello`.

We would like to write a function that checks if a given string is a palindrome. To do this, we will use two variables:
- `i`: Goes through the indices left to right.
- `j`: Goes right-to-left.

At each iteration, we will check if if the character at `i` is the same as the character `j` or not. We stop if either the characters are different (the string is not a palindrome), or if `i` and `j` reach or cross each other.

```python
def is_palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True
```

**Follow-up question 1.** Can you write the above code using a for-loop?

{% include expandable-code.html
title="Solution"
id="palindromes-for"
language="python"
file='code/palindromes-for.py'
%}

**Follow-up question 2.** Can you write the above code using a single line?

<details class="jtd-accordion">
  <summary>Answer</summary>
    Use <code> return s == s[::-1]</code>
</details>

## Application 2: Parsing Strings

Function `find` can be used to search for a string inside another string. It returns the index of the string we are searching for, unlike the `in` operator which returns either `True` or `False`. The following are examples:

```python
# indices:  0123456789...
title =    "The Prince and The Pauper"
print(title.find("Prince"))  # 4
print(title.find("xyz"))     # -1 (not found)
print(title.find("the"))     # -1 (case-sensitive)
print(title.find("The"))     # 0 (first occurrence)
print(title.find("and"))     # 11
print(title.find(" "))       # 3 (first space)
```

We will use this function in the following application: Read emails for 10 people and verify if they belong to Jordanian domains.

Note that every email has the `@` character, and every Jordanian email ends with `.jo`. Read and understand the following code:

```python
for i in range(1, 11):
    email = input("Enter your email " + str(i) + ": ").lower()
    
    # pos_at < 0 ----> No @ in email
    # pos_at = 0 ----> email begins with @
    pos_at  = email.find('@')
    if pos_at <= 0:
        print("ERROR: Invalid jordanian email")
        continue

    domain = email[pos_at + 1:]
    pos_dot = domain.find('.jo')
    # pos_dot < 0 -----> no .jo after @
    # pos_dot = 0 -----> .jo right after @
    if pos_dot <= 0:
        print("ERROR: Invalid jordanian email")
        continue

    # extract the domain name without .jo
    print(domain[: pos_dot], "is a valid jordanian domain.")
```