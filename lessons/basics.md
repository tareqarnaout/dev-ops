---
layout: page
title:  Basic Terminology
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;                       /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;   /* different font face */
    color: #3b7dc0ff;                     /* optional: different color */
}
</style>

# Basic Programming Terminology

## Languages

### Natural Language 
_Natural languages_ are the languages humans use to communicate, such as Arabic and English. While they are easy for humans, they can be ambiguous (the same sentence can have multiple meanings). This makes them unsuitable for giving computers commands.

### Machine Code
*Machine code* represents computer instructions using numbers (`0`s and `1`s).  
It corresponds directly to the electronic operations inside the computer’s hardware.  
Although this makes it efficient for machines, it is _very difficult for humans to read or write_.

### High-level Programming Language
*High-level programming languages* are designed to be easy for humans to read and write. They use English keywords and hide most of the details related to communicating with the computer hardware. Examples of such languages are: `Python`, `C`, `C++`, `Java`, `JavaScript`.

### Low-level Programming Language
A *low-level programming language* is closer to machine code and provides more direct control of the hardware.  
It is more readable than raw `0`s and `1`s but harder to deal with than high-level languages. You can think of it as a middle ground between high-level languages and machine code.


## Tools

### Compilers and Interpreters

Because humans prefer high-level languages while computers understand only machine code, we need *translators* to bridge the gap.

- A **compiler** translates the entire program written in a high-level language into a lower-level language (often machine code) **before execution**.  
  The result is a separate file that can be run directly by the computer.

- An **interpreter** translates and executes code **one step at a time**.  
  It does not produce a separate executable file but instead processes each instruction as the program runs.

Some programming languages use both. For example, **Python** first compiles code into an intermediate form called *bytecode*, which is then executed by an interpreter.

### Integrated Development Environment (IDE)

Programmers need a code editor to write their code. They'd also appreciate features like auto-completion, color-highlighting of the code, and organizing their work into projects. After writing their code, they need to compile and/or run it. An IDE offers all of that in one place. In this course, we will use **VSCode** as the IDE.

## Errors

Programs can fail or behave unexpectedly for different reasons. These problems are usually classified into three main categories.

### Syntax Error
Programming languages have rules (grammars) for how the instructions need to be written. A _syntax error_ occurs when these rules are broken. For example typing in python `1 + 1 +` leads to a syntax error, because an operator like `+` must be followed by a value.

### Semantic Error

A *semantic error* occurs when a statement follows the language’s syntax but has no meaningful interpretation in that language.

Even if a sentence is correct grammatically, it might not make any sense. For example, `I idea ate` has incorrect syntax, whereas `I ate an idea` is grammatically correct but makes no sense. In Python, `1 + "Hello"` has correct grammar (left-hand operand followed by operator `+` followed by right-hand operand), but adding `1` to `"Hello"` is not possible.

### Logic Error
Both the syntax and the semantics can be correct, but the program can still produce incorrect results if the _logic_ used is incorrect. For example, `circumference = width * height` has correct syntax and semantics (assuming `width` and `height` are numbers), but the equation computes the _area_, not the _circumference_!

Compilers and interpreters can detect errors due to violations of the language rules, but they can't detect _logic_ errors. It is the responsibility of the programmers to detect such errors.

### Quick Self-Check

- Can you write **other examples of each** type of error in Python?  
- Which type of error is **hardest to detect**, and why?  