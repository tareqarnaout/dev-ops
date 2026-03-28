---
layout: page
title:  Nov 20
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

# Dictionaries

Consider the following data:

```
Ahmad    0771234567
Lina     0777777777
Omar     0795556666
Sara     0784443333
Salim    0778889999
...
```

This data represents a phone book, where each person's name is associated with their phone number. Using this data, we would like to be able to look up a person's phone number by their name, and to add, update, or delete entries in the phone book.

In Python, we can achieve this using what is called a **dictionary**. A dictionary is a collection of _key-value_ pairs, where each key is unique and is used to access its corresponding value. In our phone book example, the **names** are the **keys**, and the **phone numbers** are the **values**.

## Creating a Dictionary

The following code creates a dictionary representing the phone book:

```python
phone_book = {
    "Ahmad": "0771234567",
    "Lina" : "0777777777",
    "Omar" : "0795556666",
    "Sara" : "0784443333",
    "Salim": "0778889999"
}
```

## Accessing Values

You can access a value in the dictionary by using its key inside square brackets:

```python
print(phone_book["Lina"])  # Output: 0777777777
print(phone_book["Omar"])  # Output: 0795556666
print(phone_book["Ali"])   # ERROR: 'Ali' is not in the dictionary

print(phone_book[0])       # ERROR: 0 is not in the dictionary
print(phone_book[1:4])     # Keys in dictionaries are not indexed like lists
                           # Dictionaries do not support slicing
```

## Common Dictionary Operations

Here are some common operations you can perform on dictionaries:

```python
# Adding a new entry
phone_book["Huda"] = "0782223333"

# Updating an existing entry
phone_book["Ahmad"] = "0779998888"

# Deleting an entry
del phone_book["Salim"]

# Checking if a key exists
if "Lina" in phone_book:
    print("Lina's number is:", phone_book["Lina"])

# The in operator does not check for values
if "0777777777" in phone_book:
    print("This will not print because values are not checked.")

# Iterating over keys:
for name in phone_book:
    print(name, "->", phone_book[name])
```

## Example 1: Counting Character Frequencies

Define a function `char_frequency(s)` that takes a string `s` as an argument and prints the frequency of each character in the string.

```python
def char_frequency(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in frequency:
        print(char, ":", frequency[char])
```

The above code goes through each character in the string `s`. If the character is already a key in the `frequency` dictionary, it increments its count by 1. If not, it adds the character to the dictionary with a count of 1.

The code can be made more concise using the `get` method of dictionaries:

```python
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
```

The method `get(key, default)` returns the value associated with `key` if it exists; otherwise, it returns `default`. In our example, if `char` is not in `frequency`, `get` returns `0`, so we add `1` to it.
    

## Example 2

Define a function that receives a string and returns a dictionary mapping word lengths to the words in the string that have that length.

### Example

```
input: "I like programming in Python very much"
output: 
{
    1:  ['I'], 
    4:  ['like', 'very', 'much'], 
    11: ['programming'], 
    2:  ['in'], 
    6:  ['Python']
}
```

### Solution

```python
def words_by_length(s):
    dictionary = {}
    words = s.split()

    for word in words:
        n = len(word)
        if n not in dictionary:
            dictionary[n] = []
        dictionary[n].append(word)
        
    return dictionary
```

